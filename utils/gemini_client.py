import os
import google.generativeai as genai
from dotenv import load_dotenv

# Explicitly set the path to the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Load the environment variables from the .env file located in the parent directory
load_dotenv(dotenv_path)

# Configure the Gemini API with the API key from the environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-pro")
print(f"API Key Loaded: {os.getenv('GOOGLE_API_KEY')}")

def gemini_ask(prompt):
    # Use the model to generate content based on the provided prompt
    response = model.generate_content(prompt)
    return response.text
