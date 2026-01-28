import subprocess
import re

def measure_latency(ip):
    result = subprocess.run(
        ["ping", "-c", "3", ip],
        capture_output=True,
        text=True
    )

    match = re.search(r'time=([\d.]+) ms', result.stdout)
    return float(match.group(1)) if match else None

