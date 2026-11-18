# Setup prompt

Paste everything below the line into Claude (claude.ai, the Claude desktop app, or Claude Code). Attach `workbook/agent-workbook.xlsx`, the `candidate-kit` folder (or `dist/candidate-kit.zip`) and your master resume.

---

I want to set up an internship application system where several AI agents share one workbook. Help me set it up end to end. I've attached the agent workbook, my private candidate kit and my master resume.

How the system works:
1. **Agent workbook** (shared): the operating structure every agent works through. The Agent Guide tab is the rulebook. Discovery holds leads, Agent Queue holds roles approved to apply and who owns each one, Agent Activity is an append-only log, Applications and Events record real results, and Blocked shows what needs me.
2. **Candidate kit** (private): START_HERE, profile.json, COMMON_ANSWERS, PROJECT_FACTS, RESUME_GUIDE, TRACKING and my resumes. Only my applying agent gets it. It never goes in the shared workbook.
3. **Role finder**: a Claude skill that runs daily, pulls new postings from the SimplifyJobs internship list on GitHub (and my other sources if it has browser access), logs them in Discovery and queues the ones that fit.
4. **Applier**: Grok Bot (xAI's agent, working on its own cloud computer) runs the grok-applier skill: it claims queued roles one at a time, applies with the right resume, and records the result or the exact blocker. MausBot (free and open source, running on an AI subscription I connect to it) can stand in as a backup applier (agent `maus`, mausbot-applier skill) when Grok Bot's weekly credits run out; only one applier runs at a time.
5. **Application inbox**: a separate Gmail used only for applications, so accounts, verification codes and replies all land in one place.
6. **Inbox listener**: a Claude skill, run daily, that reads that inbox, adds rows to Events, updates Applications, and tells me what needs me.

Do this in order:

**Step 1. Interview me.** Ask questions in rounds of at most 6, grouped by topic: (a) contact, school and work eligibility, (b) roles I want, locations, companies to skip, and my apply-myself list, (c) start dates and pace, (d) my reusable answers, (e) my projects and what I can truthfully claim about each, my resume variants, (f) my computer and accounts (Windows or Mac, which Claude app, whether I have Claude Code, Google account, an X subscription that includes Grok Bot (Premium or higher) and the Grok Bot app, Handshake, Intern Insider, LinkedIn). Pull what you can from my resume first so you only ask what's missing. Self-identification questions are optional; accept "skip". Never fill in an answer I didn't give you.

**Step 2. Fill both.** Fill every file in the candidate kit: profile.json (put anything I haven't decided in `unknowns`), COMMON_ANSWERS.md, PROJECT_FACTS.md (only claims from my resume or that I confirm, with a Don't say line for each project), RESUME_GUIDE.md and TRACKING.md. Fill the bracketed rows of the Agent Guide (Owner, Agents, Allowed locations, Role types, Skip, Apply-myself list, Pace). Have me approve or edit every answer and project fact. Give me the finished kit as a zip and the workbook, and list anything left blank.

**Step 3. Collect my resumes.** Ask me for my finished resume PDFs, one per role type I want; I make these myself. Don't edit them. Check every claim in each one against PROJECT_FACTS.md and list any that aren't there, so I can confirm them (and you add them to PROJECT_FACTS.md) or fix the resume. Put the PDFs in the kit's `resumes/` folder, then fill RESUME_GUIDE.md: which file goes with which role type, the words in a posting that point to each one, a tie-break rule and a default.

**Step 4. Write my setup plan.** A numbered checklist specific to my computer and accounts, with every click or command spelled out:
- create the separate application Gmail and add it to my Profile
- make one job-portal-only password of at least 16 characters (some portals need 14 to 16+), and give it to Grok Bot only through its secure login form (Save to vault) or by taking over its screen. Never reuse another password, never paste it into the Grok Bot chat, and never write it in the workbook, the kit or the Bot's `/workspace`
- connect the application Gmail, Google Drive and Google Sheets (with edit access) to Grok Bot using `guides/grok-bot-setup.md`
- delete the EXAMPLE rows, then upload the agent workbook to Google Sheets (File > Import, or open the .xlsx in Drive and Save as Google Sheets), check the Blocked tab's formula works, and connect Claude to Google Sheets and Gmail
- keep the candidate kit private: attach it in a direct chat with my Grok Bot and have it saved under `/workspace/candidate-kit/` (or a private Drive folder in the application account), never anywhere public
- install the role-finder skill from `dist/role-finder.zip` (source in `skills/role-finder`), create `targets.json` from the Agent Guide, do one test run with me, and schedule it daily
- sign up for Intern Insider, Handshake, Indeed and LinkedIn, and turn on daily internship job alerts on each one, sent to the application Gmail, so the role finder can read them even without browser access
- set up Grok Bot: create a Bot named `grok`, install the grok-applier skill by attaching `dist/grok-applier.zip` in a direct chat, paste the Bot description from `skills/grok-applier/SKILL.md`, give it the workbook link, do the TEST: claim, supervise the first few real applications, and only then (optionally) have it create a daily routine
- optional, if I use Intern Insider: install the intern-insider-scan skill in Grok Bot from `dist/intern-insider-scan.zip`, have me sign in to Intern Insider in the Bot's browser with the application Gmail, and have me set my filters on Intern Insider (sorted by most recent) and paste that search link into TRACKING.md; then run the scan once with me before the applier
- install the inbox-listener skill from `dist/inbox-listener.zip`, connect it to the application Gmail, run it once with me, and schedule it daily
- optional, only if I want a backup applier: set up MausBot with the mausbot-applier skill from `dist/mausbot-applier.zip`, paste the Bot instructions from `skills/mausbot-applier/SKILL.md`, connect its Gmail and Google Sheets apps to the application account, save my portal login in its Logins settings, and do its own TEST: claim as `maus`
- my daily routine: check the Blocked tab, do assessments and interviews, and spot-check a few submitted applications

**Step 5. Integrate.** Walk me through the plan one step at a time. After each step, ask me to confirm it worked or paste the error before moving on. Run the first role-finder pass and the first inbox check with me, and watch Grok Bot's test claim land in Agent Activity.

Rules: be honest when you can't do something from where you're running (for example, you can't click around my computer from claude.ai) and tell me exactly what to do instead. Never put passwords or verification codes in the workbook.
