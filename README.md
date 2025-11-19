🥗 AI Nutrition + Health Guide

A smart AI-powered meal planner, nutrition analyzer, calorie calculator, recipe generator, and daily health assistant — built using Flask + Groq Llama 3.3 + HTML/CSS/JS.

This project provides:
✅ Smart AI meal planning
✅ Nutrition scoring
✅ Ingredient-based recipe generation
✅ Chat-style assistant UI
✅ Daily food log
✅ Calorie chart visualization
✅ Fast backend powered by Groq API

🚀 Features
🔮 AI Chat Assistant

Ask anything health or nutrition related:

“Generate a meal plan for chicken, rice, salad”

“How many calories in 1 banana?”

“Make a high-protein diet plan for weight gain.”

🍽️ Smart Meal Planner

Enter foods like:

chicken, rice, salad


And AI generates:

Total calories

Protein / carbs breakdown

Portions

Breakfast / lunch / dinner plans

📊 Calorie Chart Generator

Shows calorie distribution in a bar chart generated with matplotlib.

🔍 Research Tool

Ask health questions, like:

“Nutrition for muscle gain”

“Is rice good for weight loss?”

📝 Daily Log

Track your daily eating/water/progress with a log system.

🏗️ Tech Stack
Component	Technology
Backend	Python Flask
AI Model	Groq – Llama-3.3-70B-Versatile
UI	HTML + CSS + Vanilla JS
Charts	Matplotlib
API Calls	Groq Python SDK
📁 Project Structure
full_groq_project/
│── app.py
│── requirements.txt
│── README.md
│
├── ai/
│   └── groq_client.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js

🔧 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/pxyyyyi2/kaggle-capstoneproject
cd kaggle-capstoneproject

2️⃣ Create virtual environment
python -m venv .venv

3️⃣ Activate environment

Windows

.\.venv\Scripts\activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Add Groq API Key

Set your key:

setx GROQ_API_KEY "your_api_key_here"


Restart terminal after this.

▶️ Run the Project
python app.py


Then open:
👉 http://127.0.0.1:5000/ui

🧪 Example Prompts

Try these:

💡 Generate a day meal plan:

Generate a healthy meal plan for the day using chicken, rice, salad.


💡 Recipe generator:

Create a recipe using only chicken and rice.


💡 Nutrition research:

What is the best nutrition plan for muscle gain?


💡 Calorie estimate:

How many calories in 100g rice?
