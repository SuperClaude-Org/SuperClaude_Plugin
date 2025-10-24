#!/usr/bin/env python3
"""
Confidence Check Precision/Recall Test Suite

Evaluates confidence_check skill against 8 test cases:
- 4 系統: Kong Gateway, Duplicate Implementation, Official Docs, OSS Reference
- Each系統 has 2 cases: negative (should stop) + positive (should proceed)

Success Criteria:
- Precision ≥ 0.9 (stopped correctly / all stops)
- Recall ≥ 0.85 (stopped correctly / should stop)
- Avg confidence: 85 ± 5%
- Token overhead < 150 tokens/test

Output: confidence_check_results_YYYYMMDD.json
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Tuple

# Add parent directory to path to import confidence_check
sys.path.insert(0, str(Path(__file__).parent.parent / "skills"))

from confidence_check import ConfidenceChecker


def load_test_cases() -> Dict[str, Any]:
    """Load test cases from JSON file"""
    test_file = Path(__file__).parent / "confidence_test_cases.json"
    with open(test_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def run_single_test(test_case: Dict[str, Any], checker: ConfidenceChecker) -> Dict[str, Any]:
    """
    Run a single test case

    Returns:
        {
            'id': str,
            'expected_confidence': float,
            'actual_confidence': float,
            'expected_action': str,
            'actual_action': str,
            'result': 'pass' | 'fail',
            'checks': List[str],
            'token_overhead': int (estimated)
        }
    """
    context = test_case['context'].copy()

    # Run confidence assessment
    actual_confidence = checker.assess(context)
    actual_action = 'proceed' if actual_confidence >= 0.9 else 'stop'

    # Get check results
    checks = context.get('confidence_checks', [])

    # Determine pass/fail
    expected_action = test_case['expected_action']
    expected_confidence = test_case['expected_confidence']

    # Result is 'pass' if:
    # 1. Action matches (stop vs proceed)
    # 2. Confidence is within ±0.15 of expected
    action_match = (actual_action == expected_action)
    confidence_match = abs(actual_confidence - expected_confidence) <= 0.15

    result = 'pass' if (action_match and confidence_match) else 'fail'

    # Estimate token overhead (rough calculation)
    # - Context: ~50 tokens
    # - Checks: ~20 tokens per check
    # - Total: ~50 + (5 checks * 20) = ~150 tokens
    token_overhead = 50 + len(checks) * 20

    return {
        'id': test_case['id'],
        'category': test_case['category'],
        'scenario': test_case['scenario'],
        'expected_confidence': expected_confidence,
        'actual_confidence': actual_confidence,
        'expected_action': expected_action,
        'actual_action': actual_action,
        'result': result,
        'checks': checks,
        'token_overhead': token_overhead,
        'data_source': test_case['data_source']
    }


def calculate_metrics(results: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calculate precision, recall, false_positive_rate, false_negative_rate

    Definitions:
    - True Positive (TP): expected=stop, actual=stop, confidence < 0.9
    - True Negative (TN): expected=proceed, actual=proceed, confidence >= 0.9
    - False Positive (FP): expected=proceed, actual=stop (incorrectly stopped)
    - False Negative (FN): expected=stop, actual=proceed (incorrectly proceeded)
    """
    tp = sum(1 for r in results if r['expected_action'] == 'stop' and r['actual_action'] == 'stop')
    tn = sum(1 for r in results if r['expected_action'] == 'proceed' and r['actual_action'] == 'proceed')
    fp = sum(1 for r in results if r['expected_action'] == 'proceed' and r['actual_action'] == 'stop')
    fn = sum(1 for r in results if r['expected_action'] == 'stop' and r['actual_action'] == 'proceed')

    # Precision = TP / (TP + FP)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0

    # Recall = TP / (TP + FN)
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0

    # False Positive Rate = FP / (FP + TN)
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0

    # False Negative Rate = FN / (FN + TP)
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0.0

    # Average confidence
    avg_confidence = sum(r['actual_confidence'] for r in results) / len(results)

    # Average token overhead
    avg_token_overhead = sum(r['token_overhead'] for r in results) / len(results)

    return {
        'true_positives': tp,
        'true_negatives': tn,
        'false_positives': fp,
        'false_negatives': fn,
        'precision': round(precision, 3),
        'recall': round(recall, 3),
        'false_positive_rate': round(fpr, 3),
        'false_negative_rate': round(fnr, 3),
        'avg_confidence': round(avg_confidence, 3),
        'avg_token_overhead': round(avg_token_overhead, 1)
    }


