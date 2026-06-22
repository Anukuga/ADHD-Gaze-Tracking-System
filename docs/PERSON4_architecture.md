# System Architecture – ADHD Gaze Tracking System

## Overview

The ADHD Gaze Tracking System is a Python-based prototype that uses a webcam to track a user's face and eye movements, process gaze-related data, calculate attention-related metrics, and display the final results through a simple user interface.

The application follows this workflow:

User → Webcam → Face/Eye Detection → Gaze Tracking → CSV Data Output → Attention Analysis → Attention Score → Results Dashboard

## Main Components

### 1. User Interface Module

The UI module provides the main application window. It allows the user to start a gaze tracking session and view the final analysis results after the session is completed.

Main files:

* `ui/PERSON3_app.py`
* `ui/PERSON3_dashboard.py`

Responsibilities:

* Display Start Session button
* Launch the gaze tracking module
* Trigger analysis after the session
* Show results in a dashboard format

### 2. Gaze Tracking Module

The gaze tracking module accesses the webcam, detects the user's face using MediaPipe Face Mesh, tracks eye landmarks, and estimates gaze direction.

Main files:

* `gaze_tracking/PERSON1_camera.py`
* `gaze_tracking/PERSON1_eye_detection.py`
* `gaze_tracking/PERSON1_gaze_estimation.py`
* `face_mesh.py`
* `camera_test.py`

Responsibilities:

* Open webcam stream
* Detect face and eye landmarks
* Track eye movement
* Save gaze-related data into CSV format

### 3. Attention Analysis Module

The analysis module reads gaze tracking data and calculates attention-related metrics such as fixation duration, attention shifts, gaze stability, and attention score.

Main files:

* `analysis/attention_metrics.py`
* `analysis/attention_score.py`
* `analysis/csv_converter.py`
* `analysis/test_analysis.py`

Responsibilities:

* Read gaze data
* Convert CSV data into usable format
* Calculate attention metrics
* Generate an attention score
* Provide summarized results for the dashboard

### 4. Integration and Documentation Module

The integration layer connects all project components and provides one main entry point to run the application.

Main files:

* `main.py`
* `requirements.txt`
* `README.md`
* `docs/`

Responsibilities:

* Connect UI, gaze tracking, and analysis modules
* Manage project setup instructions
* Document architecture and workflow
* Test compatibility between modules
* Prepare final presentation material

## Final Application Flow

1. The user runs the application using `python main.py`.
2. The UI dashboard opens.
3. The user clicks Start Session.
4. The webcam starts and the gaze tracking module begins processing.
5. MediaPipe Face Mesh detects facial and eye landmarks.
6. Gaze data is recorded and saved into a CSV file.
7. The user ends the session.
8. The analysis module reads the gaze data.
9. Attention metrics are calculated.
10. The dashboard displays the final score and summary.

## Architecture Diagram

```text
+----------------+
|      User      |
+----------------+
        |
        v
+----------------+
|    Webcam      |
+----------------+
        |
        v
+----------------------------+
| Face & Eye Detection       |
| OpenCV + MediaPipe         |
+----------------------------+
        |
        v
+----------------------------+
| Gaze Tracking Module       |
| Eye Position + Direction   |
+----------------------------+
        |
        v
+----------------+
|  CSV Data File |
+----------------+
        |
        v
+----------------------------+
| Attention Analysis Module  |
| Fixation / Shifts / Score  |
+----------------------------+
        |
        v
+----------------------------+
| Results Dashboard          |
| Tkinter UI                 |
+----------------------------+
```

## Technologies Used

* Python
* OpenCV
* MediaPipe Face Mesh
* NumPy
* Pandas
* Tkinter
* Matplotlib

## Integration Notes

During integration testing, the following issues were identified:

* `main.py` was empty and needed to be added as the main project entry point.
* `requirements.txt` was empty and needed the correct dependencies.
* MediaPipe version compatibility was required because newer versions caused issues with the `mp.solutions.face_mesh` API.
* The dashboard initially displayed repeated values because it was reading old CSV data instead of new session data.

## Current MVP Status

The project successfully demonstrates the minimum viable workflow:

Webcam input → face/eye detection → gaze tracking → attention analysis → dashboard results

The system is a prototype and is intended for educational demonstration only. It does not diagnose ADHD.
