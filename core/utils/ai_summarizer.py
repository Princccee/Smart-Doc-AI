import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-1.5-flash"

def summarize_text_with_gemini(text):
    if not text.strip():
        return ""

    prompt = (
        "Summarize the following document in 3-5 lines. "
        "Highlight the key points and intent of the document. "
        "Use clear, human-readable language:\n\n"
        f"{text[:4000]}"
    )

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini Summarizer Error] {e}")
        return ""
