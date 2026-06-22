"""
PERSON 3 - User Interface & Results Dashboard
ADHD Gaze Tracking System

This module provides the Tkinter-based UI that:
1. Lets the user start an eye-tracking session (runs Person 1's script)
2. Lets the user analyze the results (using Person 2's analysis functions)
3. Displays the final attention report in a clean dashboard

Folder structure assumed (adjust paths if your repo differs):

ADHD-Gaze-Tracking-System/
├── gaze_tracking/
│   └── PERSON1_gaze_estimation.py   (produces ../gaze_data.csv)
├── analysis/
│   ├── attention_metrics.py
│   ├── attention_score.py
│   ├── csv_converter.py
│   └── sample_gaze_data.py
├── ui/
│   └── main_dashboard.py            <-- this file
└── gaze_data.csv                    (created after a session runs)
"""

import os
import sys
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

# ----------------------------------------------------------------------
# PATH SETUP — make Person 2's analysis module importable from here
# ----------------------------------------------------------------------
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)  # one level up from /ui

ANALYSIS_DIR = os.path.join(PROJECT_ROOT, "analysis")
GAZE_TRACKING_DIR = os.path.join(PROJECT_ROOT, "gaze_tracking")
CSV_PATH = os.path.join(PROJECT_ROOT, "gaze_data.csv")
GAZE_SCRIPT = os.path.join(GAZE_TRACKING_DIR, "PERSON1_gaze_estimation.py")

sys.path.append(ANALYSIS_DIR)

# Import Person 2's functions directly — no code duplication
from csv_converter import convert_person1_csv_to_gaze_data      # noqa: E402
from attention_score import generate_attention_score            # noqa: E402


# ----------------------------------------------------------------------
# COLOR PALETTE
# ----------------------------------------------------------------------
COLOR_BG = "#F5F8FA"
COLOR_PRIMARY = "#0D8A8A"
COLOR_PRIMARY_DARK = "#0A6868"
COLOR_NAVY = "#1B2A4A"
COLOR_WHITE = "#FFFFFF"
COLOR_GRAY = "#64748B"
COLOR_GOOD = "#2E7D32"
COLOR_MODERATE = "#B45309"
COLOR_LOW = "#C0392B"


