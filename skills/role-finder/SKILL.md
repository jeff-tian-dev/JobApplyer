---
name: role-finder
description: Find new internship postings that match my targets and add them to my agent workbook (Discovery, then Agent Queue). Use when I ask to find roles, run the daily role search, or refresh the queue.
---

# Role finder

Finds new internship postings every day from the SimplifyJobs GitHub list, LinkedIn, Indeed, Handshake and Intern Insider, logs them in the Discovery tab of my agent workbook, and queues the ones that fit for my applying agent. Never applies to anything.

## Inputs
- My agent workbook (`workbook/agent-workbook.xlsx`, or the Google Sheet copy of it). Read the **Agent Guide** tab first, especially Allowed locations, Role types, Skip and Apply-myself list.
- `targets.json` next to this file. If it doesn't exist yet, create it from the Agent Guide using `targets.example.json` as the shape, and show it to me before the first run.

## Steps
1. **Pull the GitHub list.** Run:
   `python scripts/find_roles.py --config targets.json --tracker <agent-workbook.xlsx, or a CSV export of its Discovery tab> --out new_roles.csv`
   It reads the SimplifyJobs internship list (updated daily), keeps active postings from the last `posted_within_days` days that match my categories, terms, keywords and locations, and drops anything whose link is already in Discovery, Agent Queue or Applications.
2. **Check my other sources.** Do both of these that you can:

   **a. Job-alert emails (works everywhere, no browser needed).** If you have the Gmail connector on my application inbox, search it for alert emails from the last 2 days and pull each role's title, company, location and link:
   - LinkedIn: `from:jobalerts-noreply@linkedin.com` (or `from:linkedin.com subject:job`)
   - Indeed: `from:indeed.com subject:(jobs OR job)`
   - Handshake: `from:joinhandshake.com`
   - Intern Insider: search `"Intern Insider"` for its emails (check the sender the first time and use it from then on)
   Use the job's own link, not a tracking redirect, when you can see it. If there are no alert emails, tell me to turn on daily job alerts on each site, sent to my application Gmail.

   **b. The sites themselves (only with browser access to my signed-in browser, like Claude in Chrome).** Read the pages the way I would, a few pages per site, no bulk scraping, and follow each site's terms. Search each of my role types:
   - **LinkedIn:** `https://www.linkedin.com/jobs/search/?keywords=<role type>&f_E=1&f_TPR=r86400&sortBy=DD` (f_E=1 = internship, f_TPR=r86400 = past 24 hours, sortBy=DD = newest). Open each result for the real apply link; skip "Easy Apply"-only roles if my Agent Guide says to.
   - **Indeed:** `https://www.indeed.com/jobs?q=<role type>+intern&fromage=1&sort=date` (fromage=1 = last day).
   - **Handshake:** sign in through my school, go to Jobs, filter Job type = Internship, sort by Newest, and search each role type.
   - **Intern Insider:** open it signed in, look at the newest postings and anything matching my role types.
   Without browser access, skip 2b and say so; the alert emails in 2a cover most of it.
3. **Log leads.** Append every new role to **Discovery** with Discovery state `new`. If my workbook is a Google Sheet and you have the Sheets connector, write there; otherwise edit the .xlsx. Append only; never delete, insert or sort rows.
4. **Queue the good ones.** For each lead, check the Agent Guide rules: allowed location, role type, skip list, degree requirements, and no existing row in Applications for the same employer + requisition. If it passes, append it to **Agent Queue** with Job key `employer:<name>|req:<requisition or url>`, State `queued`, and set its Discovery state to `queued`. Companies on the Apply-myself list get Next action `HUMAN: apply myself` instead of `queued`. Unclear locations stay in Discovery as `unclear location`. Add one Agent Activity row per queued role (Agent `claude`, Action `queued`).
5. **Report.** One short summary: how many roles were added, from where, and the top 5 worth my attention.

## Rules
- Never invent a posting, a link or a deadline. Every row needs a real link.
- Don't apply, message recruiters or sign up for anything.
- If the GitHub list can't be reached, say so and stop rather than guessing.

## Running it daily
Schedule this skill to run once a day with whatever scheduler your Claude app offers (for example a scheduled task in Claude Code or Cowork) with the prompt: "Run the role-finder skill."
