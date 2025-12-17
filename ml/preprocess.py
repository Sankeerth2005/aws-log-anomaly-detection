import re
from datetime import datetime
from collections import defaultdict

LOG_PATTERN = re.compile(
    r"(?P<timestamp>[\d-]+\s[\d:]+)\s(?P<level>\w+)\s(?P<message>.*)"
)

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    return {
        "timestamp": datetime.strptime(match.group("timestamp"), "%Y-%m-%d %H:%M:%S"),
        "level": match.group("level"),
        "message": match.group("message"),
    }

def load_logs(file_path):
    parsed = []
    with open(file_path, "r") as f:
        for line in f:
            result = parse_log_line(line.strip())
            if result:
                parsed.append(result)
    return parsed

def window_logs(logs, window_minutes=5):
    windows = defaultdict(list)
    for log in logs:
        window_key = log["timestamp"].replace(
            minute=(log["timestamp"].minute // window_minutes) * window_minutes,
            second=0
        )
        windows[window_key].append(log)
    return windows

def extract_features(log_window):
    total = len(log_window)
    errors = sum(1 for l in log_window if l["level"] == "ERROR")
    unique_msgs = len(set(l["message"] for l in log_window))

    return [total, errors, unique_msgs]
