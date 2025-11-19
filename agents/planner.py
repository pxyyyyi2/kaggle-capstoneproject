from ai.groq_client import ask_ai
import json

def generate_meal_plan(foods):
    foods_str = foods if isinstance(foods, str) else ', '.join(foods)
    prompt = f"""You are a nutrition assistant. Create a concise, practical meal plan using these foods: {foods_str}
Output a JSON array of items where each item has:
- food (string)
- calories (number)
- protein_g (number)
- carbs_g (number)
- fat_g (number)
- recipes (array of short recipe strings)
Return only the JSON array."""
    out = ask_ai(prompt)
    # Try to parse JSON, if AI returned JSON; otherwise return AI text.
    try:
        return json.loads(out)
    except Exception:
        return out
