---
name: git-comprehensive
description: "Use when managing Git operations including parallel worktree development, branch cleanup, commit workflows, PR management, CI/CD integration, or release processes."
license: "(MIT AND CC-BY-SA-4.0). See LICENSE-MIT and LICENSE-CC-BY-SA-4.0"
compatibility: "Requires git, gh CLI."
metadata:
  author: Consolidated from git-cleanup, git-workflow, git-worktree-manager
  version: "1.0.0"
allowed-tools: Bash(git:*) Bash(gh:*) Read Write Grep AskUserQuestion
---

# Git Comprehensive

Complete Git mastery covering parallel development with worktrees, branch lifecycle management, collaborative workflows, and release processes.

---

## Worktree Management

Create isolated development environments for parallel branch work with automatic port allocation and safe cleanup.

### Create a Fully-Prepared Worktree

```bash
# Create worktree with branch, port allocation, and dependency installation
python scripts/worktree_manager.py \
  --repo . \
  --branch feature/new-auth \
  --name wt-auth \
  --base-branch main \
  --install-deps \
  --format text
```

### Port Allocation Strategy

Default strategy is `base + (index * stride)` with collision checks:
- App: `3000`
- Postgres: `5432`
- Redis: `6379`
- Stride: `10`

Each worktree contains `.worktree-ports.json` with assigned ports.

### Cleanup with Safety Checks

```bash
# Scan stale worktrees and remove merged/clean ones
python scripts/worktree_cleanup.py --repo . --stale-days 14 --remove-merged --format text
```

**Safety Checklist:**
- Verify no uncommitted changes before removal
- Check branch merge status against target
- Confirm no running processes depend on worktree path

---

## Branch Cleanup

Safely analyze and clean up accumulated local branches and worktrees.

### Core Principle: SAFETY FIRST

**Never delete anything without explicit user confirmation.** Two-gate workflow: analysis review, then deletion confirmation.

### Branch Categories

| Category | Meaning | Delete Command |
|----------|---------|----------------|
| SAFE_TO_DELETE | Merged into default branch | `git branch -d` |
| SQUASH_MERGED | Work incorporated via squash merge | `git branch -D` |
| SUPERSEDED | Part of related group, work in main via PR | `git branch -D` |
| REMOTE_GONE | Remote deleted, work NOT found in main | Review needed |
| UNPUSHED_WORK | Has commits not pushed to remote | Keep |
| LOCAL_WORK | Untracked branch with unique commits | Keep |

### Critical: Squash-Merged Branches

`git branch -d` will ALWAYS fail for squash-merged branches. Use `git branch -D` from the start when squash-merge is detected.

### Group Related Branches First

Before categorization, group branches by name prefix (e.g., `feature/api-*`). Analyze as a group:
1. Find oldest/newest by commit date
2. Check if newer branches contain commits from older ones
3. Find which PRs merged work from each
4. Determine superseded branches

### Analysis Workflow

```bash
# Get default branch
default_branch=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@' || echo "main")

# Protected branches - never delete
protected='^(main|master|develop|release/.*)$'

# Gather information
git branch -vv
git worktree list
git fetch --prune
git branch --merged "$default_branch"
git log --oneline "$default_branch" | grep -iE "#[0-9]+" | head -30
```

### Safety Rules

1. Never invoke automatically — only on explicit request
2. Two confirmation gates only: analysis review, then deletion confirmation
3. Use correct delete command: `-d` for merged, `-D` for squash-merged/superseded
4. Never touch protected branches (main, master, develop, release/*)
5. Block dirty worktree removal without explicit data loss acknowledgment
6. Group related branches — don't scatter across categories

---

## Workflow Patterns

### Conventional Commits

```
<type>[scope]: <description>
```

**Types**: `feat` (MINOR), `fix` (PATCH), `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`

**Breaking change**: Add `!` after type or `BREAKING CHANGE:` in footer.

### Branch Naming

```bash
feature/TICKET-123-description
fix/TICKET-456-bug-name
release/1.2.0
hotfix/1.2.1-security-patch
```

### GitHub Flow (Default)

```bash
git checkout main && git pull
git checkout -b feature/my-feature
# ... work ...
git push -u origin HEAD
gh pr create && gh pr merge --squash
```

### PR Review Workflow

1. Load `references/pull-request-workflow.md` for detailed patterns
2. Resolve review threads before merging
3. Handle merge conflicts via rebase or merge strategies
4. Verify CI checks pass before merge

### Release Management

**CRITICAL**: Deleted releases block tag names PERMANENTLY.

See `references/github-releases.md` for prevention and recovery patterns.

---

## Reference Files

| Reference | When to Load |
|-----------|--------------|
| `references/worktree-patterns.md` | Creating/managing worktrees, port allocation |
| `references/branch-cleanup-safety.md` | Detailed safety rules for branch deletion |
| `references/branching-strategies.md` | Managing branches, choosing branching model |
| `references/commit-conventions.md` | Writing commits, semantic versioning |
| `references/pull-request-workflow.md` | Creating/reviewing PRs, thread resolution, merging |
| `references/ci-cd-integration.md` | CI/CD automation, GitHub Actions |
| `references/github-releases.md` | Release management, immutable releases |
| `references/git-hooks-setup.md` | Hook frameworks, detection, recommended hooks |

---

> **Note**: This skill consolidates git-cleanup, git-workflow, and git-worktree-manager.
