<p align="center">
  <a href="#quick-start"><b>Quick start</b></a> ·
  <a href="SETUP_PROMPT.md"><b>Setup prompt</b></a> ·
  <a href="docs/GETTING_STARTED.md"><b>Checklist</b></a> ·
  <a href="dist"><b>Skill downloads</b></a>
</p>

# Internship Applyer (Claude + Grok Bot)

A template for running an internship search with AI agents. Claude skills find roles, build tailored resumes and track your inbox. A Grok Bot skill fills in and submits applications. You review what goes out, unblock what the agents can't finish, and handle assessments and interviews yourself.

This is a fork of [Oliver Browne](https://www.linkedin.com/in/olibrowne/)'s Internship Applyer, which used Meta's Muse for applying. Here the applying step has been rewritten for Grok Bot. Everything in the repo is a template: your personal details go in a private `my-setup/` copy that git ignores.

## How it works

```
 Role finder (Claude)                 Resume builder (Claude)
 SimplifyJobs GitHub list,            one resume per role type,
 plus job-alert emails                checked against what you've done
                                                 |
          |                                      v
          v                              Candidate kit (private)
   Agent workbook  <---- claims ----  Grok Bot (applies, one role at a time)
   (Google Sheet)                                |
          ^                                      v
          |                            Application Gmail (codes, replies)
          +---- status updates ---- Inbox listener (Claude)
                                                 |
                                                 v
                                  You: Blocked tab, assessments, interviews
```

1. **Role finder** runs a Python script over the SimplifyJobs internship list and, if Claude can reach your application Gmail, reads job-alert emails from LinkedIn, Indeed, Handshake and Intern Insider. With browser access to your signed-in browser it can also check those sites directly. It logs new roles in the workbook's Discovery tab and queues the ones that match your targets.
2. **Resume builder** turns your master resume into up to 8 one-page resumes, one per role type, and shows them to you for approval before they're used.
3. **Grok Bot** runs the grok-applier skill: it reads the workbook's Agent Guide, claims a queued role, applies with the matching resume, and records the result or the reason it got blocked.
4. **A separate Gmail** used only for applications receives portal accounts, verification codes and replies.
5. **Inbox listener** reads that Gmail and writes confirmations, assessments, interviews and rejections back to the workbook.
6. **You** approve submissions (at least for the first few), work through the Blocked tab, take assessments and interviews, and spot-check what was sent.

The role finder and inbox listener run when you ask, or daily if you schedule them in Claude Code or Cowork. Grok Bot can run on a schedule as a routine.

## What's in here

| Path | What it is |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Directions Claude reads when you open this folder in Claude Code. It doesn't start anything on its own; ask it to set you up and it follows `SETUP_PROMPT.md`. |
| [`SETUP_PROMPT.md`](SETUP_PROMPT.md) | Paste into Claude. It interviews you, fills in your kit and workbook, builds your resumes, and walks you through the rest of the setup. **Start here.** |
| [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md) | The same setup as a plain checklist, if you'd rather do it by hand. |
| [`workbook/agent-workbook.xlsx`](workbook/agent-workbook.xlsx) | The shared workbook every agent works through: Agent Guide (the rulebook), Discovery, Agent Queue, Agent Activity, Applications, Events, Blocked. Comes with EXAMPLE rows; delete them before you start. |
| [`candidate-kit/`](candidate-kit) | Templates for your private side: standing instructions, profile, common answers, project facts (what you can truthfully claim), resume guide. Only your applying agent gets the filled-in copy. |
| [`skills/role-finder/`](skills/role-finder) | Claude skill plus a Python script that reads the SimplifyJobs list and skips roles already in your workbook. |
| [`skills/resume-builder/`](skills/resume-builder) | Claude skill that builds role-specific resumes in a plain, ATS-friendly format (or your own template). |
| [`skills/inbox-listener/`](skills/inbox-listener) | Claude skill that updates the workbook from your application inbox. It never replies to or deletes email. |
| [`skills/grok-applier/`](skills/grok-applier) | Grok Bot skill that claims queued roles, applies and records results, plus the Bot description to paste in. |
| [`guides/grok-bot-setup.md`](guides/grok-bot-setup.md) | Setting up Grok Bot: connecting your application Gmail and Google Sheets, giving it your kit, and handling portal passwords. |
| [`dist/`](dist) | Ready-to-upload zips of each skill and the candidate kit. |

## Quick start

**With Claude Code:** clone or download this repo, open the folder in Claude Code, and say "set me up". Claude follows [`SETUP_PROMPT.md`](SETUP_PROMPT.md) and starts by asking for your master resume.

**With claude.ai or the Claude desktop app:**

1. Click **Code > Download ZIP** and unzip it.
2. Open Claude. Attach `workbook/agent-workbook.xlsx`, `dist/candidate-kit.zip` and your master resume (everything you've ever done, any length).
3. Paste in everything below the line in [`SETUP_PROMPT.md`](SETUP_PROMPT.md).
4. Answer Claude's questions. It fills your kit and workbook, builds your resumes, and gives you a step-by-step plan.
5. Follow the plan. Some steps (subscribing to Grok Bot, connecting accounts, saving passwords) you do yourself; Claude tells you which.

## What you'll need

- A Claude account with skills. For scheduled runs, use Claude Code or Cowork, because the role finder runs a small Python 3 script. On claude.ai you can run everything by hand, and the role finder relies on job-alert emails instead of the script.
- [Grok Bot](https://x.ai/bot), xAI's agent, for applying. It needs an X subscription that includes it (Premium or higher at the time of writing). Connect its **Gmail**, **Google Drive** and **Google Sheets** plugins to your application Google account (see [`guides/grok-bot-setup.md`](guides/grok-bot-setup.md)).
- A new Gmail just for applications, and the workbook imported into Google Sheets in that account. The Blocked tab's formula is made for Sheets.
- Daily job alerts turned on (sent to your application Gmail) on the boards you use: LinkedIn, Indeed, Handshake, Intern Insider.

## What it costs

Roughly **$50 a month** at October 2026 list prices. Check current pricing before you subscribe.

| Piece | Cost |
|---|---|
| Claude Pro (includes Claude Code, skills, connectors and scheduled tasks) | $20/month, or $17/month billed yearly |
| X Premium (includes Grok Bot) | About $30/month (US list price; check x.ai for yours). Grok Bot has a weekly usage allowance, and long browser sessions use it fastest |
| Gmail, Google Sheets | Free |
| Job boards | Free accounts |
| This kit | Free (MIT license) |

## Getting Grok Bot

1. Subscribe to an X plan that includes Grok Bot.
2. Install the Grok Bot app and sign in.
3. Create a Bot named `grok` and work with it in a direct chat.
4. Follow [`guides/grok-bot-setup.md`](guides/grok-bot-setup.md) to connect your application Gmail and Google Sheets, give it your kit, and install the grok-applier skill.

Grok Bot is in beta, so menus, limits and pricing change. If something in the guide doesn't match what you see, ask your Bot what it can do now.

## Rules the agents are told to follow

These are written into every skill and the workbook's Agent Guide. They're instructions, not guarantees: AI agents can still get things wrong, so check their work, especially at the start.

- **Nothing made up.** Every resume line and form answer should trace back to your master resume, your project facts or your own answers. If something's missing, the agent marks the role blocked and asks you.
- **No double applications.** Agents claim a role before touching it, and nothing marked submitted or uncertain is retried.
- **Submitted means confirmed.** Only a confirmation page or receipt email counts.
- **No secrets in files.** Passwords and verification codes never go in the workbook, the kit or the Bot's files. Grok Bot gets your portal password only through its secure login form.
- **You stay in charge.** Read what goes out in your name, and apply to the companies you care most about yourself.

## Notes

Not affiliated with Anthropic, xAI, Meta, Simplify, Intern Insider, LinkedIn, Indeed or Handshake. Automated applying may be against some sites' terms; check before you point an agent at them. Found something that breaks? Open an issue.

Maintained by [Jeff Tian](https://github.com/jeff-tian-dev). Based on [Oliver Browne](https://www.linkedin.com/in/olibrowne/)'s Internship Applyer (MIT license).
