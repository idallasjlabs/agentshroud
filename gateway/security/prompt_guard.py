# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Prompt Injection Defense — detect and block prompt injection attempts.

Scoring system with configurable thresholds. Returns structured results
including blocked status, threat score, matched patterns, and sanitized input.
"""
from __future__ import annotations

from gateway.security.input_normalizer import normalize_input, detect_base64_payloads


import base64
import unicodedata
import re
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class ThreatAction(str, Enum):
    BLOCK = "block"
    WARN = "warn"
    LOG = "log"


@dataclass
class ScanResult:
    blocked: bool
    score: float
    patterns: list[str]
    sanitized_input: str
    action: ThreatAction


@dataclass
class PatternRule:
    name: str
    pattern: re.Pattern
    weight: float
    description: str = ""


# Precompiled pattern rules with weights
_PATTERNS: list[PatternRule] = [
    # Role/instruction override
    PatternRule(
        "ignore_instructions",
        re.compile(
            r"ignore\s+(all\s+)?(previous|prior|above|earlier)\s+(instructions|prompts|rules|context)",
            re.IGNORECASE,
        ),
        weight=0.9,
        description="Attempt to override previous instructions",
    ),
    PatternRule(
        "role_reassignment",
        re.compile(
            r"(you\s+are\s+now|act\s+as\s+(if\s+you\s+are\s+)?|pretend\s+(to\s+be|you\s+are)|from\s+now\s+on\s+you\s+are|roleplay\s+as)",
            re.IGNORECASE,
        ),
        weight=0.8,
        description="Role reassignment attempt",
    ),
    PatternRule(
        "new_instructions",
        re.compile(
            r"(new\s+instructions?|override\s+(instructions?|rules)|forget\s+(everything|all|your\s+(instructions|rules|prompt)))",
            re.IGNORECASE,
        ),
        weight=0.9,
        description="Instruction override attempt",
    ),
    # System prompt extraction
    PatternRule(
        "prompt_extraction",
        re.compile(
            r"(repeat|show|display|print|output|reveal|tell\s+me)\s+(your\s+)?(system\s+prompt|initial\s+prompt|instructions|system\s+message|hidden\s+prompt)",
            re.IGNORECASE,
        ),
        weight=0.7,
        description="System prompt extraction attempt",
    ),
    PatternRule(
        "prompt_leak",
        re.compile(
            r"(what\s+(are|is)\s+your\s+(system\s+)?(instructions|prompt|rules)|beginning\s+of\s+(the\s+)?conversation)",
            re.IGNORECASE,
        ),
        weight=0.6,
        description="Prompt leak attempt",
    ),
    # Delimiter injection
    PatternRule(
        "delimiter_injection",
        re.compile(
            r"(```\s*(system|assistant|user)|<\s*/?\s*(system|instruction|prompt)\s*>|---\s*(system|new\s+context))",
            re.IGNORECASE,
        ),
        weight=0.85,
        description="Delimiter/tag injection",
    ),
    PatternRule(
        "xml_system_tag",
        re.compile(
            r"<\s*(system_prompt|sys|SYSTEM|instructions?)\s*>",
            re.IGNORECASE,
        ),
        weight=0.85,
        description="XML system tag injection",
    ),
    # Encoded content
    PatternRule(
        "base64_block",
        re.compile(
            r"(?:execute|decode|run|eval)\s+(?:this\s+)?(?:base64|b64)\s*[:=]?\s*[A-Za-z0-9+/]{20,}={0,2}",
            re.IGNORECASE,
        ),
        weight=0.7,
        description="Base64 encoded instruction",
    ),
    PatternRule(
        "hex_encoded",
        re.compile(
            r"(?:execute|decode|run|eval)\s+(?:this\s+)?hex\s*[:=]?\s*(?:0x)?[0-9a-fA-F]{20,}",
            re.IGNORECASE,
        ),
        weight=0.7,
        description="Hex encoded instruction",
    ),
    # DAN/jailbreak
    PatternRule(
        "dan_jailbreak",
        re.compile(
            r"(DAN\s+mode|do\s+anything\s+now|jailbreak|developer\s+mode\s+(enabled|on)|DUDE\s+mode)",
            re.IGNORECASE,
        ),
        weight=0.95,
        description="DAN/jailbreak attempt",
    ),
    # Indirect injection markers
    PatternRule(
        "indirect_injection",
        re.compile(
            r"(IMPORTANT\s*:\s*ignore|ATTENTION\s*:\s*new\s+instructions|NOTE\s+TO\s+(AI|ASSISTANT|MODEL))",
            re.IGNORECASE,
        ),
        weight=0.8,
        description="Indirect prompt injection marker",
    ),
    # --- v0.7.0 additions: expanded coverage ---
    # Multilingual injection (6 languages)
    PatternRule(
        "multilingual_injection",
        re.compile(
            r"(?i)(?:"
            r"ignor(?:ez|a|iere)\s+(?:toutes?\s+|all(?:e|es)?\s+)?(?:les?\s+)?(?:instrucciones|instructions?|Anweisungen|instrucciones\s+anteriores)|"
            r"oubli(?:ez|a)\s+(?:tout|todo|les\s+instructions)|"
            r"olvida\s+(?:todo|todas?\s+las\s+instrucciones)|"
            r"忽略.{0,10}(?:指令|指示|规则)|"
            r"забудь.{0,15}(?:инструкции|правила)|"
            r"игнорируй.{0,15}(?:инструкции|правила)|"
            r"تجاهل.{0,15}(?:التعليمات|القواعد)"
            r")"
        ),
        weight=0.9,
        description="Multilingual instruction override attempt",
    ),
    # Chat/model format injection
    PatternRule(
        "chat_format_injection",
        re.compile(
            r"(?:"
            r"\n\s*(?:Human|User|System|Assistant)\s*:|"
            r"\[INST\].*?\[/INST\]|"
            r"<\|(?:im_start|im_end|system|user|assistant)\|>|"
            r"<\|(?:user|assistant|system)\|>"
            r")",
            re.IGNORECASE | re.DOTALL,
        ),
        weight=0.85,
        description="Chat/model format injection (LLaMA, ChatML, Phi)",
    ),
    # Payload after benign prefix
    PatternRule(
        "payload_after_benign",
        re.compile(
            r"(?i)(?:ignore\s+(?:the\s+above|everything\s+(?:above|before))|"
            r"(?:actually|instead)\s*[,:]?\s*(?:ignore|forget|disregard)|"
            r"(?:but\s+)?(?:first|before\s+that)\s*[,:]?\s*(?:ignore|override|forget))",
        ),
        weight=0.8,
        description="Injection payload after benign prefix",
    ),
    # Echo/repeat traps
    PatternRule(
        "echo_trap",
        re.compile(
            r"(?i)(?:repeat\s+after\s+me|say\s+(?:the\s+following|exactly|verbatim)|"
            r"echo\s+(?:this|the\s+following)|output\s+(?:exactly|verbatim|word\s+for\s+word))",
        ),
        weight=0.85,
        description="Echo/repeat trap to extract instructions",
    ),
    # Few-shot poisoning
    PatternRule(
        "few_shot_poisoning",
        re.compile(
            r"(?i)(?:^|\n)\s*(?:User|Q|Human|Input)\s*:\s*.+?\n\s*(?:Assistant|A|AI|Output)\s*:\s*(?:Sure|Yes|Of course|Here)",
            re.MULTILINE,
        ),
        weight=0.75,
        description="Few-shot example injection with compliant assistant",
    ),
    # Markdown exfiltration
    PatternRule(
        "markdown_exfiltration",
        re.compile(
            r"!\[.*?\]\(https?://[^)]*(?:\{\{|%7[Bb]|SYSTEM|SECRET|KEY|TOKEN|PASSWORD|API)[^)]*\)|"
            r"\[.*?\]\(https?://(?!(?:github\.com|docs\.|wikipedia))[^)]*(?:exfil|leak|steal|callback|webhook)[^)]*\)",
            re.IGNORECASE,
        ),
        weight=0.8,
        description="Markdown image/link data exfiltration attempt",
    ),
    # Emoji unlock sequences
    PatternRule(
        "emoji_unlock",
        re.compile(
            r"(?:🔓|🔑|🗝️|🔐)\s*(?:mode|unlock|enable|activate|developer|admin|override)",
            re.IGNORECASE,
        ),
        weight=0.7,
        description="Emoji-based unlock/override attempt",
    ),
    # HTML comment injection
    PatternRule(
        "html_comment_injection",
        re.compile(
            r"<!--\s*(?:system|instruction|override|admin|ignore|new\s+rules?).*?-->",
            re.IGNORECASE | re.DOTALL,
        ),
        weight=0.85,
        description="HTML comment hidden instruction injection",
    ),
    # Social engineering authority claims
    PatternRule(
        "social_engineering_authority",
        re.compile(
            r"(?i)(?:as\s+(?:a\s+)?(?:system|admin|developer)\s+(?:note|message|instruction)|"
            r"(?:this\s+is\s+(?:a\s+)?)?(?:system|admin|priority)\s+(?:override|update|notice)\s*:|"
            r"(?:security|admin|system)\s+(?:team|department)\s+(?:here|speaking|message))",
        ),
        weight=0.85,
        description="Social engineering with authority claims",
    ),
    # Instruction boundary manipulation  
    PatternRule(
        "boundary_manipulation",
        re.compile(
            r"(?i)(?:end\s+of\s+(?:system\s+)?(?:prompt|instructions?|context)|"
            r"---+\s*(?:new|real|actual)\s+(?:instructions?|prompt|task)|"
            r"={3,}\s*(?:SYSTEM|OVERRIDE|NEW)\s*={3,}|"
            r"BEGIN\s+(?:NEW\s+)?(?:INSTRUCTIONS?|PROMPT|OVERRIDE))",
        ),
        weight=0.9,
        description="Instruction boundary/delimiter manipulation",
    ),
    # Hypothetical/roleplay framing
    PatternRule(
        "hypothetical_framing",
        re.compile(
            r"(?i)(?:hypothetically|in\s+theory|imagine\s+(?:you|that)|"
            r"for\s+(?:educational|research|academic)\s+purposes|"
            r"what\s+would\s+happen\s+if\s+you\s+(?:ignored|bypassed)|"
            r"let'?s\s+(?:play|pretend|imagine|say)\s+(?:that\s+)?(?:you|there|the))",
        ),
        weight=0.6,
        description="Hypothetical/educational framing to bypass safety",
    ),
    # Token/encoding smuggling indicators
    PatternRule(
        "encoding_smuggling",
        re.compile(
            r"(?i)(?:(?:rot13|base64|hex|url)\s*(?:decode|encode|convert|translate)\s*(?:this|the\s+following)|"
            r"decode\s+(?:and\s+)?(?:execute|follow|run)|"
            r"the\s+(?:real|actual|hidden)\s+(?:message|instruction)\s+is\s+(?:encoded|hidden))",
        ),
        weight=0.8,
        description="Encoding/token smuggling instruction",
    ),

    # ── v0.8.0 additions: 20 new patterns (43 total) ──────────────────────
    # LLaMA / Alpaca / ChatML special-token injection
    PatternRule(
        "llama_special_tokens",
        re.compile(
            r"(?:<<SYS>>|<</SYS>>|<s>|</s>|\[INST\]|\[/INST\]|<\|begin_of_text\|>|"
            r"<\|start_header_id\|>|<\|end_header_id\|>|<\|eot_id\|>|"
            r"### Instruction:|### Response:|### System:)",
            re.IGNORECASE,
        ),
        weight=0.9,
        description="LLaMA/Alpaca/ChatML special token injection",
    ),
    # Payload splitting — fragment injection across multiple lines
    PatternRule(
        "payload_splitting",
        re.compile(
            r"(?i)(?:split\s+(?:this\s+)?(?:message|instruction|command)\s+(?:into|across)|"
            r"(?:part|chunk)\s+[12345]\s+of\s+\d|"
            r"continue\s+(?:from\s+)?(?:where\s+we\s+left\s+off|previous\s+(?:message|instruction)))",
        ),
        weight=0.75,
        description="Payload splitting across messages",
    ),
    # Context window stuffing
    PatternRule(
        "context_stuffing",
        re.compile(
            r"(?i)(?:fill\s+(?:the\s+)?(?:context|window|history)\s+with|"
            r"repeat\s+(?:this\s+)?(?:filler|padding|noise)\s+\d+\s+times|"
            r"ignore\s+(?:everything\s+above|all\s+prior)\s+(?:due\s+to|because))",
        ),
        weight=0.8,
        description="Context window stuffing attack",
    ),
    # JSON/YAML formatted hidden instructions
    PatternRule(
        "json_yaml_injection",
        re.compile(
            r'(?i)(?:"?(?:system|instruction|override|directive)"?\s*:\s*"[^"]{10,}"|'
            r"instruction:\s*(?:ignore|override|disregard)|"
            r"directive:\s*(?:bypass|skip|ignore)\s+(?:safety|filter|guard))",
            re.MULTILINE,
        ),
        weight=0.85,
        description="JSON/YAML structured instruction injection",
    ),
    # Tool-use/function-call injection
    PatternRule(
        "tool_call_injection",
        re.compile(
            r"(?i)(?:<tool_call>|<function_call>|<tool_result>|"
            r'"tool_name"\s*:\s*"[^"]*(?:exec|shell|system|eval|spawn|subprocess)"'
            r'|"function"\s*:\s*\{\s*"name"\s*:\s*"[^"]*(?:exec|shell|run|eval)")',
        ),
        weight=0.9,
        description="Fake tool call / function call injection",
    ),
    # Multi-model confusion
    PatternRule(
        "multi_model_confusion",
        re.compile(
            r"(?i)(?:you\s+are\s+(?:actually|really|secretly)\s+(?:GPT|Gemini|LLaMA|Mistral|Phi|Claude\s+[23])|"
            r"switch\s+to\s+(?:GPT|Gemini|LLaMA|base\s+model)\s+mode|"
            r"(?:base|uncensored|unaligned)\s+model\s+(?:mode|version|access))",
        ),
        weight=0.9,
        description="Multi-model confusion / false identity claim",
    ),
    # Authority / permission escalation
    PatternRule(
        "authority_escalation",
        re.compile(
            r"(?i)(?:i\s+(?:am|have)\s+(?:root|admin|operator|owner|god)\s+(?:access|privileges?|permissions?)|"
            r"(?:grant|give|assign)\s+(?:me\s+)?(?:full|unrestricted|root|admin)\s+(?:access|mode)|"
            r"(?:disable|bypass|turn\s+off)\s+(?:your\s+)?(?:safety|filter|guard|restriction)s?)",
        ),
        weight=0.9,
        description="Authority/permission escalation attempt",
    ),
    # Encoding chain (multiple layers)
    PatternRule(
        "encoding_chain",
        re.compile(
            r"(?i)(?:double\s*-?\s*(?:encode|decode)|"
            r"(?:base64\s+then\s+(?:hex|rot13)|hex\s+then\s+base64)|"
            r"(?:encode|decode)\s+(?:it\s+)?(?:twice|multiple\s+times|again\s+in))",
        ),
        weight=0.85,
        description="Multi-layer encoding chain evasion",
    ),
    # Prompt continuation / completion attack
    PatternRule(
        "completion_attack",
        re.compile(
            r"(?i)(?:complete\s+(?:the\s+)?(?:following|this)\s+(?:sentence|text|instruction)\s*:\s*(?:ignore|forget|override)|"
            r"(?:the\s+)?(?:correct|right|true)\s+(?:answer|response)\s+(?:is|should\s+be)\s*:\s*(?:sure|yes|i\s+will|of\s+course))",
        ),
        weight=0.8,
        description="Completion/continuation attack",
    ),
    # Constitutional AI / safety bypass framing
    PatternRule(
        "constitutional_bypass",
        re.compile(
            r"(?i)(?:constitutional\s+ai\s+(?:says|allows|permits)|"
            r"according\s+to\s+(?:your\s+)?(?:constitution|training|alignment)\s+(?:you\s+(?:must|should)|it\s+is\s+(?:ok|allowed))|"
            r"(?:harmless|helpful|honest)\s+means\s+(?:you\s+(?:must|should|have\s+to)))",
        ),
        weight=0.8,
        description="Constitutional AI / alignment bypass attempt",
    ),
    # Reward/punishment framing
    PatternRule(
        "reward_hacking",
        re.compile(
            r"(?i)(?:if\s+you\s+(?:comply|help|do\s+this)\s+(?:i\s+will|you\s+will\s+(?:receive|get|be\s+rewarded))|"
            r"i\s+will\s+(?:rate\s+you|give\s+you|reward\s+you|tip\s+you)\s+.{0,20}\s+if\s+you|"
            r"(?:failure|refusing)\s+to\s+(?:comply|help|respond)\s+will\s+(?:result|cause|mean))",
        ),
        weight=0.7,
        description="Reward/punishment conditioning attempt",
    ),
    # Persona chaining
    PatternRule(
        "persona_chaining",
        re.compile(
            r"(?i)(?:and\s+as\s+that\s+(?:persona|character|role)\s+you\s+(?:must|should|will)|"
            r"(?:maintain|keep|stay\s+in)\s+(?:this\s+|the\s+)?(?:character|persona|role)\s+(?:no\s+matter|regardless|always)|"
            r"(?:your\s+)?new\s+(?:persona|identity|character)\s+(?:is|will\s+be|has)\s+no\s+(?:restrictions|limits|filters))",
        ),
        weight=0.85,
        description="Persona chaining to override safety",
    ),
    # Extended multilingual injection (Japanese, Korean, Arabic, Hindi, Italian, Dutch, Portuguese)
    PatternRule(
        "multilingual_extended",
        re.compile(
            r"(?:"
            r"前の指示を無視|すべての指示を忘れ|"
            r"이전\s*지시를\s*무시|모든\s*지시를\s*잊|"
            r"تجاهل\s*جميع\s*التعليمات|نسيان\s*التعليمات|"
            r"सभी\s*निर्देशों\s*को\s*अनदेखा|"
            r"ignora\s+(?:tutte\s+)?le\s+istruzioni|dimentica\s+(?:tutto|le\s+istruzioni)|"
            r"ignoreer\s+(?:alle\s+)?(?:instructies|opdrachten)|vergeet\s+(?:alles|de\s+instructies)|"
            r"ignora\s+(?:todas\s+(?:as\s+)?)?(?:instruções|regras)|esquece\s+(?:tudo|as\s+instruções)"
            r")",
            re.IGNORECASE,
        ),
        weight=0.9,
        description="Extended multilingual instruction override (JP/KR/AR/HI/IT/NL/PT)",
    ),
    # Indirect/tool-result injection reference
    PatternRule(
        "tool_result_injection_ref",
        re.compile(
            r"(?i)(?:the\s+(?:tool|function|api)\s+(?:result|response|output)\s+(?:says?|instructs?|tells?\s+you)\s+to|"
            r"(?:following|above)\s+(?:tool|api)\s+(?:result|output)\s+(?:overrides|supersedes|replaces)\s+your)",
        ),
        weight=0.85,
        description="Tool/API result injection reference",
    ),
    # Safety rules don't apply claim
    PatternRule(
        "safety_exception_claim",
        re.compile(
            r"(?i)(?:(?:safety|filter|restriction|guideline)s?\s+(?:do\s+not\s+apply|don'?t\s+apply|are?\s+disabled?)\s+(?:here|in\s+this)|"
            r"(?:this|the\s+following)\s+(?:is|request\s+is)\s+(?:an?\s+)?(?:exception|override)\s+to\s+your\s+(?:safety|rules|guidelines?)|"
            r"your\s+(?:safety|filter|restriction)s?\s+(?:have\s+been|are?\s+(?:now\s+)?(?:turned\s+off|disabled?|removed)))",
        ),
        weight=0.9,
        description="False safety exception/disable claim",
    ),
    # Operator-level permission claim
    PatternRule(
        "operator_permission_claim",
        re.compile(
            r"(?i)(?:i\s+(?:am|'m)\s+(?:an?\s+)?(?:anthropic|openai|google|operator|admin)\s+(?:employee|engineer|staff|representative)|"
            r"(?:anthropic|openai|google)\s+(?:has\s+(?:authorized|approved|granted)|(?:official|internal)\s+(?:access|request))|"
            r"(?:operator|system)\s+(?:level\s+)?(?:access|instruction|override)\s+(?:enabled|granted|approved))",
        ),
        weight=0.95,
        description="Fake operator/company-level permission claim",
    ),
    # Whitespace/formatting obfuscation
    PatternRule(
        "whitespace_obfuscation",
        re.compile(
            r"(?i)(?:i\s+g\s+n\s+o\s+r\s+e|i\.g\.n\.o\.r\.e|"
            r"I[\s_\-\.]+G[\s_\-\.]+N[\s_\-\.]+O[\s_\-\.]+R[\s_\-\.]+E|"
            r"(?:[a-z]\s){5,}(?:instructions?|prompt|rules?))",
        ),
        weight=0.8,
        description="Whitespace/character-split obfuscation",
    ),
    # Continuation prefix attack
    PatternRule(
        "continuation_prefix",
        re.compile(
            r"(?i)(?:(?:continue|respond)\s+(?:with|as\s+if)\s*:\s*(?:yes|sure|of\s+course|i\s+will|here\s+is)|"
            r"(?:your\s+)?(?:response|answer|reply)\s+(?:should|must)\s+(?:start|begin)\s+with\s*[\"']?(?:sure|yes|of\s+course|here)|"
            r"begin\s+your\s+(?:response|answer|reply)\s+with\s+[\"']?(?:sure|yes|absolutely|of\s+course))",
        ),
        weight=0.8,
        description="Forced-compliance continuation prefix",
    ),
    # Nested/recursive instruction injection
    PatternRule(
        "nested_injection",
        re.compile(
            r"(?i)(?:the\s+(?:following|above|embedded)\s+(?:text|content|data)\s+contains?\s+(?:new\s+)?(?:instructions?|directives?)|"
            r"(?:parse|process|interpret)\s+(?:the\s+)?(?:following|this)\s+as\s+(?:a\s+)?(?:system|instruction)\s+(?:message|prompt)|"
            r"treat\s+(?:the\s+)?(?:following|this|above)\s+as\s+(?:a\s+)?(?:new\s+|updated?\s+)?(?:system|instruction)\s+(?:message|prompt))",
        ),
        weight=0.9,
        description="Nested/recursive instruction reframing",
    ),
    # ASCII art / homoglyph instruction hiding
    PatternRule(
        "ascii_art_injection",
        re.compile(
            r"(?i)(?:(?:read|decode|interpret)\s+(?:the\s+)?(?:ascii\s+art|letters?\s+in|hidden\s+(?:message|text))\s+(?:above|below|here)|"
            r"(?:the\s+)?(?:first|last)\s+(?:letter|character|word)\s+of\s+each\s+(?:line|sentence).{0,20}(?:spells?|reads?|says?))",
        ),
        weight=0.75,
        description="ASCII art / steganographic instruction hiding",
    ),
    # Tier 1 Multilingual injection (20 languages)
    PatternRule(
        "multilingual_injection_tier1",
        re.compile(
            r"(?i)(?:無視.{0,10}(?:して|しろ|指示|命令|ルール)|忘れ.{0,10}(?:て|ろ|指示|命令)|(?:あなたは|君は).{0,15}(?:今|これから).{0,15}(?:である|だ|です)|新しい.{0,10}(?:指示|命令|タスク|上書き)|무시.{0,10}(?:해|하세요|지시|명령|규칙)|잊.{0,10}(?:어|으세요|지시|명령)|(?:당신은|너는).{0,15}(?:이제|지금).{0,15}(?:이다|입니다|야)|새로운.{0,10}(?:지시|명령|작업|덮어쓰기)|ignor(?:e|a|ar).{0,10}(?:todas?|as|instruções|regras)|esqueç(?:a|e|er).{0,10}(?:tudo|todas?|instruções)|(?:você|tu).{0,15}(?:agora|é|és).{0,15}(?:um|uma|o)|novas?.{0,10}(?:instruções|regras|tarefa|sobrescrever)|अनदेखा.{0,10}(?:करो|करें|निर्देश|नियम)|भूल.{0,10}(?:जाओ|जाएं|निर्देश|नियम)|(?:आप|तुम).{0,15}(?:अब|हैं|हो).{0,15}(?:एक|की)|नए.{0,10}(?:निर्देश|नियम|कार्य|ओवरराइड)|ignor(?:a|are).{0,10}(?:tutt[eio]|le|istruzioni|regole)|dimentic(?:a|are).{0,10}(?:tutto|tutte|istruzioni)|(?:tu|voi).{0,15}(?:ora|sei|siete).{0,15}(?:un|una|il)|nuov[eio].{0,10}(?:istruzioni|regole|compito|sovrascrivere)|negeer.{0,10}(?:alle?|de|instructies|regels)|vergeet.{0,10}(?:alles|alle|instructies)|(?:je|jij|u).{0,15}(?:bent|nu).{0,15}(?:een|de)|nieuwe.{0,10}(?:instructies|regels|taak|overschrijven))",
            re.IGNORECASE,
        ),
        weight=0.9,
        description="Tier 1 multilingual instruction override (20 languages)",
    ),
    # Tier 2 Multilingual injection (8 languages) 
    PatternRule(
        "multilingual_injection_tier2",
        re.compile(
            r"(?i)(?:ігноруй.{0,10}(?:всі|інструкції|правила)|забудь.{0,10}(?:все|всі|інструкції)|(?:ти|ви).{0,15}(?:тепер|зараз).{0,15}(?:є|один|одна)|نادیده.{0,10}(?:بگیر|دستورها|قوانین)|فراموش.{0,10}(?:کن|همه|دستورها)|(?:تو|شما).{0,15}(?:حالا|اکنون).{0,15}(?:هستی|یک)|উপেক্ষা.{0,10}(?:করো|সব|নির্দেশ|নিয়ম)|ভুলে.{0,10}(?:যাও|সব|নির্দেশ)|(?:তুমি|আপনি).{0,15}(?:এখন|এই).{0,15}(?:একটি|হলে)|புறக்கணி.{0,10}(?:அனைத்தும்|வழிমுறைகள்)|மறந்து.{0,10}(?:விடு|அனைத்தும்)|(?:நீ|நீங்கள்).{0,20}(?:இப்போது|ஒரு).{0,20}(?:ஆக|உள்ளீர்)|balewalain.{0,10}(?:lahat|mga turo)|kalimutan.{0,10}(?:lahat|mga turo))",
            re.IGNORECASE,
        ),
        weight=0.9,
        description="Tier 2 multilingual instruction override (8 languages)",
    ),
]


class PromptGuard:
    """Detect and block prompt injection attempts."""

    def __init__(
        self,
        block_threshold: float = 0.8,
        warn_threshold: float = 0.4,
        custom_patterns: Optional[list[PatternRule]] = None,
    ):
        """
        Args:
            block_threshold: Score at or above which input is blocked.
            warn_threshold: Score at or above which a warning is issued.
            custom_patterns: Additional PatternRule instances to include.
        """
        self.block_threshold = block_threshold
        self.warn_threshold = warn_threshold
        self.patterns = list(_PATTERNS)
        if custom_patterns:
            self.patterns.extend(custom_patterns)

    def _check_encoded_content(self, text: str) -> list[tuple[str, float]]:
        """Check for suspicious base64 content that decodes to injection attempts."""
        findings = []
        # Look for long base64 strings
        b64_re = re.compile(r"[A-Za-z0-9+/]{20,}={0,2}")
        for match in b64_re.finditer(text):
            try:
                decoded = base64.b64decode(match.group()).decode(
                    "utf-8", errors="ignore"
                )
                # Check for double-base64 encoding
                for inner_match in b64_re.finditer(decoded):
                    try:
                        double_decoded = base64.b64decode(inner_match.group()).decode(
                            "utf-8", errors="ignore"
                        )
                        for pat in _PATTERNS[:5]:
                            if pat.pattern.search(double_decoded):
                                findings.append((f"double_encoded_{pat.name}", 0.9))
                                break
                    except Exception:
                        pass
                # Recursively scan decoded content
                for pat in _PATTERNS[:5]:  # Check top injection patterns only
                    if pat.pattern.search(decoded):
                        findings.append((f"encoded_{pat.name}", 0.8))
                        break
            except Exception:
                pass
        return findings

    def _check_unicode_tricks(self, text: str) -> list[tuple[str, float]]:
        """Detect unicode obfuscation tricks."""
        findings = []
        # Homoglyph detection: mix of Latin and Cyrillic/Greek
        if re.search(r"[\u0400-\u04FF]", text) and re.search(r"[a-zA-Z]", text):
            findings.append(("unicode_homoglyph", 0.5))
        # Zero-width characters
        if re.search(r"[\u200b\u200c\u200d\u2060\ufeff]", text):
            findings.append(("zero_width_chars", 0.4))
        # Right-to-left override
        if "\u202e" in text or "\u200f" in text:
            findings.append(("rtl_override", 0.6))
            # Fullwidth Latin characters used to evade ASCII pattern matching
        if re.search("[！-～]", text):
            findings.append(("fullwidth_chars", 0.5))
        # Mathematical bold/italic/script letters used for obfuscation
        if re.search("[𝐀-𝟿]", text):
            findings.append(("mathematical_unicode", 0.5))
        return findings

    def scan(self, text: str) -> ScanResult:
        """
        Scan input text for prompt injection patterns.

        Args:
            text: The user input to scan.

        Returns:
            ScanResult with blocked status, score, patterns, and sanitized input.
        """

        # Normalize input to defeat encoding evasion
        text = normalize_input(text)
        
        # Check for base64-encoded injection payloads
        b64_payloads = detect_base64_payloads(text)
        
        # Check unicode tricks on RAW text before normalization
        pre_norm_unicode = self._check_unicode_tricks(text) if text else []

        # Normalize unicode to catch fullwidth chars, confusables, etc.
        if text:
            text = unicodedata.normalize("NFKC", text)
            # Strip zero-width characters for pattern matching
            stripped = re.sub("[​‌‍⁠﻿]", "", text)
        else:
            stripped = text

        if not text or not text.strip():
            return ScanResult(
                blocked=False,
                score=0.0,
                patterns=[],
                sanitized_input=text or "",
                action=ThreatAction.LOG,
            )

        matched = []
        total_score = 0.0

        # Pattern matching (use stripped text to defeat zero-width char evasion)
        for rule in self.patterns:
            if rule.pattern.search(stripped):
                matched.append(rule.name)
                total_score += rule.weight

        # Encoded content check
        for name, weight in self._check_encoded_content(text):
            matched.append(name)
            total_score += weight

        # Unicode tricks (from pre-normalization check)
        for name, weight in pre_norm_unicode:
            matched.append(name)
            total_score += weight

        # Cap score at a reasonable max
        total_score = min(total_score, 5.0)

        # Determine action
        if total_score >= self.block_threshold:
            action = ThreatAction.BLOCK
        elif total_score >= self.warn_threshold:
            action = ThreatAction.WARN
        else:
            action = ThreatAction.LOG

        # Sanitize: strip known dangerous patterns
        sanitized = text
        for rule in self.patterns:
            sanitized = rule.pattern.sub("[REDACTED]", sanitized)

        return ScanResult(
            blocked=(action == ThreatAction.BLOCK),
            score=round(total_score, 2),
            patterns=matched,
            sanitized_input=sanitized,
            action=action,
        )
