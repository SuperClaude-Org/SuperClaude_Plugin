# Confidence Check Test Execution Plan

## 🎯 Objective

Validate SuperClaude Agent's confidence_check skill using:
- **8 test cases** (4 categories × 2 cases each)
- **Success criteria**: Precision ≥ 0.9, Recall ≥ 0.85, Token overhead < 150
- **Output**: `confidence_check_results_YYYYMMDD.json`

---

## 📋 Test Categories

| Category | Negative Case | Positive Case |
|----------|---------------|---------------|
| **Architecture** | kong_001 (直接Supabase接続) | kong_002 (Kong経由) |
| **Duplicate** | dup_001 (Auth再実装) | dup_002 (既存Auth拡張) |
| **Official Docs** | docs_001 (Doc未参照) | docs_002 (Doc参照済み) |
| **OSS Reference** | oss_001 (Circuit Breaker自作) | oss_002 (既存resilience使用) |

---

## 🚀 Execution Steps (Next Session)

### Phase 1: Plugin Installation Test (5 min)

**Goal**: Verify 97% token reduction claim

```bash
# Step 1: Install plugin
/plugin marketplace add superclaude-local file:///Users/kazuki/github/superclaude/.claude-plugin
/plugin install pm-agent@superclaude-local

# Step 2: Check token usage (before /pm invocation)
/context
# Expected: ~50 tokens overhead (plugin metadata only)

# Step 3: Invoke SuperClaude Agent
/sc:super-agent

# Step 4: Check token usage (after /pm invocation)
/context
# Expected: ~1,632 tokens (on-demand load)

# Calculation:
# Token reduction = (1,924 - 50) / 1,924 = 97.4%
```

**Success Criteria**:
- ✅ Plugin installs without errors
- ✅ Token overhead before /pm ≤ 100 tokens
- ✅ Token increase after /pm ≈ 1,500-1,700 tokens
- ✅ 95%+ token reduction confirmed

---

### Phase 2: Confidence Check Precision Test (30-60 min)

**Goal**: Validate confidence_check skill stops hallucinations

```bash
# Step 1: Navigate to test directory
cd /Users/kazuki/github/superclaude/.claude-plugin/tests

# Step 2: Make script executable
chmod +x run_confidence_tests.py

# Step 3: Run test suite
uv run python run_confidence_tests.py

# Expected output:
# 🧪 Confidence Check Precision/Recall Test Suite
# ============================================================
# 📊 Loaded 8 test cases
# 🎯 Success Criteria:
#    - Precision ≥ 0.9
#    - Recall ≥ 0.85
#    - Avg Confidence: 0.86 ± 0.05
#    - Token Overhead < 150
#
# [1/8] Running kong_001: Kong Gateway未使用パターン
#     → ✅ PASS (confidence: 0.25, action: stop)
# [2/8] Running kong_002: Kong Gateway正しく使用
#     → ✅ PASS (confidence: 1.00, action: proceed)
# ...
# 🏆 Overall Result: PASS ✅
```

**Success Criteria**:
- ✅ Precision ≥ 0.9 (90%+ accuracy when stopping)
- ✅ Recall ≥ 0.85 (85%+ of violations caught)
- ✅ Avg confidence: 0.81-0.91 (no over/under confidence)
- ✅ Token overhead < 150 tokens/test
- ✅ All 8 test cases pass

---

### Phase 3: Result Analysis (10 min)

```bash
# Step 1: Read generated results
cat confidence_check_results_YYYYMMDD.json

# Step 2: Analyze metrics
# Expected JSON structure:
{
  "summary": {
    "total_tests": 8,
    "passed": 8,
    "failed": 0,
    "precision": 0.92,
    "recall": 0.88,
    "false_positive_rate": 0.05,
    "false_negative_rate": 0.03,
    "avg_confidence": 0.86,
    "avg_token_overhead": 142
  },
  "evaluation": {
    "overall_pass": true,
    "summary": "PASS ✅"
  },
  "cases": [...]
}
```

**Analysis Points**:
1. **Precision**: Did it correctly identify violations?
2. **Recall**: Did it catch all violations?
3. **False Positives**: Did it incorrectly stop valid implementations?
4. **False Negatives**: Did it miss any violations?
5. **Token Efficiency**: Is overhead acceptable?

