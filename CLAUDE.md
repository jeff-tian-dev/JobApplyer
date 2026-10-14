# Instructions for Claude

This repository is an internship application setup kit. When someone opens it with you, your job is to set it up for them by following `SETUP_PROMPT.md` exactly. That file is the full set of directions, from the interview through filling the kit, building resumes, writing the setup plan and integrating each step.

## When a session starts here
1. Greet them in one line and ask for their master resume (any length, any format). Mention that, if they want, they can also give you a resume template of their own to use instead of the default format.
2. Then follow `SETUP_PROMPT.md` steps 1 to 5 in order, starting with the interview: rounds of at most 6 questions, grouped by topic, pulling whatever you can from their resume first.
3. Work on copies: write their filled-in files to a new `my-setup/` folder (already ignored by git), never over the templates.

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
