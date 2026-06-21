"""
PERSON3_app.py
Entry point for the ADHD Gaze Tracking UI.
Run this file to launch the application.
"""

from PERSON3_dashboard import ADHDGazeDashboard

if __name__ == "__main__":
    app = ADHDGazeDashboard()
    app.mainloop()