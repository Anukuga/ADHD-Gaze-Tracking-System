import math


def distance(point1, point2):
    """Calculate distance between two gaze points."""
    return math.sqrt((point2["x"] - point1["x"]) ** 2 + (point2["y"] - point1["y"]) ** 2)


def count_attention_shifts(gaze_data, threshold=150):
    """
    Count large gaze movements.
    Large movements may suggest distraction or attention shift.
    """
    shifts = 0

    for i in range(1, len(gaze_data)):
        if distance(gaze_data[i - 1], gaze_data[i]) > threshold:
            shifts += 1

    return shifts


def calculate_average_fixation_duration(gaze_data, threshold=80):
    """
    Estimate average fixation duration.
    A fixation is counted when gaze stays within a small distance range.
    """
    if len(gaze_data) < 2:
        return 0

    fixation_durations = []
    start_time = gaze_data[0]["time"]

    for i in range(1, len(gaze_data)):
        movement = distance(gaze_data[i - 1], gaze_data[i])

        if movement > threshold:
            duration = gaze_data[i - 1]["time"] - start_time
            if duration > 0:
                fixation_durations.append(duration)
            start_time = gaze_data[i]["time"]

    final_duration = gaze_data[-1]["time"] - start_time
    if final_duration > 0:
        fixation_durations.append(final_duration)

    if not fixation_durations:
        return 0

    return round(sum(fixation_durations) / len(fixation_durations), 2)


def calculate_gaze_stability(gaze_data):
    """
    Classify gaze stability based on average movement distance.
    """
    if len(gaze_data) < 2:
        return "Unknown"

    total_distance = 0

    for i in range(1, len(gaze_data)):
        total_distance += distance(gaze_data[i - 1], gaze_data[i])

    average_movement = total_distance / (len(gaze_data) - 1)

    if average_movement < 50:
        return "Good"
    elif average_movement < 150:
        return "Moderate"
    else:
        return "Low"