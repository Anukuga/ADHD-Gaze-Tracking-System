import os
from sample_gaze_data import sample_gaze_data
from attention_score import generate_attention_score, print_attention_report
from csv_converter import convert_person1_csv_to_gaze_data


csv_path = "../gaze_data.csv"

if os.path.exists(csv_path):
    print("Using Person 1 gaze_data.csv file...")
    gaze_data = convert_person1_csv_to_gaze_data(csv_path)
else:
    print("Using sample gaze data...")
    gaze_data = sample_gaze_data

results = generate_attention_score(gaze_data)
print_attention_report(results)