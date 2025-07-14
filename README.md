# Smart Assistant for Research Summarization 🧠📘

A GenAI-powered assistant that reads, understands, and quizzes users on long documents like research papers and reports using Google's Gemini API.

## Features

- 📄 Upload PDF or TXT files
- 🧠 Auto-summarization (≤150 words)
- 🔎 Ask Anything mode (comprehension Q&A)
- 🤔 Challenge Me mode (logic-based quizzes)
- 📌 Document-anchored justifications
- Local web app using Streamlit

## Setup Instructions

```bash
git clone https://github.com/6merge/ez.git
cd ez
pip install -r requirements.txt

# Set your Gemini API key
echo "GOOGLE_API_KEY=your_key_here" > .env

# Run the app
streamlit run app.py


Developed by Mayank Raj Singh (6merge)
