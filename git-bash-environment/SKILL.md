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
 
## Windsurf on Windows: Command Execution Patterns
 
### What Works Directly
 
These commands execute correctly without wrapping:
 
```bash
# Basic commands
ls
echo "message"
cat file.txt
pwd
which command
 
# Command options
ls -la
head -n 5 file.txt
grep -r "pattern" --include="*.md" .
find . -name "*.md" -type f
 
# Quoting and variable expansion
echo 'single quotes'
echo "double quotes with $PATH expansion"
echo "escaped \"quotes\""
 
# Simple command substitution with built-ins
echo "Current dir: $(pwd)"
 
# Semicolon separator
echo "one"; echo "two"; echo "three"
 
# OR operator
false || echo "fallback"
 
# AND chains work (built-in or external)
echo "first" && echo "second"
ls && echo "success"
head --version && echo "done"
```
 
### What Requires bash -c Wrapper
 
These patterns fail unless wrapped in `bash -c '...'`:
 
```bash
# ❌ FAILS: Pipelines with GNU tools
ls | head
cat file.txt | grep "pattern"
echo test | awk '{print $1}'
 
# ✅ WORKS: Wrap in bash -c
bash -c 'ls | head'
bash -c 'cat file.txt | grep "pattern"'
bash -c 'echo test | awk "{print \$1}"'
 
# ❌ FAILS: Redirects
echo "output" > file.txt
echo "append" >> file.txt
cat file.txt 2>&1
 
# ✅ WORKS: Wrap in bash -c
bash -c 'echo "output" > file.txt'
bash -c 'echo "append" >> file.txt'
bash -c 'cat file.txt 2>&1'
 
# ❌ FAILS: Complex command substitution
result=$(ls | head -n 1)
 
# ✅ WORKS: Wrap entire expression
bash -c 'result=$(ls | head -n 1) && echo "First: $result"'
 
# ⚠️ CRITICAL: Subshells HANG indefinitely (not just fail)
(echo "in subshell"; pwd)   # NEVER RETURNS - use bash -c!
(ls | head -1)              # NEVER RETURNS - use bash -c!

# ✅ WORKS: Wrap in bash -c
bash -c '(echo "in subshell"; pwd)'
bash -c '(cd /tmp; ls | head -3)'
```
 
### Rule of Thumb

**Use `bash -c` wrapper if your command includes:**
- Pipes (`|`)
- Redirects (`>`, `>>`, `<`, `2>&1`)
- Subshells `( )` ⚠️ **WARNING: hangs if not wrapped**
- Command substitution containing pipes: `$(cmd | cmd)`
- Any combination of the above

**DO NOT need `bash -c` for:**
- Simple `&&` or `||` chains (they work directly)
- Basic command substitution without pipes: `$(pwd)`
- Semicolon-separated commands: `cmd1; cmd2`
 
## Why bash -c is Needed (Root Cause)

Windsurf on Windows validates commands using `bash.exe -n -c` before execution. This validation runs in a Windows command context where special characters (`|`, `>`, `<`) are intercepted by Windows CMD parsing before reaching bash.

**The Pattern:**
- `ls | head` → Windows intercepts `|` → Parser error: `'head' not recognized`
- `echo > file` → Windows intercepts `>` → Error: `The system cannot find the path`
- `(echo test)` → Parser hangs waiting for closing paren → **Never returns**

**The Fix:**
Wrapping in `bash -c '...'` ensures the entire command string is passed to bash as a single argument, bypassing Windows CMD interpretation.

**Escaping Inside bash -c:**
When using `bash -c`, escape `$` for literal dollar signs:
```bash
# ❌ WRONG: $1 expanded by outer shell
bash -c 'echo "test" | awk "{print $1}"'

# ✅ CORRECT: \$1 passed literally to awk
bash -c 'echo "test" | awk "{print \$1}"'
```

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
| Git Bash commands | Unix-style | `../agent-external/skills/` |
| cmd / PowerShell | Windows-style | `..\\agent-external\\skills\\` |
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
 
# View file content (requires bash -c for pipes)
bash -c 'cat file.txt | head -50'
 
# Chaining with pipes (requires bash -c)
bash -c 'ls | head && echo "done"'
 
# Redirects (requires bash -c)
bash -c 'echo "output" > file.txt'
bash -c 'cat file.txt >> another.txt'
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

Need to choose command format?
│
├─ Contains | (pipe)? ───────────────┐
│                                    YES → Use bash -c
│                                     NO ↓
├─ Contains >, >>, <, 2>&1? ───────┐
│                                    YES → Use bash -c
│                                     NO ↓
├─ Contains (subshell)? ─────────────┐
│                                    YES → Use bash -c (or it HANGS)
│                                     NO ↓
├─ Contains $(cmd | cmd)? ───────────┐
│                                    YES → Use bash -c
│                                     NO ↓
└─ All other cases ──────────────────→ Run directly
```
 
## Troubleshooting
 
| Error | Cause | Fix |
|-------|-------|-----|
| `Invalid switch - /E` | Used single slash in Git Bash | Use `//E` instead |
| `The system cannot find the path` | Wrong path format | Check Unix vs Windows path style |
| `command not found` | Tool not in PATH, or pipeline/redirect/chaining not parsed correctly | Use `which toolname` to verify tool exists, then wrap command in `bash -c '...'` |
 
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
 
# Check versions (use bash -c for pipes)
bash -c 'cp --version | head -1'
bash -c 'bash --version | head -1'
bash -c 'ls --version | head -1'
```
 
## Environment Summary
 
**Git Bash (MSYS2) 5.2.37** on Windows
- Standard POSIX environment with GNU coreutils
- `cp -r` works for recursive copy
- Use `cmd //c` prefix for Windows cmd tools
- Use `//` instead of `/` for cmd switches
- PowerShell available as `powershell`
- Python3 may not be in PATH
- **Windsurf**: Pipelines, redirects, and complex chaining require