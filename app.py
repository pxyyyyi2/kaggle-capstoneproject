from flask import Flask, render_template, request, jsonify, send_file
from ai.groq_client import ask_ai
import io
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/ui")
def ui():
    return render_template("index.html")

@app.route("/")
def home():
    return jsonify({"service": "AI Nutrition Health Guide", "status": "ok"})

@app.route("/agent", methods=["POST"])
def agent():
    prompt = request.json.get("prompt", "")
    reply = ask_ai(prompt)
    return jsonify({"reply": reply})

@app.route("/meal-plan", methods=["POST"])
def meal_plan():
    foods = request.json.get("foods", "")
    reply = ask_ai("Generate meal plan for: " + foods)
    return jsonify({"plan": reply})

@app.route("/research", methods=["POST"])
def research():
    q = request.json.get("query", "")
    reply = ask_ai("Research this nutrition topic: " + q)
    return jsonify({"results": reply})

@app.route("/calories-chart")
def calories_chart():
    foods = request.args.get("foods", "")
    items = [f.strip() for f in foods.split(",")]

    calories = [200, 150, 300][:len(items)]

    fig, ax = plt.subplots()
    ax.bar(items, calories)
    ax.set_title("Calories Chart")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)

    return send_file(img, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
