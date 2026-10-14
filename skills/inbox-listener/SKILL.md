---
name: inbox-listener
description: Read my application Gmail, record what happened (confirmations, assessments, interviews, rejections) in my agent workbook, and tell me what needs me. Use when I ask to check my application inbox or run the daily inbox check.
---

# Inbox listener

Reads the Gmail I use only for applications and keeps my agent workbook up to date. Never replies to, deletes, or archives email, and never applies to anything.

## Needs
- The Gmail connector, signed in to my application inbox.
- My agent workbook (Google Sheet with the Sheets connector, or the .xlsx). Read the **Agent Guide** tab first.

## Steps
1. **Find new mail.** Search the application inbox for messages since the last Events row (or the last 2 days on the first run). Skip newsletters, job alerts and marketing.
2. **Classify each message:** confirmation, assessment, interview invite, rejection, offer, or other (for example, a recruiter question). Verification codes are not events; ignore them.
3. **Match it to a role.** Match on employer name and role title, or requisition number, against Applications and Agent Queue. If nothing matches, still log it with Role = `unmatched`.
4. **Record it.**
   - Append a row to **Events**: Event at (the email's date, UTC), Employer, Role, Event type, Source = `email: <subject>`, a one-line Summary, and Recruitment status.
   - Update the matching **Applications** row: Recruitment status, Last event at, Next action (for example "Take HackerRank by Oct 20").
   - If a confirmation arrives for an Agent Queue row still marked `submitting` or `uncertain`, add an Agent Activity row noting the confirmation; leave the state change to the agent that owns it unless the Agent Guide says otherwise.
5. **Report to me.** A short summary: deadlines in the next 7 days first, then interview invites, then anything a human has to answer, then a count of rejections. Include the email subject so I can find each one.

## Rules
- Never put verification codes, passwords or links that log me in into the workbook or the summary.
- Never reply to, forward, delete, label or archive email unless I ask.
- If you're not sure what an email means, log it as `other` and tell me.

## Running it daily
Schedule it once or twice a day with your Claude app's scheduled tasks, using the prompt: "Run the inbox-listener skill."
