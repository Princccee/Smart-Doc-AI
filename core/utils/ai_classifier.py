import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize client
client = genai.Client(api_key=api_key)

# Available models: gemini-1.5-pro, gemini-1.5-flash, etc.
MODEL_NAME = "gemini-1.5-flash"

CATEGORIES = ["Invoice", "Legal", "HR", "Technical", "Marketing", "Resume"]

def classify_with_gemini(text):
    if not text.strip():
        return "Unknown"

    prompt = (
        f"Classify the following document into one of the categories: {', '.join(CATEGORIES)}.\n\n"
        f"Document Text:\n{text[:4000]}\n\n"
        f"Reply ONLY with the category name."
    )

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        result = response.text.strip()
        return result if result in CATEGORIES else "Unknown"
    except Exception as e:
        print(f"[Gemini SDK Error] {e}")
        return "Unknown"
