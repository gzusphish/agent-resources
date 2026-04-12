---
name: autoresearch-agent
description: "Autonomous experiment loop that optimizes files by measurable metrics. Use when: optimizing code speed, reducing bundle size, improving test pass rate, optimizing prompts, or running overnight improvement loops. Requires: target file, evaluation command, git repo."
---

# Autoresearch Agent

Autonomous experiment loop inspired by Karpathy's autoresearch. Edit → Evaluate → Commit/Reset → Repeat.

## When to Use

- "Make this faster / smaller / better"
- "Optimize [file] for [metric]"
- "Run experiments overnight"
- Any target file + measurable success metric

## Quick Start

```bash
# 1. Setup experiment
python scripts/setup_experiment.py \
  --domain engineering \
  --name api-speed \
  --target src/api/search.py \
  --eval "pytest bench.py --tb=no -q" \
  --metric p50_ms \
  --direction lower

# 2. Run single iteration
python scripts/run_experiment.py --experiment engineering/api-speed --single

# 3. Start autonomous loop
python scripts/run_experiment.py --experiment engineering/api-speed --loop --interval 10m
```

## Core Loop

1. **Review** results.tsv for patterns
2. **Decide** ONE change to target file
3. **Edit** the target
4. **Commit** with descriptive message
5. **Evaluate** via fixed evaluator
6. **Keep** (commit stands) or **Discard** (git reset)
7. **Log** result to results.tsv
8. **Repeat**

## Experiment Structure

```
.autoresearch/
├── config.yaml
└── {domain}/{experiment-name}/
    ├── program.md          ← Strategy, constraints
    ├── config.cfg          ← Target, eval cmd, metric
    ├── results.tsv         ← Experiment log
    └── evaluate.py         ← Evaluator (copied from evaluators/)
```

## Built-in Evaluators

| Evaluator | Metric | Use Case |
|-----------|--------|----------|
| `benchmark_speed` | `p50_ms` (lower) | Execution time |
| `benchmark_size` | `size_bytes` (lower) | File/bundle size |
| `test_pass_rate` | `pass_rate` (higher) | Test suite pass % |
| `build_speed` | `build_seconds` (lower) | Build time |

**SECURITY NOTE:** Evaluators use `shell=False` with list commands only. Configure as `["npm", "run", "build"]` not `"npm run build"`.

## Key Rules

- **One change per experiment** — isolate variables
- **Never modify evaluator** — ground truth must stay fixed
- **Simplicity wins** — small improvement with simpler code beats complex optimization
- **Timeout** — kill runs exceeding 2.5× time budget
- **5 crashes → pause** — alert user instead of burning cycles

## Viewing Results

```bash
# Single experiment
python scripts/log_results.py --experiment engineering/api-speed

# Dashboard
python scripts/log_results.py --dashboard

# Export
python scripts/log_results.py --experiment engineering/api-speed --format markdown
```

## Strategy Escalation

- Runs 1-5: Low-hanging fruit
- Runs 6-15: Systematic exploration
- Runs 16-30: Structural changes
- Runs 30+: Radical experiments
- 20+ runs no improvement → Update program.md strategy

## Custom Evaluators

If built-in evaluators don't fit, write your own `evaluate.py`:

```python
#!/usr/bin/env python3
import subprocess
result = subprocess.run(["my-benchmark", "--json"], capture_output=True, text=True)
print(f"my_metric: {parse_score(result.stdout)}")
```

Must print `metric_name: value` to stdout.

## Self-Improvement

After every 10 experiments, review results.tsv and update `program.md` Strategy section with learnings. Future iterations benefit from accumulated knowledge.

## Reference Files

- `references/setup-guide.md` — Detailed setup instructions
- `references/evaluator-writing.md` — Creating custom evaluators
- `agents/experiment-runner.md` — Advanced loop control
