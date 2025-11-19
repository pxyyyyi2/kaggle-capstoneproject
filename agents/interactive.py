from ai.groq_client import ask_ai
def interactive_chat(user_text):
    if not user_text or not str(user_text).strip():
        return "Which nutrition topic do you want? (meal plan / recipes / calories / research)"
    prompt = f"You are a friendly nutrition assistant. Answer succinctly: {user_text}"
    return ask_ai(prompt)
