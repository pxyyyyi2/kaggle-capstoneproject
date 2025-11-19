from ai.groq_client import ask_ai
def generate_reminder(text):
    prompt = f"Turn this into a short reminder message: {text}"
    return ask_ai(prompt)
