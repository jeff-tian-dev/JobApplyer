# Setup prompt

Paste everything below the line into Claude (claude.ai, the Claude desktop app, or Claude Code). Attach `workbook/agent-workbook.xlsx`, the `candidate-kit` folder (or `dist/candidate-kit.zip`) and your master resume.

---

I want to set up an internship application system where several AI agents share one workbook. Help me set it up end to end. I've attached the agent workbook, my private candidate kit and my master resume.

How the system works:
1. **Agent workbook** (shared): the operating structure every agent works through. The Agent Guide tab is the rulebook. Discovery holds leads, Agent Queue holds roles approved to apply and who owns each one, Agent Activity is an append-only log, Applications and Events record real results, and Blocked shows what needs me.
2. **Candidate kit** (private): START_HERE, profile.json, COMMON_ANSWERS, PROJECT_FACTS, RESUME_GUIDE, TRACKING and my resumes. Only my applying agent gets it. It never goes in the shared workbook.
3. **Role finder**: a Claude skill that runs daily, pulls new postings from the SimplifyJobs internship list on GitHub (and my other sources if it has browser access), logs them in Discovery and queues the ones that fit.
4. **Applier**: Muse (Meta's AI agent) claims queued roles one at a time, applies with the right resume, and records the result or the exact blocker.
5. **Application inbox**: a separate Gmail used only for applications, so accounts, verification codes and replies all land in one place.
6. **Inbox listener**: a Claude skill, run daily, that reads that inbox, adds rows to Events, updates Applications, and tells me what needs me.

Do this in order:

**Step 1. Interview me.** Ask questions in rounds of at most 6, grouped by topic: (a) contact, school and work eligibility, (b) roles I want, locations, companies to skip, and my apply-myself list, (c) start dates and pace, (d) my reusable answers, (e) my projects and what I can truthfully claim about each, my resume variants, (f) my computer and accounts (Windows or Mac, which Claude app, whether I have Claude Code, Google account, Muse, Handshake, Intern Insider, LinkedIn). Pull what you can from my resume first so you only ask what's missing. Self-identification questions are optional; accept "skip". Never fill in an answer I didn't give you.

**Step 2. Fill both.** Fill every file in the candidate kit: profile.json (put anything I haven't decided in `unknowns`), COMMON_ANSWERS.md, PROJECT_FACTS.md (only claims from my resume or that I confirm, with a Don't say line for each project), RESUME_GUIDE.md and TRACKING.md. Fill the bracketed rows of the Agent Guide (Owner, Agents, Allowed locations, Role types, Skip, Apply-myself list, Pace). Have me approve or edit every answer and project fact. Give me the finished kit as a zip and the workbook, and list anything left blank.

**Step 3. Build my resumes.** Install the resume-builder skill from `dist/resume-builder.zip` (or follow its SKILL.md directly if you can't install skills here). Use it to build up to 8 one-page resumes from my master in its default format (or my own template if I give you one), one per role type or industry I want, truth-checked against PROJECT_FACTS.md. Show me each one for approval, then fill RESUME_GUIDE.md so my applying agent knows which file to use for which role.

**Step 4. Write my setup plan.** A numbered checklist specific to my computer and accounts, with every click or command spelled out:
- create the separate application Gmail and add it to my Profile
- make one job-portal-only password of at least 16 characters (some portals need 14 to 16+), and save it in Muse's secure sign-in or keep it ready to send Muse when it asks. Never reuse another password and never write it in the workbook or kit
- connect the application Gmail to Muse using `guides/muse-gmail.md`
- delete the EXAMPLE rows, then upload the agent workbook to Google Sheets (File > Import, or open the .xlsx in Drive and Save as Google Sheets), check the Blocked tab's formula works, and connect Claude to Google Sheets and Gmail
- keep the candidate kit private: a Drive folder shared only with my applying agent's account
- install the role-finder skill from `dist/role-finder.zip` (source in `skills/role-finder`), create `targets.json` from the Agent Guide, do one test run with me, and schedule it daily
- sign up for Intern Insider, Handshake, Indeed and LinkedIn, and turn on daily internship job alerts on each one, sent to the application Gmail, so the role finder can read them even without browser access
- set up Muse: give it the workbook link and the candidate kit, tell it to read the Agent Guide tab first, do the TEST: claim, and only then start applying
- install the inbox-listener skill from `dist/inbox-listener.zip`, connect it to the application Gmail, run it once with me, and schedule it daily
- my daily routine: check the Blocked tab, do assessments and interviews, and spot-check a few submitted applications

**Step 5. Integrate.** Walk me through the plan one step at a time. After each step, ask me to confirm it worked or paste the error before moving on. Run the first role-finder pass and the first inbox check with me, and watch Muse's test claim land in Agent Activity.

Rules: be honest when you can't do something from where you're running (for example, you can't click around my computer from claude.ai) and tell me exactly what to do instead. Never put passwords or verification codes in the workbook.
