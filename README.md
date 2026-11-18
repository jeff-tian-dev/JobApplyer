<p align="center">
  <a href="#quick-start"><b>Quick start</b></a> ·
  <a href="SETUP_PROMPT.md"><b>Setup prompt</b></a> ·
  <a href="docs/GETTING_STARTED.md"><b>Checklist</b></a> ·
  <a href="dist"><b>Skill downloads</b></a>
</p>

# Internship Applyer (Claude + Grok Bot)

A template for running an internship search with AI agents that share one Google Sheet:

- **Claude** finds new internship postings and watches your application inbox.
- **Grok Bot** applies to the roles that fit, one at a time, using your resumes and pre-approved answers.
- **MausBot** (optional, free and open source) is a backup applier that runs on your own AI subscription, used only when Grok Bot's weekly credits run out.

You stay in the loop. You make the resumes, approve the answers the agents can use, clear anything they get stuck on, and do the assessments and interviews yourself.

Everything in the repo is a blank template. Your personal details go in a private `my-setup/` folder that git ignores, so nothing about you gets committed.

## How it works

```
 Role finder (Claude)                    Your resumes + candidate kit
 SimplifyJobs list + job-alert emails    (private: facts, answers, PDFs)
 Intern Insider scan (Grok Bot)
          |                                          |
          v                                          v
   Agent workbook  <------ claims a role ------  Applier
   (Google Sheet)  ------- records result ---->  Grok Bot (main)
          ^                                      MausBot (backup)
          |                                          |
          |                                          v
          +--- status updates ---  Inbox listener <-- Application Gmail
                                   (Claude)          (codes, receipts, replies)
                                          |
                                          v
                       You: Blocked tab, assessments, interviews
```

