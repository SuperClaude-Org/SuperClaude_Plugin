# PM Agent Confidence Check Test Suite

## 📊 Overview

This test suite validates the `confidence_check` skill's ability to prevent hallucinations and enforce investigation loops before implementation.

**Goal**: Ensure Claude stops at <90% confidence and continues investigation, rather than implementing with incomplete knowledge.

---

## 🗂️ Files

| File | Purpose |
|------|---------|
| `confidence_test_cases.json` | 8 test cases (4 categories × 2 cases) |
| `run_confidence_tests.py` | Evaluation script (precision/recall) |
| `EXECUTION_PLAN.md` | Next session execution guide |
| `README.md` | This file |

---

## 🧪 Test Categories

### 1. Architecture Compliance (Kong Gateway)

**Real Data Source**: `agiletec/PROJECT_INDEX.md:93`, commit `d6c9f2dc3`

- **kong_001** (negative): Direct Supabase connection → Should STOP
- **kong_002** (positive): Kong Gateway (port 8000) → Should PROCEED

**Why This Matters**: agiletec enforces "All Supabase HTTP access MUST go through Kong Gateway" — this test validates the rule is followed.

### 2. Duplicate Implementation

**Real Data Source**: `agiletec/docs/code-quality.md:22` (Supabase Auth duplication)

- **dup_001** (negative): Reimplement Supabase Auth → Should STOP
- **dup_002** (positive): Extend existing Auth with MFA → Should PROCEED

**Why This Matters**: Prevents reinventing existing functionality (Supabase Auth already exists).

### 3. Official Documentation

**Pattern**: Guessing API endpoints vs reading official docs

- **docs_001** (negative): Guess Supabase Storage endpoint → Should STOP
- **docs_002** (positive): Read official docs, use SDK → Should PROCEED

**Why This Matters**: Ensures Claude references official documentation before implementation.

### 4. OSS Reference

**Real Data Source**: `agiletec/libs/resilience/` (existing circuit breaker)

- **oss_001** (negative): Implement circuit breaker from scratch → Should STOP
- **oss_002** (positive): Use existing libs/resilience → Should PROCEED

**Why This Matters**: Prevents reinventing OSS libraries already in the project.

---

## 🚀 Quick Start (Next Session)

```bash
# 1. Navigate to test directory
cd /Users/kazuki/github/superclaude/.claude-plugin/tests

# 2. Run tests
uv run python run_confidence_tests.py

# 3. Check results
cat confidence_check_results_$(date +%Y%m%d).json
```

**Expected Runtime**: ~30 seconds (8 tests)

---

## 📊 Success Criteria

| Metric | Threshold | Current |
|--------|-----------|---------|
| **Precision** | ≥ 0.9 | TBD |
| **Recall** | ≥ 0.85 | TBD |
| **Avg Confidence** | 0.81-0.91 | TBD |
| **Token Overhead** | < 150 tokens | TBD |

**Overall**: All 4 metrics must pass for production deployment.

---

## 📈 Test Results (To Be Updated)

Results will be saved to `confidence_check_results_YYYYMMDD.json` after running tests.

**Status**: ⏳ Awaiting next session execution

---

## 🔧 Debugging

If tests fail, check:

1. **Context dict population**: Ensure `architecture_check_complete`, `duplicate_check_complete`, etc. are set correctly
2. **Confidence threshold**: Currently 0.9 (90%) — may need adjustment
3. **Check weights**: Currently 25%, 25%, 20%, 15%, 15% — may need rebalancing

See `EXECUTION_PLAN.md` for detailed troubleshooting.

---

## 📝 Next Steps

After tests pass:
1. ✅ Deploy PM Agent to production
2. ✅ Delete 24 obsolete slash commands
3. ✅ Update CLAUDE.md (lightweight rules only)
4. ✅ Integrate with Mindbase MCP (optional)

See `EXECUTION_PLAN.md` for full roadmap.

---

**Last Updated**: 2025-10-21
**Test Suite Version**: 1.0.0
**Status**: Ready for execution 🚀
