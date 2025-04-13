import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python nikto.py <target_url>")
    sys.exit(1)

target_url = sys.argv[1]

try:
    subprocess.run(["wsl", "nikto", "-h", target_url], check=True)
except subprocess.CalledProcessError as e:
    print("Nikto scan failed:", e)
except FileNotFoundError as e:
    print("Failed to run Nikto:", e)
