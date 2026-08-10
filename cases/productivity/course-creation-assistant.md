# Course Creation Assistant

> Help a product manager design and produce a practical programming course without requiring them to write every document or code sample manually.

---

## 🎯 Pain Point

A product manager may want to turn practical experience into a course but struggle to validate code, coordinate course documents and scripts, and quickly incorporate new ideas.

---

## 💡 What It Does

Minis acts as a course-production assistant:

- Designs the course structure and chapter sequence
- Generates project examples and supporting code
- Writes lesson scripts
- Produces course descriptions, welcome messages, glossaries, and FAQs
- Runs and reviews generated examples before presenting them as ready to teach

The user remains responsible for product decisions, subject-matter accuracy, and final acceptance.

---

## 🛠 Skills and Capabilities

| Skill or capability | Purpose | Availability |
|---------------------|---------|--------------|
| Built-in file and coding tools | Write, run, test, and revise course examples | Built into Minis |
| `project-case-builder` | Generate project examples | Contributor-provided custom skill; not currently in public MinisSkills |
| `video-script-writer` | Write lesson scripts | Contributor-provided custom skill; not currently in public MinisSkills |
| `project-reviewer` | Review code quality | Contributor-provided custom skill; not currently in public MinisSkills |

The workflow does not require those three custom skills. Minis can perform the same bounded tasks with built-in coding, file, and testing tools. Do not describe the custom skills as publicly installable unless their source is supplied.

---

## 📋 How to Use

1. Define the audience, course goal, prerequisites, and differentiator.
2. Design the chapter sequence and learning objectives.
3. Generate one chapter at a time, including code, exercises, and lesson script.
4. Run and test every code sample before accepting it.
5. Generate operating material such as the course description, glossary, and FAQ.
6. Version each revision so later changes remain traceable.

---

## 💬 Example Prompts

```text
I am a product manager creating a six-chapter Python course for complete beginners.
The goal is to help students start vibe coding. Each chapter must contain one
practical project. Design the course structure, prerequisites, learning objectives,
and an observable completion check for each chapter.
```

```text
Create the chapter-one weather lookup project. Write the runnable code and tests,
execute the tests, then write a 15-minute teaching script that explains the verified implementation.
```

---

## 📤 Expected Output

- Six or seven chapters with clear learning objectives
- Runnable and tested Python or HTML examples
- Detailed lesson scripts with interaction prompts
- Course description, welcome message, glossary, and FAQ
- Versioned revisions

---

## ⚙️ Requirements

- [ ] No public repository skill is required
- [ ] Prepare a target-audience description and initial course goal
- [ ] If using the contributor's custom skills, obtain them from their original source and review them before installation

---

## 💡 Tips

- Define the teaching perspective and expected student background explicitly.
- Ask Minis to preserve version numbers and a concise change log.
- Build reusable chapter and lesson-script templates.
- Treat generated code as unverified until it has been executed and tested.

---

## 👤 Author

Submitted by **@sawyer-wang**

---

## 📅 Case Last Verified

2026-04

## 🔄 Skill Catalog Check

Checked against `OpenMinis/MinisSkills` commit `3993f5ab0a0ff204d774da7a5cf27ea281e7b021` on 2026-07-27.
