---
name: privacy-guardian
description: "Use when handling files that may contain sensitive information. Automatically screens content and routes to local models when credentials, PII, or secrets are detected."
allowed-tools:
  - Read
  - Bash
  - Write
---

# Privacy Guardian

Protect sensitive data by screening files before cloud processing.

## When to Use

- Opening files from unknown sources
- Processing code with potential credentials
- Handling data exports, logs, or config files
- Any uncertainty about file sensitivity

## Screening Protocol

### Step 1: Fast Heuristic Check

Run regex patterns to detect common sensitive data:

| Pattern Type | Examples |
|--------------|----------|
| Credentials | `password = "..."`, `api_key = "..."` |
| PII | SSN patterns, emails, credit cards |
| Financial | Account numbers, routing numbers |
| Security Files | `.env`, `.pem`, `.key` files |

### Step 2: Local Model Verification (if needed)

For edge cases or high-stakes decisions, use local model:

```bash
python C:/Users/wyatt/git/agent-workspaces/model-testing/model-testing/scripts/sensitive_router.py \
  --screen <file> \
  --model llama3.2
```

**Exit codes:**
- `0` = Safe for cloud processing
- `1` = Sensitive — use local model only
- `2` = Error — assume sensitive

## Decision Matrix

| Heuristic | Local Verdict | Action |
|-----------|-------------|--------|
| Positive | N/A | **Use local model** — detected credentials/PII |
| Negative | Sensitive | **Use local model** — edge case detected |
| Negative | Safe | **Use cloud** — verified safe |
| Error | N/A | **Use local model** — fail secure |

## Integration with Panopticon

### Automatic Screening on File Operations

Before reading a file with `Read` tool:

```python
# Check if file needs screening
if file_path.suffix in ['.env', '.key', '.pem'] or file_path.stat().st_size < 1000000:
    result = run_sensitive_check(file_path)
    if result.is_sensitive:
        print(f"⚠️  Sensitive content detected: {file_path}")
        print(f"   Reasons: {result.reasons}")
        print(f"   Action: Use local model or handle manually")
        # Do not proceed with cloud processing
```

### Skill Selection Based on Sensitivity

| Task | Risk Level | Recommended Model |
|------|-----------|-------------------|
| Public code analysis | Low | Cloud (fastest) |
| Generic config review | Low-Medium | Cloud with caution |
| Credentials found | **High** | Local model (phi4) |
| Proprietary code | **High** | Local model (llama3.2) |
| Unknown origin | Unknown | Screen first, then decide |

## Safe Handling Patterns

**If sensitive content detected:**

1. **Don't read the file into context** — stops exposure
2. **Log the finding** — record what was detected (not the actual secret)
3. **Route to local model** — process with Ollama
4. **Summarize safely** — local model can describe without exposing

**Example safe workflow:**
```
User: Analyze this config file
→ Privacy Guardian screens file
→ Detects: api_key pattern
→ Action: Route to local phi4
→ Local model: Analyzes and reports issues
→ Result: User gets analysis, no data leaves machine
```

## What Never to Do

- **Never** send `.env` files to cloud models
- **Never** process `id_rsa`, `.pem` keys externally
- **Never** assume "it looks safe" without checking
- **Never** log actual credential values
- **Never** override a positive sensitive detection

## Quick Reference

**Screen a file:**
```bash
python C:/Users/wyatt/git/agent-workspaces/model-testing/model-testing/scripts/sensitive_router.py --check <file>
```

**Batch screen directory:**
```bash
python C:/Users/wyatt/git/agent-workspaces/model-testing/model-testing/scripts/sensitive_router.py \
  --batch <directory> \
  --output screening_results.json
```

**Manual local model query:**
```bash
ollama run phi4
```
