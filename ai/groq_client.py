import os
from groq import Groq

# Load API key
API_KEY = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=API_KEY)

def ask_ai(prompt: str) -> str:
    """
    Send prompt to Groq API and return text response.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        # Correct response format
        return response.choices[0].message.content

    except Exception as e:
        return f"[AI Error] {e}"
