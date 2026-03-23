import subprocess
import time

# Path to the Python file you want to run
script_path = "index.py"  # <-- replace with your file

# Time to wait between runs (seconds)
interval_seconds = 5

try:
    while True:
        print("Starting script:", script_path)
        # Run the other script and wait for it to finish
        result = subprocess.run(["python", script_path], capture_output=True, text=True)

        # Print output from the script
        print("Script output:\n", result.stdout)
        if result.stderr:
            print("Script errors:\n", result.stderr)

        # Check exit code
        if result.returncode == 0:
            print("Child script exited normally. Stopping runner.")
            break  # ✅ exit the loop if child exits normally
        else:
            print(f"Child script exited with code {result.returncode}. Restarting in {interval_seconds} seconds...\n")
            time.sleep(interval_seconds)

except KeyboardInterrupt:
    print("Runner stopped manually.")