class ADHDGazeDashboard(tk.Tk):
    """Main application window with a simple screen-switching system."""

    def __init__(self):
        super().__init__()
        self.title("ADHD Gaze Tracking — Attention Dashboard")
        self.geometry("760x560")
        self.configure(bg=COLOR_BG)
        self.resizable(False, False)

        # Container that holds whichever screen is currently active
        self.container = tk.Frame(self, bg=COLOR_BG)
        self.container.pack(fill="both", expand=True)

        self.session_ran = False  # tracks whether a recording session has completed

        self.show_start_screen()

    # ------------------------------------------------------------------
    # SCREEN MANAGEMENT
    # ------------------------------------------------------------------
    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # ------------------------------------------------------------------
    # SCREEN 1 — START SCREEN
    # ------------------------------------------------------------------
    def show_start_screen(self):
        self.clear_container()

        header = tk.Frame(self.container, bg=COLOR_NAVY, height=90)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="ADHD Gaze Tracking System",
            font=("Calibri", 22, "bold"), bg=COLOR_NAVY, fg=COLOR_WHITE
        ).pack(pady=(20, 0))
        tk.Label(
            header, text="Attention Screening Dashboard",
            font=("Calibri", 12), bg=COLOR_NAVY, fg="#A8D8D8"
        ).pack()

        body = tk.Frame(self.container, bg=COLOR_BG)
        body.pack(fill="both", expand=True, padx=40, pady=30)

        tk.Label(
            body, text="Step 1 — Record an Eye-Tracking Session",
            font=("Calibri", 15, "bold"), bg=COLOR_BG, fg=COLOR_NAVY
        ).pack(anchor="w", pady=(10, 5))

        tk.Label(
            body,
            text=("Press the button below to start the webcam.\n"
                  "A separate window will open showing the live camera feed\n"
                  "with gaze detection. Press 'q' in that window to stop\n"
                  "the session whenever you are ready."),
            font=("Calibri", 11), bg=COLOR_BG, fg=COLOR_GRAY, justify="left"
        ).pack(anchor="w", pady=(0, 20))

        start_btn = tk.Button(
            body, text="▶  Start Eye Tracking Session",
            font=("Calibri", 13, "bold"), bg=COLOR_PRIMARY, fg=COLOR_WHITE,
            activebackground=COLOR_PRIMARY_DARK, activeforeground=COLOR_WHITE,
            relief="flat", padx=20, pady=12, cursor="hand2",
            command=self.start_session
        )
        start_btn.pack(anchor="w")

        self.status_label = tk.Label(
            body, text="", font=("Calibri", 11, "italic"),
            bg=COLOR_BG, fg=COLOR_GRAY
        )
        self.status_label.pack(anchor="w", pady=(15, 0))

        tk.Frame(body, bg="#D9E2E8", height=1).pack(fill="x", pady=25)

        tk.Label(
            body, text="Step 2 — Analyze the Recorded Session",
            font=("Calibri", 15, "bold"), bg=COLOR_BG, fg=COLOR_NAVY
        ).pack(anchor="w", pady=(0, 5))

        tk.Label(
            body,
            text="Once a session has been recorded, analyze it to generate\n"
                 "the attention report.",
            font=("Calibri", 11), bg=COLOR_BG, fg=COLOR_GRAY, justify="left"
        ).pack(anchor="w", pady=(0, 15))

        self.analyze_btn = tk.Button(
            body, text="📊  Analyze Results",
            font=("Calibri", 13, "bold"), bg=COLOR_NAVY, fg=COLOR_WHITE,
            activebackground="#13203B", activeforeground=COLOR_WHITE,
            relief="flat", padx=20, pady=12, cursor="hand2",
            command=self.analyze_results
        )
        self.analyze_btn.pack(anchor="w")

        footer = tk.Label(
            self.container,
            text="This tool supports ADHD attention screening — it does not diagnose ADHD.",
            font=("Calibri", 9, "italic"), bg=COLOR_BG, fg=COLOR_GRAY
        )
        footer.pack(side="bottom", pady=10)

    # ------------------------------------------------------------------
    # ACTION — START SESSION (runs Person 1's script as a subprocess)
    # ------------------------------------------------------------------
    def start_session(self):
        if not os.path.exists(GAZE_SCRIPT):
            messagebox.showerror(
                "Script Not Found",
                f"Could not find Person 1's tracking script at:\n{GAZE_SCRIPT}\n\n"
                "Make sure the folder structure matches the project layout."
            )
            return

        self.status_label.config(
            text="Opening camera window... Press 'q' in that window when you are done."
        )
        self.update_idletasks()

        try:
            # Run Person 1's script as a separate process.
            # We wait for it to finish (blocking) since the user controls
            # when it ends by pressing 'q' in the OpenCV window.
            # Delete old CSV before starting a new session
            if os.path.exists(CSV_PATH):
                os.remove(CSV_PATH)

            subprocess.run(
                [sys.executable, GAZE_SCRIPT],
                cwd=PROJECT_ROOT,
                check=True
            )
            self.session_ran = True
            self.status_label.config(
                text="✅ Session complete. Click 'Analyze Results' below.",
                fg=COLOR_GOOD
            )
        except subprocess.CalledProcessError:
            messagebox.showerror(
                "Session Error",
                "The eye-tracking script closed unexpectedly. Please try again."
            )
            self.status_label.config(text="")
        except Exception as e:
            messagebox.showerror("Error", f"Could not start session:\n{e}")
            self.status_label.config(text="")

    # ------------------------------------------------------------------
    # ACTION — ANALYZE RESULTS (uses Person 2's functions directly)
    # ------------------------------------------------------------------
    def analyze_results(self):
        if not os.path.exists(CSV_PATH):
            messagebox.showwarning(
                "No Data Found",
                "No gaze_data.csv file was found yet.\n\n"
                "Please run a tracking session first by clicking "
                "'Start Eye Tracking Session'."
            )
            return

        try:
            gaze_data = convert_person1_csv_to_gaze_data(CSV_PATH)

            if len(gaze_data) < 2:
                messagebox.showwarning(
                    "Not Enough Data",
                    "The recorded session does not contain enough valid "
                    "gaze data to analyze. Please record a longer session."
                )
                return

            results = generate_attention_score(gaze_data)
            self.show_results_screen(results)

        except Exception as e:
            messagebox.showerror("Analysis Error", f"Could not analyze data:\n{e}")

    # ------------------------------------------------------------------
    # SCREEN 2 — RESULTS SCREEN
    # ------------------------------------------------------------------
    def show_results_screen(self, results):
        self.clear_container()

        score = results["attention_score"]
        fixation = results["average_fixation_duration"]
        shifts = results["attention_shifts"]
        stability = results["gaze_stability"]

        # Determine color based on score
        if score >= 75:
            score_color = COLOR_GOOD
        elif score >= 50:
            score_color = COLOR_MODERATE
        else:
            score_color = COLOR_LOW

        header = tk.Frame(self.container, bg=COLOR_NAVY, height=90)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(
            header, text="Attention Analysis Report",
            font=("Calibri", 22, "bold"), bg=COLOR_NAVY, fg=COLOR_WHITE
        ).pack(pady=(25, 0))

        body = tk.Frame(self.container, bg=COLOR_BG)
        body.pack(fill="both", expand=True, padx=40, pady=25)

        # --- Big score circle/card ---
        score_card = tk.Frame(body, bg=COLOR_WHITE, highlightbackground="#D9E2E8",
                               highlightthickness=1)
        score_card.pack(fill="x", pady=(0, 20))

        tk.Label(
            score_card, text="Attention Score",
            font=("Calibri", 13, "bold"), bg=COLOR_WHITE, fg=COLOR_GRAY
        ).pack(pady=(15, 0))
        tk.Label(
            score_card, text=f"{score}/100",
            font=("Cambria", 42, "bold"), bg=COLOR_WHITE, fg=score_color
        ).pack(pady=(0, 15))

        # --- Metric cards row ---
        metrics_frame = tk.Frame(body, bg=COLOR_BG)
        metrics_frame.pack(fill="x", pady=(0, 20))

        self._make_metric_card(
            metrics_frame, "Avg. Fixation Duration",
            f"{fixation} sec", 0
        )
        self._make_metric_card(
            metrics_frame, "Attention Shifts",
            str(shifts), 1
        )
        self._make_metric_card(
            metrics_frame, "Gaze Stability",
            stability, 2
        )

        # --- Disclaimer ---
        disclaimer = tk.Label(
            body,
            text="⚠ This tool supports ADHD attention screening.\nIt does not provide a medical diagnosis.",
            font=("Calibri", 10, "italic"), bg=COLOR_BG, fg=COLOR_GRAY,
            justify="center"
        )
        disclaimer.pack(pady=(10, 20))

        # --- Back button ---
        back_btn = tk.Button(
            body, text="⟵  Back to Start",
            font=("Calibri", 12, "bold"), bg=COLOR_PRIMARY, fg=COLOR_WHITE,
            activebackground=COLOR_PRIMARY_DARK, activeforeground=COLOR_WHITE,
            relief="flat", padx=18, pady=10, cursor="hand2",
            command=self.show_start_screen
        )
        back_btn.pack()

    def _make_metric_card(self, parent, label, value, col):
        card = tk.Frame(parent, bg=COLOR_WHITE, highlightbackground="#D9E2E8",
                         highlightthickness=1, width=200, height=110)
        card.grid(row=0, column=col, padx=10, sticky="nsew")
        card.grid_propagate(False)
        parent.grid_columnconfigure(col, weight=1)

        tk.Label(
            card, text=label, font=("Calibri", 10, "bold"),
            bg=COLOR_WHITE, fg=COLOR_GRAY, wraplength=160, justify="center"
        ).pack(pady=(18, 5))
        tk.Label(
            card, text=value, font=("Cambria", 18, "bold"),
            bg=COLOR_WHITE, fg=COLOR_NAVY
        ).pack()


if __name__ == "__main__":
    app = ADHDGazeDashboard()
    app.mainloop()