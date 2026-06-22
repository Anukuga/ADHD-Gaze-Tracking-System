# Presentation Notes – ADHD Gaze Tracking System

## Slide 1: Title

ADHD Gaze Tracking System

Presented by: Team Members
Course Project 3

## Slide 2: Problem Statement

ADHD is often associated with attention difficulties and frequent distractions. Eye movement and gaze behavior can provide useful signals for estimating attention patterns.

The goal of this project is to build a simple prototype that uses webcam-based gaze tracking to generate attention-related metrics.

Important note: This system is not a medical diagnostic tool. It is only a prototype for demonstrating gaze tracking and attention analysis.

## Slide 3: Project Goal

The goal of the project is to create a minimum viable product that demonstrates the following workflow:

User → Webcam → Eye Detection → Gaze Tracking → Attention Analysis → Attention Score → Results Dashboard

The application should allow a user to start a tracking session, record gaze-related data, analyze attention behavior, and display the final results.

## Slide 4: Technologies Used

The project uses the following technologies:

* Python for the main application logic
* OpenCV for webcam access and image processing
* MediaPipe Face Mesh for face and eye landmark detection
* NumPy and Pandas for data processing
* Tkinter for the graphical user interface
* Matplotlib for optional visualization

## Slide 5: System Architecture

The system is divided into four main modules:

1. Gaze Tracking Module
2. Attention Analysis Module
3. User Interface Module
4. Integration and Documentation Module

The UI launches the gaze tracking session. The gaze tracking module records gaze data into a CSV file. The analysis module processes the CSV file and calculates attention metrics. The dashboard then displays the final results.

## Slide 6: Gaze Tracking Module

The gaze tracking module accesses the webcam and uses MediaPipe Face Mesh to detect facial landmarks.

It focuses on eye landmarks to estimate the user's gaze position and gaze direction.

The output of this module is gaze-related data stored in CSV format.

## Slide 7: Attention Analysis Module

The attention analysis module processes the gaze data collected during the session.

It calculates:

* Average fixation duration
* Attention shifts
* Gaze stability
* Attention score

These values are used to summarize the user's attention behavior during the session.

## Slide 8: User Interface and Dashboard

The UI provides a simple way to interact with the application.

Main UI functions:

* Start gaze tracking session
* Stop or finish the session
* Analyze collected data
* Display attention score and metrics

The dashboard makes the results easier for the user or clinician to understand.

## Slide 9: Integration Work

The integration work focused on connecting the different team modules into one working application.

Main integration tasks:

* Created the main application entry point
* Tested gaze tracking, analysis, and UI modules
* Fixed dependency and compatibility issues
* Added project requirements
* Verified the final workflow
* Updated documentation and presentation material

## Slide 10: Testing

The following tests were performed:

* Webcam access test
* Face Mesh landmark detection test
* Gaze tracking session test
* Attention analysis test using gaze data
* UI dashboard test
* Full application test using `python main.py`

The project successfully opens the webcam, tracks facial landmarks, runs the UI, and displays final attention results.

## Slide 11: Team Contributions

Person 1: Gaze Tracking and Camera Module

* Webcam access
* Face and eye landmark detection
* Gaze estimation

Person 2: Attention Analysis and ADHD Metrics

* Gaze data processing
* Attention score calculation
* Fixation and stability metrics

Person 3: User Interface and Dashboard

* Tkinter application interface
* Start session controls
* Results dashboard

Person 4: Integration, GitHub, and Documentation

* Combined modules into one application
* Added project setup files
* Tested integration
* Updated documentation
* Prepared presentation notes

## Slide 12: Limitations and Future Improvements

Current limitations:

* The system is a prototype
* Accuracy depends on webcam quality and lighting
* The attention score is based on a simplified algorithm
* It is not clinically validated
* It does not diagnose ADHD

Future improvements:

* Improve gaze estimation accuracy
* Add real-time graphs
* Store session history
* Add machine learning-based attention classification
* Improve UI design
* Validate results with larger datasets

## Slide 13: Conclusion

The project successfully demonstrates a working ADHD gaze tracking prototype.

It combines webcam-based face detection, gaze tracking, attention analysis, and a results dashboard into one application.

The final MVP shows how gaze behavior can be used to estimate attention-related metrics in a simple and understandable way.
