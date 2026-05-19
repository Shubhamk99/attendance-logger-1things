import subprocess
import time
import platform

# Path to the Python file you want to run
script_path = "index.py"  # <-- replace with your file

# Time to wait between runs (seconds)
interval_seconds = 5
PYTHON = "python" if platform.system() == "Windows" else "python3"
print(PYTHON)

try:
    while True:
        print("Starting script:", script_path)
        # Run the other script and wait for it to finish
        result = subprocess.Popen(
            [PYTHON, "-u", script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        # Print output in real time
        for line in result.stdout:
            print(line, end="")

        # Wait for process to finish
        result.wait()

        # Check exit code
        if result.returncode == 0:
            print("Child script exited normally. Stopping runner.")
            break  # ✅ exit the loop if child exits normally
        else:
            print(f"Child script exited with code {result.returncode}. Restarting in {interval_seconds} seconds...\n")
            time.sleep(interval_seconds)

except KeyboardInterrupt:
    print("Runner stopped manually.")