---
name: resume-builder
description: Build one tailored resume per role type or industry from my master resume, or a one-off version for a single posting. Use when I ask for resume variants, a resume for a kind of role, or a resume for a specific job link.
---

# Resume builder

Turns my master resume into a small library of targeted resumes, one per role type, and keeps my candidate kit's RESUME_GUIDE.md in sync so my applying agent always knows which file to use.

## Inputs
- My **master resume**: everything I've done, any length. Ask for it if it isn't attached.
- My candidate kit: `PROJECT_FACTS.md` (what I can claim), `profile.json` (contact, school, preferences) and `RESUME_GUIDE.md`.
- My **role types**: from the Agent Guide tab's Role types row, or ask me (for example: hardware, embedded/firmware, power electronics, software, AI/ML, test, product).

## Default resume format
Use this structure unless I give you my own template or ask for a different style. If I do, my template wins.

**Layout:** one column, US Letter, about 0.5 to 0.75 inch margins, one clean sans-serif font (like Lato or Calibri) at 10 to 11 pt, bold section headings with a thin rule under each. Dates and locations right-aligned on the same line as the company or school. No photos, icons, tables, text boxes, columns or skill bars, so applicant tracking systems can read it. Export as a text PDF (selectable text, not an image). LaTeX (for example a Jake's-Resume-style template), Word or Google Docs are all fine.

**Header:** name large and centered. One line under it: phone | email | LinkedIn | GitHub | portfolio, each one a working link.

**Sections, in this order:**
1. **Professional Summary**: 2 to 4 lines aimed at the role type. Who you are, what you build, your strongest relevant areas.
2. **Education**: school (location on the right); degree, major, minor and GPA if 3.5+ (expected graduation on the right); one "Relevant Coursework" bullet picked for the role type.
3. **Work Experience**: company (location on the right); title (dates on the right); 2 to 4 bullets each.
4. **Research & Publications** (if any): title (venue or funding and year on the right); 1 to 3 bullets.
5. **Projects**: name | link on the left, tech stack on the right; 2 to 4 bullets.
6. **Honors & Awards** and **Leadership & Organizations**: short, one line each.
For a role type where projects beat experience (for example software with little software work history), Projects can move above Work Experience.

**Bullets:** start with a strong past-tense verb (Designed, Built, Led, Measured), say what you did and how, and end with the result. Put a real number in when you have one (sizes, speeds, percentages, counts). Keep each bullet to 1 or 2 lines, with no "Responsible for" and no first person. Put the posting's key terms in naturally where they're true.

**Length:** one page for every variant. The master can be as long as it needs to be.

## Building the library (up to 8 variants)
1. **Confirm the list.** Propose up to 8 role types from my targets, with one line on what each one emphasizes. Wait for my OK before building.
2. **Pick a base format.** If I gave you my own template or style, use it. Otherwise use the Default resume format above, and keep the same format across all variants.
3. **For each role type:**
   - Read 3 to 5 real postings of that type (from my Discovery tab, or search) and list the skills and words they repeat.
   - Choose what goes in: the most relevant experience and projects go first, and unrelated items are trimmed or cut. Reorder bullets so the closest match leads.
   - Reword using the postings' terms **only where it's still true** (for example "automated testing" to "test automation").
   - Keep it to **one page**.
4. **Truth check, every variant.** Every bullet must trace back to my master resume or PROJECT_FACTS.md. No new metrics, tools, titles, dates or results. Never move one project's numbers to another. Follow every "Don't say" line. List anything you were unsure about and ask me.
5. **Save.** Name files `Firstname_Lastname_<RoleType>.pdf` (plus the editable source). Export to PDF. If you can't create files where you're running, give me the full text of each variant and tell me how to paste it into my template.
6. **Update RESUME_GUIDE.md.** Fill the table with role type → file name, plus one line on when to use each.
7. **Show me a summary:** each variant, what leads it, and anything you cut. I approve before these go to my applying agent.

## One-off version for a single posting
When I give a job link: read the posting, start from the closest variant, apply the same steps and truth check, save it as `Firstname_Lastname_<Company>_<Role>.pdf`, and note in the Agent Queue row (Resume column) which file was used.

## Rules
- Never invent experience, skills, metrics, dates, GPA, awards or links.
- Don't change contact details, school, dates or titles between variants.
- Keep the master unchanged. It's the source of truth, not a resume to send.
