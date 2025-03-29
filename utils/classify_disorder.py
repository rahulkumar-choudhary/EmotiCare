import re

def classify_disorder(analysis_text):
    match = re.search(r"Disorder:\s*(.+)", analysis_text)
    if match:
        return match.group(1).strip()
    return "General Emotional Concern"
