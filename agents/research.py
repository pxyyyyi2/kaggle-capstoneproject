from ai.groq_client import ask_ai
def run_research(query):
    prompt = f"""Summarize reliable nutrition information about: {query}. Provide 3 bullet points and one short recommendation."""
    return ask_ai(prompt)
