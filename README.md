# ADHD-Gaze-Tracking-System

## Project Overview

The ADHD Gaze Tracking System is an AI-assisted healthcare application designed to support objective ADHD screening using webcam-based eye tracking and attention analysis.

Traditional ADHD assessments often rely on subjective questionnaires, clinical interviews, and behavioral observations. This project explores the use of digital biomarkers, specifically gaze behavior, to provide additional objective insights into attention patterns.

The system captures eye movement data through a standard camera, analyzes attention-related behaviors such as fixation duration, attention shifts, and gaze stability, and presents the results through a clinician-friendly dashboard.

> Note: This system is intended as a screening and support tool and does not provide a medical diagnosis of ADHD.

---

# System Workflow

```
User
 ↓
Camera & Gaze Tracking Module
 ↓
Eye Movement Data (x, y coordinates, timestamps)
 ↓
Attention Analysis Module
 ↓
ADHD Attention Metrics & Score
 ↓
User Interface / Clinical Dashboard
 ↓
Healthcare Professional
```

---

# Project Architecture

The project follows a modular architecture where each component is developed independently and integrated into a complete system.

## 1. Gaze Tracking Module (Person 1)

Responsible for capturing and processing eye movement data.

Functions:
- Access webcam or camera feed
- Detect face and eye landmarks
- Estimate gaze direction
- Generate structured gaze data containing:
  - Timestamp
  - X-axis eye position
  - Y-axis eye position
  - Additional eye metrics (optional)

Folder:
```
gaze_tracking/
```

---

## 2. Attention Analysis Module (Person 2)

Responsible for converting raw gaze data into meaningful ADHD-related attention metrics.

Implemented features:
- Calculation of fixation duration
- Detection of attention shifts
- Evaluation of gaze stability
- Generation of an attention score
- Creation of a readable attention analysis report

Current files:

```
analysis/
├── sample_gaze_data.py       # Simulated gaze data for testing
├── attention_metrics.py      # Gaze metric calculations
├── attention_score.py        # ADHD attention scoring system
└── test_analysis.py          # Module testing
```

Example output:

```
ADHD Attention Analysis Report

Attention Score: 33/100
Average Fixation Duration: 0.62 seconds
Attention Shifts Detected: 4
Gaze Stability: Low
```

---

## 3. User Interface & Dashboard Module (Person 3)

Responsible for displaying the results in a simple and understandable format.

Functions:
- Display attention scores
- Visualize gaze patterns
- Present assessment results
- Provide a user-friendly interface for clinicians and users

Folder:
```
ui/
```

---

## 4. Documentation & Integration Module (Muhammad Ahmed Shahab)

Responsible for connecting project components and maintaining documentation.

Functions:
- System integration
- Testing the complete workflow
- Managing documentation
- Preparing project presentation materials

Folder:
```
docs/
```

---

# Technologies

The project may use the following technologies:

### Programming & AI
- Python
- Machine Learning algorithms
- Data analysis techniques

### Computer Vision
- OpenCV
- MediaPipe
- Webcam-based gaze estimation

### Backend & Data Storage
- Flask / FastAPI
- PostgreSQL / MongoDB

### User Interface
- React
- Web dashboard technologies

---

# Team Responsibilities

| Team Member | Role |
|------------|------|
| Person 1 | Gaze Tracking & Camera Module |
| Person 2 | Attention Analysis & ADHD Metrics |
| Person 3 | User Interface & Results Dashboard |
| Muhammad Ahmed Shahab | Documentation, Integration & Testing |

---

# Current Project Status

- [x] Repository created
- [x] System architecture designed
- [x] Project folders organized
- [x] Attention analysis prototype completed
- [x] Gaze tracking implementation
- [x] UI dashboard implementation
- [x] Full system integration
- [x] Testing with real gaze data

---

## How to Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/Anukuga/ADHD-Gaze-Tracking-System.git
cd ADHD-Gaze-Tracking-System
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the Application

```bash
python main.py
```

### Application Workflow

1. Launch the application using `python main.py`.
2. Click **Start Session**.
3. The webcam window will open and begin gaze tracking.
4. Complete the gaze tracking session.
5. Press **q** to close the webcam window and end the session.
6. Click **Analyze Results**.
7. The dashboard will display the attention score and attention metrics.

### Requirements

* Python 3.10 or newer
* Webcam
* Windows operating system (recommended)

---

# Future Improvements

Future versions of the system may include:
- Real-time webcam processing
- Machine learning-based ADHD classification
- Pupil size analysis (pupillometry)
- Blink frequency analysis
- Long-term attention monitoring
- Improved clinical reporting

---

# References

This project is inspired by research on eye tracking, digital biomarkers, and AI-assisted ADHD screening, including:

- Elbaum, T., Braw, Y., Lev, A., & Rassovsky, Y. (2020). *Attention-deficit/hyperactivity disorder (ADHD): Integrating the MOXO-dCPT with an eye tracker enhances diagnostic precision*. Sensors, 20(9), 2448.

- Yoo, J. H., Kang, C., Lim, J. S., Wang, B., Choi, C.-H., Hwang, H., Han, D. H., Kim, H., Cheon, H., & Kim, J.-W. (2024). *Development of an innovative approach using portable eye tracking to assist ADHD screening: A machine learning study*. Frontiers in Psychiatry, 15.

- Vidhya, V., & Faria, D. R. (2025). *Real-time gaze estimation using webcam-based CNN models for human–computer interactions*. Computers, 14(2), 57.

---

## Repository Owner

Created and initialized as part of the Programming Application group project.
