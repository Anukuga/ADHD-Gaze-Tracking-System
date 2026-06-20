from attention_metrics import (
    count_attention_shifts,
    calculate_average_fixation_duration,
    calculate_gaze_stability,
)


def generate_attention_score(gaze_data):
    """
    Generate a simple attention score from gaze metrics.
    This is not a medical diagnosis. It only supports attention analysis.
    """
    shifts = count_attention_shifts(gaze_data)
    avg_fixation = calculate_average_fixation_duration(gaze_data)
    stability = calculate_gaze_stability(gaze_data)

    score = 100

    score -= shifts * 8

    if avg_fixation < 1.0:
        score -= 15
    elif avg_fixation < 2.0:
        score -= 8

    if stability == "Moderate":
        score -= 10
    elif stability == "Low":
        score -= 20

    score = max(0, min(100, score))

    return {
        "attention_score": score,
        "average_fixation_duration": avg_fixation,
        "attention_shifts": shifts,
        "gaze_stability": stability,
    }


def print_attention_report(results):
    print("\nADHD Attention Analysis Report")
    print("--------------------------------")
    print(f"Attention Score: {results['attention_score']}/100")
    print(f"Average Fixation Duration: {results['average_fixation_duration']} seconds")
    print(f"Attention Shifts Detected: {results['attention_shifts']}")
    print(f"Gaze Stability: {results['gaze_stability']}")
    print("\nNote: This tool supports ADHD screening but does not diagnose ADHD.")