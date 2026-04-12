# Profile: General Engineering (Python / CLI / light projects)

## Rules (Guardrails)

These are written in a style the agent can *internalize per loop*, not just glance at once.

```
- Always reproduce the issue or confirm current behavior before making changes.
- Prefer reading and understanding relevant code before modifying it.
- Make the smallest possible change that could solve the problem.
- After every code change, validate by running the relevant script, test, or command.
- Do not modify unrelated code or perform broad refactors unless explicitly required.
- If the cause of an issue is unclear, gather more information instead of guessing.
- When multiple solutions are possible, prefer the simplest and most maintainable.
- Stop once the task is complete and verified. Do not continue making unnecessary improvements.
```

## Skills (Capabilities to Enable)

Make sure your workspace exposes or encourages these:

```
- search_codebase
- open_file / read_file
- apply_patch / edit_file
- run_shell_command
- inspect_command_output
- list_files / navigate_directory
```

### Optional but Valuable

```
- run_tests (if you introduce tests later)
- git_diff / view_changes
```

## Workflows (Playbooks, Not Scripts)

These should guide behavior, not constrain it.

### Bug Fix Workflow

```
- Reproduce the issue using a command or script
- Identify the exact failure point (error message, incorrect output)
- Locate relevant code
- Understand the current logic before changing anything
- Apply a minimal fix
- Re-run the original command or test
- Repeat until resolved
```

### Feature Workflow

```
- Understand how similar functionality is implemented
- Identify the correct integration point
- Implement incrementally
- Validate behavior after each meaningful change
- Keep changes consistent with existing patterns
```

### Refactor Workflow

```
- Confirm current behavior first
- Make small, isolated improvements
- Avoid changing behavior unless required
- Validate after each change
```


## Behavioral Bias (This Is the Secret Sauce)

If your system allows a “system prompt” or guiding instruction, this is gold:

```
- Prefer information gathering over assumptions when uncertain.
- Think in small steps: observe → act → verify.
- Treat each change as an experiment that must be validated.
- Avoid making multiple simultaneous changes that obscure cause and effect.
- Use tool feedback (errors, outputs) to guide the next step.
```

## ⚙️ Environment Assumptions (Desktop-Friendly Tweaks)

Since you're not in Termux:

* You can rely on:

  * fuller shell environment
  * better file navigation
  * potentially faster execution

So this config subtly encourages:

* **more frequent validation**
* **slightly deeper inspection before acting**

# What This Will Feel Like in Practice

When you say:

> “Fix this bug”

You’ll see behavior like:

1. Runs the script first
2. Reads the error
3. Opens the exact file
4. Makes a *small* change
5. Runs again
6. Stops when clean

Not:

> “I rewrote half the function, let’s hope”

# Optional Tiny Upgrade (Highly Recommended)

Add this one line somewhere prominent:

```
- Always run the simplest possible command to validate behavior before and after changes.
```

This dramatically improves loop quality.

# What To Do Next

1. Drop this in as your **default workspace**
2. Use it for everything for a bit
3. Watch for friction:

   * too cautious?
   * too loose?
   * missing a skill?

Then we evolve it into:

* Fast workspace (looser)
* Strict workspace (tighter)

If you want, next step we can:

* Translate this into a **Windsurf-native format (if you show me yours)**
* Or simulate a **real task run-through** using this config so you can see the loop in action step-by-step
