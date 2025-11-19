from ai.groq_client import ask_ai
def evaluate_nutrition(foods):
    prompt = f"Evaluate these foods and give calories estimate + short advice: {foods}"
    return ask_ai(prompt)
