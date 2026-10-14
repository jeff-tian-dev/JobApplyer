# Connect Gmail and Google Sheets to Muse

Use the separate Gmail you made just for applications, not your personal inbox.

Steps from Meta's help page ("How Muse works with Connectors", meta.com/help/artificial-intelligence/1687253048996149):

1. Open Muse and go to **Settings > Connectors**. (Or just tell Muse: "Connect my Gmail.")
2. Tap **Connect** next to Gmail and read what it will access.
3. Tap **Continue**, then sign in with your **application Gmail** and approve Google's permission screen.
4. Back in Connectors, open Gmail and set its permissions. Read/search access is enough for finding verification emails; leave sending set to "ask me first".
5. Test it: ask Muse "Search my Gmail for the most recent email and tell me the subject line." If it answers, it's connected.

## Connect Google Sheets (so Muse can claim roles and record results)

Muse works through your agent workbook, so it needs read and write access to it.

1. Upload the agent workbook to Google Drive and open it as a Google Sheet, in the same Google account you'll connect.
2. In Muse go to **Settings > Connectors**, tap **Connect** next to **Google Sheets**, tap **Continue**, and approve Google's permission screen.
3. Make sure Sheets is allowed to **edit**, not just read. Muse has to write claims, states and results.
4. Give Muse the Sheet's link and test it: "Open my agent workbook, read the Agent Guide tab, then do the TEST: claim it describes and read it back. Don't open any employer form." Check that a TEST: row shows up in Agent Activity.

Good to know:
- By default Muse asks before important actions like sending an email.
- Connecting email lets Muse search it; it doesn't download your whole inbox unless you ask.
- To disconnect: Settings > Connectors. What Muse already read can stay in its memory and history.
- Verification codes: Muse can read codes sent to the connected application Gmail. If a code ever doesn't show up for it, it should mark the role blocked so you can grab the code yourself.

## Passwords for job portals

Most portals (Workday, Greenhouse, iCIMS and so on) make you create an account. Set this up once:
- Make **one password used only for job-portal signups**. Never reuse your Gmail, school or bank password.
- Make it **at least 16 characters** with upper and lower case, a number and a symbol. Some portals require 14 to 16 or more, and one long password passes all of them.
- Muse only remembers passwords saved through its **secure sign-in**. If you don't use that, Muse will ask you for the password again from time to time. Send it in your private Muse chat when it asks.
- Never put the password in the agent workbook, the candidate kit or any file you share.
