import os
import google.generativeai as genai
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path)


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-pro")
print(f"API Key Loaded: {os.getenv('GOOGLE_API_KEY')}")

def gemini_ask(prompt):
    # Use the model to generate content based on the provided prompt
    response = model.generate_content(prompt)
    return response.text
