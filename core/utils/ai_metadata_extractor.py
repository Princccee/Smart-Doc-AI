import os
import re
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-1.5-flash"

def extract_metadata_with_gemini(text):
    if not text.strip():
        return {}

    prompt = (
        "You are an AI assistant that extracts structured metadata from documents.\n"
        "From the given document text, extract the following metadata as a JSON object:\n\n"
        "- Person: [List of people mentioned]\n"
        "- Organization: [List of organizations]\n"
        "- Date: [All dates mentioned]\n"
        "- Location: [Countries, cities, addresses]\n"
        "- Money: [Currency amounts]\n"
        "- Email: [Email addresses, if any]\n"
        "- Phone: [Phone numbers, if any]\n\n"
        "Only return valid JSON.\n"
        f"\n---\nDocument Text:\n{text[:4000]}\n---"
    )

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        raw_output = response.text.strip()
        # print("=== Gemini RAW Output ===")
        # print(raw_output)

        cleaned = re.sub(r"^```(?:json)?\s*", "", raw_output)
        cleaned = re.sub(r"\s*```$", "", cleaned)

        # Use eval() or json.loads depending on format safety
        return json.loads(cleaned)
    except Exception as e:
        print(f"[Gemini Metadata Error] {e}")
        return {}
