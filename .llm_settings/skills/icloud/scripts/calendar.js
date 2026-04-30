#!/usr/bin/env node
/**
 * iCloud Calendar Management
 * Manages calendar events via CalDAV
 */

const https = require('https');
const { execSync } = require('child_process');

const CONFIG = {
    host: 'caldav.icloud.com',
    port: 443,
    username: 'agentshroud.ai@gmail.com'
};

function getCredentials() {
    const password = execSync(
        '1password-skill get-field "Apple ID - therealidallasj" "oenclaw bot password"',
        { encoding: 'utf8' }
    ).trim().replace(/-/g, '');
    
    return {
        username: CONFIG.username,
        password,
        auth: 'Basic ' + Buffer.from(`${CONFIG.username}:${password}`).toString('base64')
    };
}

function makeRequest(method, path, body = '', headers = {}) {
    return new Promise((resolve, reject) => {
        const creds = getCredentials();
        
        const options = {
            hostname: CONFIG.host,
            port: CONFIG.port,
            path,
            method,
            headers: {
                'Authorization': creds.auth,
                'Content-Type': 'application/xml; charset=utf-8',
                'User-Agent': 'OpenClaw-iCloud/1.0',
                ...headers
            }
        };

        if (body) {
            options.headers['Content-Length'] = Buffer.byteLength(body);
        }

        const req = https.request(options, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                resolve({
                    statusCode: res.statusCode,
                    data,
                    success: res.statusCode >= 200 && res.statusCode < 400
                });
            });
        });

        req.on('error', reject);
        if (body) req.write(body);
        req.end();
    });
}

async function listEvents(from, to) {
    console.log(`📅 Listing events from ${from} to ${to}\n`);
    
    // REPORT query to list events in date range
    const query = `<?xml version="1.0" encoding="utf-8" ?>
        <C:calendar-query xmlns:D="DAV:" xmlns:C="urn:ietf:params:xml:ns:caldav">
            <D:prop>
                <D:getetag/>
                <C:calendar-data/>
            </D:prop>
            <C:filter>
                <C:comp-filter name="VCALENDAR">
                    <C:comp-filter name="VEVENT">
                        <C:time-range start="${from}" end="${to}"/>
                    </C:comp-filter>
                </C:comp-filter>
            </C:filter>
        </C:calendar-query>`;

    try {
        const result = await makeRequest('REPORT', '/', query, {
            'Depth': '1'
        });

        if (result.success) {
            console.log('✓ Events retrieved');
            // Parse iCalendar data (simplified)
            const events = parseCalendarData(result.data);
            console.log(`Found ${events.length} events`);
        } else {
            console.error('✗ Failed to list events:', result.statusCode);
        }
    } catch (error) {
        console.error('✗ Error:', error.message);
    }
}

async function createEvent(summary, start, end, location = '', description = '') {
    console.log(`📅 Creating event: ${summary}\n`);
    
    const uid = Date.now() + '@openclaw.local';
    const now = new Date().toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';
    
    // iCalendar format
    const ical = `BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//OpenClaw//iCloud Skill//EN
BEGIN:VEVENT
UID:${uid}
DTSTAMP:${now}
DTSTART:${start.replace(/[-:]/g, '').split('.')[0]}Z
DTEND:${end.replace(/[-:]/g, '').split('.')[0]}Z
SUMMARY:${summary}
${location ? `LOCATION:${location}` : ''}
${description ? `DESCRIPTION:${description}` : ''}
END:VEVENT
END:VCALENDAR`;

    try {
        const result = await makeRequest('PUT', `/${uid}.ics`, ical, {
            'Content-Type': 'text/calendar; charset=utf-8'
        });

        if (result.success) {
            console.log('✓ Event created successfully');
            console.log(`Event ID: ${uid}`);
        } else {
            console.error('✗ Failed to create event:', result.statusCode);
        }
    } catch (error) {
        console.error('✗ Error:', error.message);
    }
}

function parseCalendarData(xmlData) {
    // Simplified parser - extract event summaries
    const events = [];
    const summaryRegex = /SUMMARY:([^\n]+)/g;
    let match;
    
    while ((match = summaryRegex.exec(xmlData)) !== null) {
        events.push({ summary: match[1].trim() });
    }
    
    return events;
}

// CLI
const args = process.argv.slice(2);
const command = args[0];

if (command === 'list') {
    const fromIdx = args.indexOf('--from');
    const toIdx = args.indexOf('--to');
    const from = fromIdx >= 0 ? args[fromIdx + 1] : new Date().toISOString().split('T')[0];
    const to = toIdx >= 0 ? args[toIdx + 1] : new Date(Date.now() + 7*24*60*60*1000).toISOString().split('T')[0];
    listEvents(from, to);
    
} else if (command === 'create') {
    const summaryIdx = args.indexOf('--summary');
    const startIdx = args.indexOf('--start');
    const endIdx = args.indexOf('--end');
    const locationIdx = args.indexOf('--location');
    const descIdx = args.indexOf('--description');
    
    const summary = summaryIdx >= 0 ? args[summaryIdx + 1] : 'New Event';
    const start = startIdx >= 0 ? args[startIdx + 1] : new Date().toISOString();
    const end = endIdx >= 0 ? args[endIdx + 1] : new Date(Date.now() + 3600000).toISOString();
    const location = locationIdx >= 0 ? args[locationIdx + 1] : '';
    const description = descIdx >= 0 ? args[descIdx + 1] : '';
    
    createEvent(summary, start, end, location, description);
    
} else {
    console.log('Usage:');
    console.log('  calendar.js list [--from YYYY-MM-DD] [--to YYYY-MM-DD]');
    console.log('  calendar.js create --summary "Title" --start "YYYY-MM-DDTHH:MM:SS" --end "YYYY-MM-DDTHH:MM:SS" [--location "Place"] [--description "Details"]');
}
