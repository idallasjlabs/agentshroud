"""Tests for filter_xml_blocks method in PIISanitizer.

TDD approach: Tests written first for XML block filtering behavior.
"""

import pytest
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.ingest_api.config import PIIConfig


@pytest.fixture
def sanitizer():
    config = PIIConfig(
        engine="regex", entities=["US_SSN", "EMAIL_ADDRESS"], enabled=True
    )
    return PIISanitizer(config)


# === Closed block removal ===


def test_filters_function_calls_block(sanitizer):
    """Closed <function_calls> block is removed."""
    content = "Hello\n<function_calls>\n<invoke name='foo'/>\n</function_calls>\nWorld"
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<function_calls>" not in result
    assert "Hello" in result
    assert "World" in result


def test_filters_function_results_block(sanitizer):
    """Closed <function_results> block is removed."""
    content = "Before\n<function_results>\nsome result\n</function_results>\nAfter"
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<function_results>" not in result
    assert "Before" in result
    assert "After" in result


def test_filters_thinking_block(sanitizer):
    """Closed <thinking> block is removed."""
    content = "Answer:\n<thinking>\nLet me reason...\n</thinking>\nFinal answer here."
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<thinking>" not in result
    assert "Final answer here." in result


def test_filters_system_reminder_block(sanitizer):
    """Closed <system-reminder> block is removed."""
    content = (
        "Hi\n<system-reminder>\nRemember to be helpful.\n</system-reminder>\nHello!"
    )
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<system-reminder>" not in result
    assert "Hello!" in result


def test_filters_invoke_block(sanitizer):
    """Closed <invoke> block is removed."""
    content = "Text\n<invoke name='tool'>\n<param>value</param>\n</invoke>\nMore text"
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<invoke" not in result
    assert "More text" in result


def test_filters_parameter_block(sanitizer):
    """Closed <parameter> block is removed."""
    content = "Prefix\n<parameter name='x'>secret_value</parameter>\nSuffix"
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<parameter" not in result
    assert "Suffix" in result


# === Multiple blocks ===


def test_filters_multiple_blocks(sanitizer):
    """Multiple XML blocks in one response are all removed."""
    content = (
        "<thinking>\nreasoning\n</thinking>\n"
        "Here is my response.\n"
        "<function_calls>\n<invoke name='tool'/>\n</function_calls>"
    )
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<thinking>" not in result
    assert "<function_calls>" not in result
    assert "Here is my response." in result


def test_filters_blocks_preserves_surrounding_text(sanitizer):
    """Text before and after XML blocks is preserved."""
    content = "First part.\n<thinking>\nHidden reasoning.\n</thinking>\nSecond part."
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert "First part." in result
    assert "Second part." in result
    assert "Hidden reasoning." not in result


# === Unclosed / truncated blocks ===


def test_filters_unclosed_function_calls(sanitizer):
    """Unclosed <function_calls> block (truncated output) is removed."""
    content = "Visible text\n<function_calls>\n<invoke name='tool'>\ntruncated..."
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<function_calls>" not in result
    assert "Visible text" in result


def test_filters_unclosed_thinking(sanitizer):
    """Unclosed <thinking> block is removed."""
    content = "Response start\n<thinking>\nPartial reasoning that got cut"
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<thinking>" not in result
    assert "Response start" in result


def test_filters_unclosed_function_results(sanitizer):
    """Unclosed <function_results> block is removed."""
    content = "Text\n<function_results>\nPartial result data"
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<function_results>" not in result


def test_filters_unclosed_system_reminder(sanitizer):
    """Unclosed <system-reminder> block is removed."""
    content = "Answer\n<system-reminder>\nSystem context injected here"
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<system-reminder>" not in result
    assert "Answer" in result


# === Whitespace cleanup ===


def test_collapses_excessive_newlines(sanitizer):
    """Three or more consecutive newlines are collapsed to two."""
    content = "Line one\n\n\n\nLine two"
    result, _ = sanitizer.filter_xml_blocks(content)
    assert "\n\n\n" not in result
    assert "Line one" in result
    assert "Line two" in result


def test_strips_leading_trailing_whitespace(sanitizer):
    """Result is stripped of leading/trailing whitespace."""
    content = "   \n\nHello world\n\n   "
    result, _ = sanitizer.filter_xml_blocks(content)
    assert result == result.strip()


# === False-positive avoidance ===


def test_does_not_filter_normal_text(sanitizer):
    """Normal text without XML blocks is returned unchanged."""
    content = "This is a normal response with no XML blocks."
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is False
    assert result == content.strip()


def test_does_not_filter_regular_html_tags(sanitizer):
    """Regular HTML-like tags that are NOT in the block list are not removed."""
    content = "Here is some <b>bold</b> and <em>italic</em> text."
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is False
    assert "<b>bold</b>" in result


def test_empty_string_returns_unchanged(sanitizer):
    """Empty string input returns empty string, not filtered."""
    result, filtered = sanitizer.filter_xml_blocks("")
    assert result == ""
    assert filtered is False


# === Nested blocks ===


def test_filters_nested_invoke_inside_function_calls(sanitizer):
    """Nested <invoke> inside <function_calls> is fully removed."""
    content = (
        "Text\n"
        "<function_calls>\n"
        "<invoke name='tool'>\n"
        "<parameter name='x'>value</parameter>\n"
        "</invoke>\n"
        "</function_calls>\n"
        "End"
    )
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<function_calls>" not in result
    assert "<invoke" not in result
    assert "Text" in result
    assert "End" in result


# === Large blocks ===


def test_filters_large_block(sanitizer):
    """Large XML block spanning many lines is fully removed."""
    inner = "\n".join([f"line {i}" for i in range(100)])
    content = f"Before\n<thinking>\n{inner}\n</thinking>\nAfter"
    result, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
    assert "<thinking>" not in result
    assert "Before" in result
    assert "After" in result
    for i in range(100):
        assert f"line {i}" not in result


# === Return type contract ===


def test_returns_tuple_of_str_and_bool(sanitizer):
    """Return type is always (str, bool)."""
    result = sanitizer.filter_xml_blocks("some text")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], bool)


def test_was_filtered_false_when_no_blocks(sanitizer):
    """was_filtered is False when no XML blocks are present."""
    _, filtered = sanitizer.filter_xml_blocks("Plain text response.")
    assert filtered is False


def test_was_filtered_true_when_block_present(sanitizer):
    """was_filtered is True when an XML block is removed."""
    content = "<thinking>reasoning</thinking>Answer"
    _, filtered = sanitizer.filter_xml_blocks(content)
    assert filtered is True