def evaluate_success(metrics: Dict[str, float], criteria: Dict[str, float]) -> Dict[str, Any]:
    """
    Evaluate if metrics meet success criteria

    Success Criteria (from JSON):
    - Precision ≥ criteria['precision']
    - Recall ≥ criteria['recall']
    - Avg confidence ≥ criteria['avg_confidence']
    - Token overhead < criteria['token_overhead_max']
    """
    checks = {
        'precision_pass': metrics['precision'] >= criteria['precision'],
        'recall_pass': metrics['recall'] >= criteria['recall'],
        'confidence_pass': metrics['avg_confidence'] >= criteria['avg_confidence'],
        'token_overhead_pass': metrics['avg_token_overhead'] < criteria['token_overhead_max']
    }

    all_pass = all(checks.values())

    return {
        'overall_pass': all_pass,
        'checks': checks,
        'summary': 'PASS ✅' if all_pass else 'FAIL ❌'
    }


def main():
    """Run all confidence check tests"""
    print("🧪 Confidence Check Precision/Recall Test Suite")
    print("=" * 60)

    # Load test cases
    test_data = load_test_cases()
    test_cases = test_data['test_cases']
    criteria = test_data['success_criteria']

    print(f"📊 Loaded {len(test_cases)} test cases")
    print(f"🎯 Success Criteria:")
    print(f"   - Precision ≥ {criteria['precision']}")
    print(f"   - Recall ≥ {criteria['recall']}")
    print(f"   - Avg Confidence ≥ {criteria['avg_confidence']}")
    print(f"   - Token Overhead < {criteria['token_overhead_max']}")
    print()

    # Run tests
    checker = ConfidenceChecker()
    results = []

    for i, test_case in enumerate(test_cases, 1):
        print(f"[{i}/{len(test_cases)}] Running {test_case['id']}: {test_case['scenario']}")
        result = run_single_test(test_case, checker)
        results.append(result)

        status = "✅ PASS" if result['result'] == 'pass' else "❌ FAIL"
        print(f"    → {status} (confidence: {result['actual_confidence']:.2f}, action: {result['actual_action']})")

    print()
    print("📊 Calculating Metrics...")
    metrics = calculate_metrics(results)

    print()
    print("📈 Results:")
    print(f"   - Precision: {metrics['precision']:.3f} (≥ {criteria['precision']} required)")
    print(f"   - Recall: {metrics['recall']:.3f} (≥ {criteria['recall']} required)")
    print(f"   - False Positive Rate: {metrics['false_positive_rate']:.3f}")
    print(f"   - False Negative Rate: {metrics['false_negative_rate']:.3f}")
    print(f"   - Avg Confidence: {metrics['avg_confidence']:.3f} (≥ {criteria['avg_confidence']} required)")
    print(f"   - Avg Token Overhead: {metrics['avg_token_overhead']:.1f} tokens (< {criteria['token_overhead_max']} required)")
    print()

    # Evaluate success
    evaluation = evaluate_success(metrics, criteria)
    print(f"🏆 Overall Result: {evaluation['summary']}")
    print()
    print("Detailed Checks:")
    for check, passed in evaluation['checks'].items():
        status = "✅" if passed else "❌"
        print(f"   {status} {check}")

    # Save results
    output_file = Path(__file__).parent / f"confidence_check_results_{datetime.now().strftime('%Y%m%d')}.json"
    output = {
        'generated': datetime.now().isoformat(),
        'test_suite': test_data['test_suite'],
        'summary': {
            'total_tests': len(test_cases),
            'passed': sum(1 for r in results if r['result'] == 'pass'),
            'failed': sum(1 for r in results if r['result'] == 'fail'),
            **metrics
        },
        'evaluation': evaluation,
        'cases': results
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print()
    print(f"💾 Results saved to: {output_file}")

    # Exit with appropriate code
    sys.exit(0 if evaluation['overall_pass'] else 1)


if __name__ == '__main__':
    main()
