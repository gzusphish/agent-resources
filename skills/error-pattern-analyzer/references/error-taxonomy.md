# Error Taxonomy

Categorized error types with examples and prevention strategies.

## Tool Failures

### API Errors
- **Symptom**: HTTP errors, timeouts, rate limits
- **Common Causes**: Network issues, service down, quota exceeded
- **Prevention**: Check service status, implement retry with backoff
- **Detection**: Monitor response codes and latency

### Permission Errors
- **Symptom**: Access denied, unauthorized
- **Common Causes**: Wrong credentials, insufficient scope
- **Prevention**: Verify permissions before operations
- **Detection**: Check auth status early

### Timeout Errors
- **Symptom**: Operation didn't complete in time
- **Common Causes**: Large data, slow network, long processing
- **Prevention**: Batch large operations, add progress checks
- **Detection**: Monitor operation duration

## Assumption Errors

### File Structure Assumptions
- **Symptom**: File not found, wrong path
- **Common Causes**: Assuming specific directory structure
- **Prevention**: Verify structure before operations
- **Detection**: Check file existence, list directories first

### Dependency Assumptions
- **Symptom**: Import errors, missing packages
- **Common Causes**: Assuming dependencies installed
- **Prevention**: Check deps before code operations
- **Detection**: Verify imports work

### State Assumptions
- **Symptom**: Operation fails due to wrong state
- **Common Causes**: Assuming clean state, specific branch
- **Prevention**: Check git status, workspace cleanliness
- **Detection**: Status checks before operations

## Logic Errors

### Approach Selection
- **Symptom**: Wrong solution strategy
- **Common Causes**: Misunderstanding problem scope
- **Prevention**: Clarify requirements first
- **Detection**: User corrections, failed validations

### Reasoning Flaws
- **Symptom**: Conclusion doesn't follow from premises
- **Common Causes**: Rushed analysis, confirmation bias
- **Prevention**: Test assumptions, seek disconfirming evidence
- **Detection**: Verify each step

### Edge Case Blindness
- **Symptom**: Works for main case, fails on edge cases
- **Common Causes**: Focusing on happy path
- **Prevention**: Explicitly consider edge cases
- **Detection**: Test with boundary values

## Context Misses

### Scope Misses
- **Symptom**: Solution doesn't cover all requirements
- **Common Causes**: Incomplete requirements gathering
- **Prevention**: Checklist of requirements, user confirmation
- **Detection**: User requests additions

### Constraint Misses
- **Symptom**: Solution violates unstated constraints
- **Common Causes**: Implicit knowledge not surfaced
- **Prevention**: Ask about constraints explicitly
- **Detection**: User rejects approach

### History Misses
- **Symptom**: Ignoring previous decisions/context
- **Common Causes**: Not checking conversation history
- **Prevention**: Review context before suggesting
- **Detection**: User refers to previous discussion

## Communication Errors

### Intent Misunderstanding
- **Symptom**: Solution not what user wanted
- **Common Causes**: Ambiguous requests, assumptions
- **Prevention**: Paraphrase back, ask clarifying questions
- **Detection**: User corrections, rejection

### Style Misalignment
- **Symptom**: Output format not as expected
- **Common Causes**: Not confirming format preferences
- **Prevention**: Ask about output preferences
- **Detection**: User reformats or requests changes

### Timing Issues
- **Symptom**: Too much/too little communication
- **Common Causes**: Misreading user preferences
- **Prevention**: Watch for user cues
- **Detection**: User expresses frustration or silence
