import csv


def convert_person1_csv_to_gaze_data(csv_file_path):
    """
    Converts Person 1's gaze_data.csv output into the format
    required by the attention analysis module.
    """

    gaze_data = []

    with open(csv_file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            left_x = int(row["left_eye_x"])
            left_y = int(row["left_eye_y"])
            right_x = int(row["right_eye_x"])
            right_y = int(row["right_eye_y"])

            # Skip frames where eyes were not detected
            if left_x == 0 or right_x == 0:
                continue

            avg_x = (left_x + right_x) / 2
            avg_y = (left_y + right_y) / 2

            gaze_data.append({
                "time": float(row["timestamp"]),
                "x": avg_x,
                "y": avg_y
            })

    return gaze_data