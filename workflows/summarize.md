---
description: Summarize current conversation using conversation-manager skill
auto_execution_mode: 2
---

Summarize the current active conversation using the conversation-manager skill and store the result in the scriptorium.

**BEFORE DOING ANYTHING ELSE:**
Check the timestamp of the first exchange in this conversation

## 1) Intake (define the summary)
- Task statement: Summarize current conversation
- Success criteria: Summary stored in scriptorium with proper format
- Scope: Current active conversation only
- Risk level: Low
- Constraints: Must use conversation-manager skill exactly, output to scriptorium

## 2) Route (pick the approach)
- Selected skills/tools/workflows: conversation-manager skill
- Evidence sources to consult: Current conversation transcript
- Expected outputs: Formatted summary file in .panopticon/scriptorium/

## 3) Preflight (security + enforceability)
Required when risk is Medium/High or when touching skills/rules/workflows/tooling.

**Risk Level**: Low - No preflight required
- Read-only conversation processing
- No security boundary interaction
- No changes to skills/rules/workflows/tooling

## 4) Execute
Apply the conversation-manager skill to summarize the current conversation:

1. **Invoke conversation-manager skill** per `@[.panopticon/.windsurf/skills/conversation-manager/SKILL.md]`
2. **Process current conversation** using the skill's documented approach
3. **Generate structured summary** following conversation-manager template format
4. **Store summary** in `@[.panopticon/scriptorium]` with timestamped filename

**Implementation steps:**
- Use conversation-manager skill exactly as documented
- Apply two-stage loading if conversation is lengthy
- Follow conversation-manager's YAML frontmatter and exchange ID structure
- Ensure output location is explicitly .panopticon/scriptorium/

## 5) Evaluate (gated, ordered)
Evaluate in this order; stop at the first failing gate.

### Gate 1: Security
- Check for dangerous execution patterns and supply-chain risk
- **Expected**: PASS (read-only processing)

### Gate 2: Documentation integrity
- Ensure docs match reality (paths, tools, claims)
- **Expected**: PASS (using existing documented skill)

### Gate 3: Skill quality
- Clear contract, deterministic outputs, triggers/stop conditions
- **Expected**: PASS (conversation-manager skill already vetted)

### Gate 4: Rules coherence
- No contradictions/duplication; rules refer to mechanisms where possible
- **Expected**: PASS (following established patterns)

### Gate 5: Coding correctness
- Tests/build/lint where available
- **Expected**: PASS (no new code required)

## 6) Decide + Loop
- If all gates PASS:
  - Proceed to Record
- If a gate FAILS:
  - Self-correct decision:
    - CONTINUE (only if failure is non-blocking and risk is understood)
    - ADAPT (change approach, add checks, narrow scope)
    - ESCALATE (ask user for decision/approval/info)
    - ABANDON (stop; record why)
  - Loop target:
    - If routing/preflight wrong -> go to Route or Preflight
    - If implementation wrong -> go to Execute
    - If evaluation rubric wrong -> update rubric, then re-evaluate

Repeat until success criteria are met or you ESCALATE/ABANDON.

## 7) Record (scriptorium)
Create/update a scriptorium entry with:
- Task: Conversation summarization
- Risk level: Low
- Route chosen: conversation-manager skill
- Preflight results: Not required (Low risk)
- Evaluation results (which gate failed/passed)
- Changes made (summary file created)
- Follow-ups: None expected

**Output file location**: `.panopticon/scriptorium/YYYYMMDD.HHMM-[descriptive-name].md`
- Use timestamp of FIRST exchange, not current date
- Example: If first exchange was April 10, 2026 at 2:21pm → `20260410.1421-conversation-summary.md`
