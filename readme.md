# 📄 Smart Document Tagger & Classifier 

A full-stack intelligent document management system that automatically:
- Extract text from uploaded documents (`.pdf` / `.txt`)
- Classify documents into predefined enterprise categories
- Move files to category-specific folders
- Display classification results and extracted text in a web dashboard

> 🚀 Built using Django + Gemini API + PyMuPDF. Designed for real-world AI/ML applications in Enterprise Information Management.

---

## ✨ Features

✅ Upload `.pdf` or `.txt` documents  
✅ Automatically extract text using PyMuPDF  
✅ Classify document using **Gemini (Google AI)** with zero training  
✅ Dynamically store predicted label (e.g., `Invoice`, `HR`, `Legal`, `Resume`, etc.)  
✅ Auto-organize files into folders based on their classification  
✅ Minimal, functional web UI using Django templates  
✅ Scalable structure: each phase builds toward a production-grade AI pipeline  

---

## 🧠 Document Categories

Currently supported categories:
- `Invoice`
- `Legal`
- `HR`
- `Technical`
- `Resume`
- `Report`
- `Marketing`
- `Financial Statement`
- `Email`
- `Policy Document`
- `Meeting Minutes`
- `Presentation`
- `Contract`
- `Product Manual`
- `Other` (fallback)

---

## ⚙️ Tech Stack

| Layer      | Tech Used |
|------------|-----------|
| Backend    | Django 5.2, Python 3.10+ |
| AI/NLP     | Google Gemini Pro (via `google-genai` SDK), PyMuPDF |
| Storage    | Local filesystem (Django `MEDIA_ROOT`) |
| Frontend   | Django Templates (HTML/CSS), Bootstrap (optional) |
| Deployment | Dev: runserver; Prod: WSGI/ASGI |

---

## 🧪 How It Works

1. User uploads a `.pdf` or `.txt` file through the web form  
2. System extracts raw text using PyMuPDF  
3. The extracted text is passed to **Gemini Pro (via API)**  
4. Gemini returns a **category label** based on the content  
5. The file is **moved to a subdirectory** for that category (e.g., `documents/HR/`)  
6. All document data is saved and displayed in the dashboard  

---

## 🛠️ Local Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/smart-doc-ai.git
cd smart-doc-ai
