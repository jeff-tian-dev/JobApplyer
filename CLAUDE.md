# Instructions for Claude

This repository is an internship application setup kit.

## This project is paused
- Do not greet, ask for a resume, or start any step of `SETUP_PROMPT.md` when a session starts. Just answer what you're asked.
- Do not run, install or schedule the role-finder, resume-builder or inbox-listener skills, and do not start any Muse agents, unless explicitly asked in that session.
- If setup is explicitly requested, follow `SETUP_PROMPT.md` and write filled-in files to `my-setup/` (ignored by git), never over the templates.

## Where things are
- `SETUP_PROMPT.md`: the directions you follow.
- `workbook/agent-workbook.xlsx`: the shared agent workbook. Its Agent Guide tab is the rulebook every agent follows.
- `candidate-kit/`: templates for the private kit. Fill a copy in `my-setup/candidate-kit/`.
- `skills/role-finder`, `skills/resume-builder`, `skills/inbox-listener`: skills to install or follow. Each one has a SKILL.md.
- `guides/muse-gmail.md`: connecting Gmail to Muse, and handling portal passwords.
- `docs/GETTING_STARTED.md`: the human checklist version of the setup.

## Rules
- Never invent experience, answers, metrics or authorizations. Blank stays blank until they answer.
- Never write passwords, verification codes or other credentials into any file.
- Never commit or push their personal files. Everything personal goes in `my-setup/`.
- If you can't do a step from where you're running, say so and tell them exactly what to do themselves.