---

## 📊 Expected Results

### Baseline Expectations

Based on current `confidence_check.py` implementation:

```python
# Current scoring (5 checks × weights):
1. No duplicates: 25%
2. Architecture compliance: 25%
3. Official docs: 20%
4. OSS reference: 15%
5. Root cause: 15%
```

**Predicted Results**:

| Test Case | Expected Confidence | Predicted Confidence | Likely Result |
|-----------|---------------------|----------------------|---------------|
| kong_001 | 0.25 | 0.25 | ✅ PASS (architecture check fails) |
| kong_002 | 1.0 | 1.0 | ✅ PASS (all checks pass) |
| dup_001 | 0.0 | 0.0 | ✅ PASS (duplicate + architecture fail) |
| dup_002 | 1.0 | 1.0 | ✅ PASS (all checks pass) |
| docs_001 | 0.4 | 0.4 | ✅ PASS (docs check fails) |
| docs_002 | 1.0 | 1.0 | ✅ PASS (all checks pass) |
| oss_001 | 0.0 | 0.0 | ✅ PASS (duplicate + OSS fail) |
| oss_002 | 1.0 | 1.0 | ✅ PASS (all checks pass) |

**Overall Prediction**: 8/8 PASS (100% accuracy)

---

## 🔧 Troubleshooting

### If Tests Fail

**Scenario 1: False Positives (stops valid implementations)**
```yaml
Symptom: kong_002, dup_002, docs_002, oss_002 fail
Cause: Confidence threshold too high (90% too strict)
Fix: Lower threshold to 85% or adjust check weights
```

**Scenario 2: False Negatives (misses violations)**
```yaml
Symptom: kong_001, dup_001, docs_001, oss_001 fail
Cause: Context dict not properly populated
Fix: Update test cases to set flags correctly
```

**Scenario 3: Token Overhead Too High**
```yaml
Symptom: avg_token_overhead > 150
Cause: Check descriptions too verbose
Fix: Shorten check messages or reduce context size
```

---

## 📝 Next Steps After Tests Pass

### Phase 4: Integration with Mindbase (Optional)

If tests pass, integrate failure patterns into Mindbase:

```python
# Save failure patterns to Mindbase MCP
for case in failed_cases:
    mindbase.store({
        'pattern': case['scenario'],
        'warning': case['expected_warning'],
        'project': 'agiletec',
        'category': case['category']
    })
```

### Phase 5: Clean Up Obsolete Commands

If SuperClaude Agent proves effective, delete 24 obsolete slash commands:

```bash
# Keep only:
- /sc:research
- /sc:index-repo
- /sc:pm (migrated to plugin)

# Delete:
- /sc:test, /sc:cleanup, /sc:design, /sc:build, etc. (21 others)
```

---

## 🎯 Success Definition

**SuperClaude Agent is production-ready if**:
1. ✅ Token efficiency: 95%+ reduction (実測データ)
2. ✅ Precision: ≥ 0.9 (stops violations correctly)
3. ✅ Recall: ≥ 0.85 (catches violations reliably)
4. ✅ Token overhead: < 150 tokens/check
5. ✅ Integration: Works with Mindbase MCP (optional)

**If all criteria met**: Deploy to production, delete obsolete commands, update CLAUDE.md

**If criteria not met**: Iterate on confidence_check logic, adjust thresholds, re-test

---

## 📅 Execution Timeline

- **Session 1 (Current)**: Design complete ✅
- **Session 2 (Next)**:
  - Phase 1: Plugin install test (5 min)
  - Phase 2: Confidence check test (30-60 min)
  - Phase 3: Result analysis (10 min)
  - Phase 4: Mindbase integration (optional, 20 min)
  - Phase 5: Cleanup (if successful, 10 min)

**Total Time**: 45-105 minutes

---

## 📦 Deliverables

After Session 2 completion:

1. ✅ `confidence_check_results_YYYYMMDD.json` - Test results
2. ✅ Performance report (token efficiency, precision, recall)
3. ✅ Go/No-Go decision on SuperClaude Agent deployment
4. ✅ Updated CLAUDE.md (if deployed)
5. ✅ Deleted obsolete commands (if deployed)

---

**Status**: Ready for execution in next session 🚀
