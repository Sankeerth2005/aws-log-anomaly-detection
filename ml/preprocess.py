import re
from collections import Counter

def extract_features(log_lines):
    features = {
        "total_logs": len(log_lines),
        "error_count": 0,
        "unique_messages": 0
    }

    messages = []

    for line in log_lines:
        if "ERROR" in line:
            features["error_count"] += 1
        msg = re.sub(r"\d+", "", line)
        messages.append(msg)

    features["unique_messages"] = len(set(messages))
    return features