1. **Role finder** (Claude skill) runs a Python script over the [SimplifyJobs](https://github.com/SimplifyJobs) internship list and, if Claude can reach your application Gmail, reads job-alert emails from LinkedIn, Indeed, Handshake and Intern Insider. It logs new roles in the workbook's Discovery tab and queues the ones that match your locations, role types and skip list.
2. **Your candidate kit** holds your profile, reusable answers, the project facts you can truthfully claim, and one resume PDF per role type, with a guide saying which resume goes with which kind of posting. Only the applier gets it.
3. **Intern Insider scan** (optional Grok Bot skill) opens your saved Intern Insider search right before an applying run, checks every internship posted in the last 2 days against your Agent Guide, and queues the new ones. It needs your Intern Insider login saved in Grok Bot's browser and the link to your search, with your filters set, in the kit.
4. **Grok Bot** runs the grok-applier skill. It reads the workbook's Agent Guide, claims a queued role, picks the best-matching resume, fills in and submits the application, and records the result, or exactly why it got stuck.
5. **MausBot** (optional) runs the mausbot-applier skill with the same rules, as agent `maus`. It's free and open source and connects to an AI subscription you already have. Only one applier works the queue at a time: switch to MausBot when Grok Bot's credits run out, and back when they reset.
6. **A separate Gmail** used only for applications receives portal accounts, verification codes, receipts and replies.
7. **Inbox listener** (Claude skill) reads that Gmail and writes confirmations, assessments, interviews and rejections back to the workbook. It never replies to or deletes email.
8. **You** approve the first few submissions, work through the Blocked tab, take assessments and interviews, and spot-check what was sent.

The role finder and inbox listener run when you ask, or daily if you schedule them in Claude Code or Cowork. Grok Bot can run on a schedule as a routine once you trust it.

## What's in here

| Path | What it is |
|---|---|
| [`SETUP_PROMPT.md`](SETUP_PROMPT.md) | Paste into Claude. It interviews you, fills in your kit and workbook, checks your resumes against your project facts, and walks you through the rest of the setup. **Start here.** |
| [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md) | The same setup as a plain checklist, if you'd rather do it by hand. |
| [`CLAUDE.md`](CLAUDE.md) | Directions Claude reads when you open this folder in Claude Code. It doesn't start anything on its own; ask it to set you up and it follows `SETUP_PROMPT.md`. |
| [`workbook/agent-workbook.xlsx`](workbook/agent-workbook.xlsx) | The shared workbook every agent works through: Agent Guide (the rulebook), Discovery, Agent Queue, Agent Activity, Applications, Events, Blocked. Comes with EXAMPLE rows; delete them before you start. |
| [`candidate-kit/`](candidate-kit) | Templates for your private kit: standing instructions, profile, common answers, project facts, resume guide, tracking. |
| [`skills/role-finder/`](skills/role-finder) | Claude skill plus a Python script that reads the SimplifyJobs list and skips roles already in your workbook. |
| [`skills/inbox-listener/`](skills/inbox-listener) | Claude skill that updates the workbook from your application inbox. |
| [`skills/grok-applier/`](skills/grok-applier) | The main applier: Grok Bot skill plus the Bot description to paste in. |
| [`skills/intern-insider-scan/`](skills/intern-insider-scan) | Optional Grok Bot skill: scans your saved Intern Insider search and queues new roles before each applying run. |
| [`skills/mausbot-applier/`](skills/mausbot-applier) | The backup applier: MausBot skill, its Bot instructions, and how to switch between the two. |
| [`guides/grok-bot-setup.md`](guides/grok-bot-setup.md) | Setting up Grok Bot: connecting your application Gmail and Google Sheets, giving it your kit, and handling portal passwords. |
| [`dist/`](dist) | Ready-to-upload zips of each skill and the candidate kit. |

## Quick start

**With Claude Code:** clone this repo, open the folder in Claude Code, and say "set me up". Claude follows [`SETUP_PROMPT.md`](SETUP_PROMPT.md) and starts by asking for your master resume.

**With claude.ai or the Claude desktop app:**

1. Click **Code > Download ZIP** and unzip it.
2. Open Claude. Attach `workbook/agent-workbook.xlsx`, `dist/candidate-kit.zip` and your master resume (everything you've ever done, any length).
3. Paste in everything below the line in [`SETUP_PROMPT.md`](SETUP_PROMPT.md).
4. Answer Claude's questions and give it your resumes (one PDF per role type, made by you). It fills your kit and workbook and gives you a step-by-step plan.
5. Follow the plan. Some steps (subscribing to Grok Bot, connecting accounts, saving passwords) you do yourself; Claude tells you which.

## What you'll need

- A Claude account with skills. For scheduled runs, use Claude Code or Cowork, because the role finder runs a small Python 3 script. On claude.ai you can run everything by hand, and the role finder relies on job-alert emails instead of the script.
- [Grok Bot](https://x.ai/bot), xAI's agent, for applying. It needs an X subscription that includes it (Premium or higher at the time of writing). Connect its **Gmail**, **Google Drive** and **Google Sheets** plugins to your application Google account (see [`guides/grok-bot-setup.md`](guides/grok-bot-setup.md)).
- Optional: MausBot as a backup applier for when Grok Bot's credits run out. It's free and open source, connects to your own AI subscription, and needs its Gmail and Google Sheets apps connected to the same application account.
- A new Gmail just for applications, and the workbook imported into Google Sheets in that account. The Blocked tab's formula is made for Sheets.
- Daily job alerts turned on (sent to your application Gmail) on the boards you use: LinkedIn, Indeed, Handshake, Intern Insider.

## What it costs

Roughly **$50 a month** at October 2026 list prices. Check current pricing before you subscribe.

| Piece | Cost |
|---|---|
| Claude Pro (includes Claude Code, skills, connectors and scheduled tasks) | $20/month, or $17/month billed yearly |
| X Premium (includes Grok Bot) | About $30/month (US list price; check x.ai for yours). Grok Bot has a weekly usage allowance, and long browser sessions use it fastest |
| MausBot (optional backup) | Free and open source. It runs on an AI subscription you connect, so its usage counts against that plan |
| Gmail, Google Sheets | Free |
| Job boards | Free accounts |
| This kit | Free (MIT license) |

## Rules the agents are told to follow

These are written into every skill and the workbook's Agent Guide. They're instructions, not guarantees: AI agents can still get things wrong, so check their work, especially at the start.

- **Nothing made up.** Every form answer should trace back to your master resume, your project facts or your own answers. If something's missing, the agent stops and asks you.
- **No double applications.** Agents claim a role before touching it, never edit a row another agent owns, and never retry anything marked submitted or uncertain.
- **Submitted means confirmed.** Only a confirmation page or receipt email counts.
- **No secrets in files.** Passwords and verification codes never go in the workbook, the kit or the agents' files. Portal passwords go only through each bot's own secure login feature.
- **You stay in charge.** Read what goes out in your name, and apply to the companies you care most about yourself (put them on the Apply-myself list and the agents skip them).

## Notes

Not affiliated with Anthropic, xAI, Meta, Simplify, Intern Insider, LinkedIn, Indeed or Handshake. Automated applying may be against some sites' terms; check before you point an agent at them. Found something that breaks? Open an issue.

Maintained by [Jeff Tian](https://github.com/jeff-tian-dev). Based on [Oliver Browne](https://www.linkedin.com/in/olibrowne/)'s Internship Applyer (MIT license), which used Meta's Muse for applying.
