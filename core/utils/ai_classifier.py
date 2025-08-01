import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize client
client = genai.Client(api_key=api_key)


MODEL_NAME = "gemini-1.5-flash"

CATEGORIES = [
    "Invoice", "Legal", "HR", "Technical", "Resume", "Report",
    "Presentation", "Financial Statement", "Marketing", "Email", "Policy Document",
    "Meeting Minutes", "Contract", "Product Manual", "Other"
]


def classify_with_gemini(text):
    if not text.strip():
        return "Unknown"

    prompt = (
        f"You are a document classification assistant.\n"
        f"Given the content of a document, your job is to classify it into one of the following categories:\n"
        f"{', '.join(CATEGORIES)}.\n\n"
        f"---\n"
        f"Document Content:\n{text[:4000]}\n"
        f"---\n\n"
        f"Reply ONLY with one category name from the list above. Do not add any explanation or extra words."
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
