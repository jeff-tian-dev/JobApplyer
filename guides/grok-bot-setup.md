# Set up Grok Bot as your applier

Grok Bot is xAI's agent. Each Bot works on its own cloud computer with a browser, a file system (`/workspace`) and a terminal, and keeps going when your laptop is closed. Here it claims roles from the agent workbook, fills applications with your candidate kit and records what happened.

Grok Bot is in beta and changes often. If a menu or tool name below doesn't match what you see, ask your Bot what it has now.

## 1. Get Grok Bot
1. Get an X subscription that includes Grok Bot (Premium or higher; Plus doesn't include it).
2. Install the Grok Bot app and sign in.
3. Create a Bot. Name: `grok` (this is the name it writes in the workbook). Title: `Internship applier`. Leave Description for step 5.
4. Always work with it in a **direct chat**, not a group chat. Group chats don't show approval requests or the secure forms it uses to ask for passwords.

## 2. Connect Gmail, Drive and Google Sheets
Use the separate Gmail you made just for applications, not your personal inbox, and keep the workbook in that same Google account.

1. In the app, open **Plugins** and connect **Gmail**, **Google Drive** and **Google Sheets**, signing in with your **application** Google account each time.
2. If you've connected more than one Google account, tell the Bot which one to use: "Use only <application Gmail> for Gmail, Drive and Sheets."
3. Gmail: read and search is all it needs. Keep sending and drafting behind approval.
4. Test Gmail: "Search my Gmail for the most recent email and tell me the subject line."
5. Test Sheets: the Bot should be able to read with `read_range` and write with `write_range` and `append_rows`. If it says the Sheets connector is missing, it can edit the Sheet in its own browser instead, but the connector is more reliable.

## 3. Give it your candidate kit
1. In the direct chat, attach every file from your candidate kit and your resume PDFs.
2. Say: "Save these under /workspace/candidate-kit/ with resumes in /workspace/candidate-kit/resumes/, then list every file back to me." Check the list against your kit.
3. Everything under `/workspace` stays between chats. Every Bot on your account can read it, so keep only your kit there and never anything secret.

Prefer Drive? Put the kit in a private Drive folder in the application account and tell the Bot where it is instead.

## 4. Install the applier skill
1. Attach `dist/grok-applier.zip` in the direct chat.
2. Say: "Unzip this and save it as a skill."
3. Ask it to confirm the skill is saved and describe what it does.

## 5. Paste the Bot's instructions
Copy the **Bot description** block from `skills/grok-applier/SKILL.md` into the Bot's **Description** (and Settings > General > Agent, if your app has it).

## 6. Test claim
Give the Bot your workbook link and say: "Open my agent workbook, read the Agent Guide tab, then do the TEST: claim it describes and read it back. Don't open any employer form." Check that a TEST: row shows up in Agent Activity with Agent `grok`.

## Passwords for job portals
Most portals (Workday, Greenhouse, iCIMS and so on) make you create an account. Set this up once:
- Make **one password used only for job-portal signups**. Never reuse your Gmail, school or bank password.
- Make it **at least 16 characters** with upper and lower case, a number and a symbol. Some portals require 14 to 16 or more, and one long password passes all of them.
- Give it to the Bot only through its **secure login form**: say "Ask me for my job-portal password with a login form." Type it in the form and choose **Save to vault** (it then lives in Settings › Vault) so it doesn't ask again. The Bot never sees it in the chat.
- Or take over the Bot's screen when it asks and type it yourself; the login then stays in its browser.
- Never paste the password into the chat, the agent workbook, the candidate kit, `/workspace` or any file you share.

## Codes, CAPTCHAs and two-factor
- The Bot reads verification codes from the connected application Gmail. If a code doesn't arrive, it marks the role blocked so you can grab the code yourself.
- For a CAPTCHA or two-factor prompt it asks you to take over its screen. Do the step, hand control back, and it carries on.

## Approvals
- For your first few applications, keep the final Submit click on **Allow once** so you see each one before it goes.
- After that, add narrow always-allow rules if you're comfortable. Never always-allow purchases, deletions or sending email.

## Running it daily (optional)
Once a few supervised applications have gone well, say: "Create a routine that runs the grok-applier skill every weekday at 10am." Routines run on your local time zone. Every run uses your weekly Grok usage, even when there's nothing to do, so don't schedule more often than you need. Set a daily cap in the Agent Guide's Pace row.

## If a portal blocks the Bot
Some job sites block cloud computers. If a portal won't load or keeps refusing the Bot, turn on **Route egress through this desktop** in the desktop app for that run so its traffic goes through your computer, then turn it off when it's done.

## Good to know
- Logins in the Bot's browser stay signed in, and every Bot on your account shares them. Separate Bots are not a security boundary.
- To disconnect a service, open Plugins and disconnect it. What the Bot already read can stay in its memory, and you can't delete individual memories.
- Deleting a Bot doesn't delete files or browser sessions on its computer.
