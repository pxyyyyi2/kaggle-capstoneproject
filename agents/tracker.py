from ai.groq_client import ask_ai
import os, json

DB = os.path.join(os.getcwd(), 'data_logs.json')

def add_log_entry(text):
    entry = {'text': text}
    # append to a simple file
    try:
        data = json.load(open(DB)) if os.path.exists(DB) else []
    except Exception:
        data = []
    data.append(entry)
    json.dump(data, open(DB, 'w'), indent=2)
    # let AI provide quick feedback
    return ask_ai(f"Interpret this health log entry and give a short supportive reply: {text}")
