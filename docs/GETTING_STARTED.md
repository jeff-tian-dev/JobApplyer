# Getting started (by hand)

The setup prompt does all of this with you. This is the same thing as a checklist.

## 1. Accounts (about 20 minutes)
- [ ] Make a new Gmail used only for applications.
- [ ] Make one password used only for job-portal signups, at least 16 characters (some portals need 14 to 16+). Don't reuse it anywhere else.
- [ ] Sign up for Intern Insider, Handshake (through your school), Indeed and LinkedIn. Turn on daily internship job alerts on each, sent to the application Gmail.
- [ ] Get Grok Bot (X Premium or higher, plus the Grok Bot app) and connect the application Gmail, Google Drive and Google Sheets (edit access): see [`guides/grok-bot-setup.md`](../guides/grok-bot-setup.md).

## 2. Your candidate kit
- [ ] Fill in `candidate-kit/profile.json`, `COMMON_ANSWERS.md` and `PROJECT_FACTS.md`. Put anything you haven't decided in `unknowns`.
- [ ] Write or collect your master resume: everything you've done, any length.
- [ ] Build your resumes with the resume-builder skill (`dist/resume-builder.zip`), approve each one, and drop the PDFs in `candidate-kit/resumes/`.
- [ ] Fill in the table in `RESUME_GUIDE.md`.

## 3. The workbook
- [ ] Delete the EXAMPLE rows.
- [ ] Fill in the bracketed rows of the Agent Guide tab: owner, agents, allowed locations, role types, skip list, apply-myself list, pace.
- [ ] Upload it to Google Drive and open it as a Google Sheet. Check that the Blocked tab shows "Nothing blocked".
- [ ] Put the Sheet's link in `candidate-kit/TRACKING.md`.

## 4. Claude
- [ ] Connect Claude to Gmail (your application inbox) and Google Sheets.
- [ ] Install the role-finder and inbox-listener skills from `dist/`.
- [ ] Copy `targets.example.json` to `targets.json` and edit it to match your Agent Guide.
- [ ] Run "Run the role-finder skill" once and check the new rows in Discovery and Agent Queue.
- [ ] Schedule the role finder daily and the inbox listener once or twice a day.

## 5. Grok Bot
- [ ] Create a Bot named `grok` and use it in a direct chat (group chats hide its approval and password requests).
- [ ] Attach `dist/grok-applier.zip` and say "Unzip this and save it as a skill."
- [ ] Paste the Bot description from `skills/grok-applier/SKILL.md` into the Bot's Description.
- [ ] Attach your candidate kit and resumes and have it save them under `/workspace/candidate-kit/`, then list them back.
- [ ] Have it ask for your job-portal password with a login form, and choose Save to vault. Never paste the password into the chat.
- [ ] Give it the workbook link and tell it: "Read the Agent Guide tab first, then do the TEST: claim it describes. Don't open any employer form until I confirm."
- [ ] Check the test claim in Agent Activity (Agent `grok`), then tell it to start on queued roles. Approve the first few submits yourself.
- [ ] Optional: once that's going well, ask it to create a daily routine that runs the grok-applier skill.

## Every day (about 15 minutes)
- [ ] Check the Blocked tab and clear what you can.
- [ ] Read the inbox listener's summary: deadlines first.
- [ ] Spot-check a couple of submitted applications.
- [ ] Do your assessments and interviews.
