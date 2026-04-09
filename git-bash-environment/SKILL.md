---
name: git-bash-environment
description: Use when running commands in this Git Bash environment to ensure correct syntax and tool selection
---

# Git Bash Environment Interface

## Shell Profile

**Git Bash (MSYS2) 5.2.37** - Unix-like shell on Windows with GNU coreutils

## Available Tools

All standard POSIX tools available:

| Tool | Status | Notes |
|------|--------|-------|
| **ls** | ✅ | GNU coreutils |
| **cp** | ✅ | GNU coreutils (`cp -r` for recursive) |
| **mv** | ✅ | GNU coreutils |
| **rm** | ✅ | GNU coreutils (`rm -rf` for recursive) |
| **mkdir** | ✅ | GNU coreutils (`mkdir -p` for nested) |
| **grep** | ✅ | GNU grep 3.0 |
| **head/tail** | ✅ | GNU coreutils |
| **awk** | ✅ | GNU Awk 5.3.1 |
| **cat** | ✅ | GNU coreutils |
| **echo** | ✅ | Built-in |
| **pwd** | ✅ | Built-in |
| **find** | ✅ | GNU findutils |
| **chmod** | ✅ | GNU coreutils |

## Windows Bridge Tools

When you need Windows-specific functionality:

| Tool | Syntax | Example |
|------|--------|---------|
| **PowerShell** | `powershell -Command "..."` | `powershell -Command "Get-ChildItem"` |
| **cmd** | `cmd //c command` | `cmd //c xcopy //E source dest` |
| **xcopy** | `cmd //c xcopy //E //I //Y` | Note: `//` instead of `/` |

## Critical Syntax Notes

### xcopy in Git Bash

**ALWAYS use doubled slashes for switches:**

```bash
# ❌ WRONG: Git Bash interprets /E as path
xcopy /E /I source dest

# ✅ CORRECT: // passes as / to Windows
cmd //c xcopy //E //I //Y source dest
```

| Switch | Git Bash Syntax | Meaning |
|--------|-----------------|---------|
| /E | //E | Recursive, including empty dirs |
| /I | //I | Assume directory if dest doesn't exist |
| /Y | //Y | Suppress overwrite prompt |
| /S | //S | Recursive, skip empty dirs |

### Path Formats

| Context | Format | Example |
|---------|--------|---------|
| Git Bash commands | Unix-style | `../agent-resources/skills/` |
| cmd / PowerShell | Windows-style | `..\\agent-resources\\skills\\` |
| Mixed (cmd in Git Bash) | Doubled | `//c//Windows//System32` |

## File Operations Quick Reference

```bash
# Copy file
cp source.txt dest.txt

# Copy directory recursively
cp -r source_dir/ dest_dir/

# Copy with verbose
cp -rv source_dir/ dest_dir/

# Move/rename
mv old.txt new.txt
mv file.txt ../archive/

# Remove
rm file.txt
rm -rf directory/

# Create directories
mkdir -p path/to/nested/dir

# List with details
ls -la

# Find files
grep -r "pattern" --include="*.md" .

# View file content
cat file.txt | head -50
```

## When to Use What

```
Need to copy files?
├── Simple file copy → cp
├── Directory recursively → cp -r
├── Many files with filtering → find + cp
└── Windows-specific behavior → cmd //c xcopy //E //I //Y

Need Windows-specific features?
├── Registry, WMI, .NET → powershell -Command "..."
├── Legacy DOS commands → cmd //c command
└── Windows paths required → Use // instead of / for switches
```

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `Invalid switch - /E` | Used single slash in Git Bash | Use `//E` instead |
| `The system cannot find the path` | Wrong path format | Check Unix vs Windows path style |
| `command not found` | Tool not in PATH | Use `which toolname` to verify |

### Git LFS Smudge Failure (TLS / certificate trust)

Symptom during `git reset --hard` or `git checkout`:
```
tls: failed to verify certificate: x509: certificate signed by unknown authority
error: external filter 'git-lfs filter-process' failed
```

**Fast recovery — exclude common LFS binary asset types via sparse-checkout:**
```bash
git sparse-checkout set "/*" "!*.png" "!*.gif"
git reset --hard HEAD
```

**Alternative — skip LFS download entirely (safe for reference/read-only repos):**
```bash
GIT_LFS_SKIP_SMUDGE=1 git reset --hard HEAD
```

The root cause is corporate CA chain not being trusted by Git's TLS stack for the LFS batch endpoint. The above workarounds restore the working tree without fixing the underlying trust issue.

## Verification Commands

```bash
# Check tool availability
which cp          # /usr/bin/cp
which powershell  # /c/Windows/System32/WindowsPowerShell/v1.0/powershell
which python3     # (may be missing)

# Check versions
cp --version | head -1
bash --version | head -1
ls --version | head -1
```

## Environment Summary

**Git Bash (MSYS2) 5.2.37** on Windows
- Standard POSIX environment with GNU coreutils
- `cp -r` works for recursive copy
- Use `cmd //c` prefix for Windows cmd tools
- Use `//` instead of `/` for cmd switches
- PowerShell available as `powershell`
- Python3 may not be in PATH
