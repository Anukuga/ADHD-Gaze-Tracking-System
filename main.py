import subprocess
import sys

if __name__ == "__main__":
    subprocess.run(
        [sys.executable, "ui/PERSON3_app.py"],
        check=True
    )