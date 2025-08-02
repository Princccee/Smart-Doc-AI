# core/views.py
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from .utils.extract_text import extract_text_from_file
from .utils.ai_classifier import classify_with_gemini
from .utils.ai_metadata_extractor import extract_metadata_with_gemini
import shutil
import os
from django.conf import settings

def home(request):
    documents = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'core/home.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.save()
            file_path = doc.file.path

            # Extract text from the uploaded file
            extracted = extract_text_from_file(file_path)
            doc.extracted_text = extracted

            # Classify using Gemini
            predicted = classify_with_gemini(extracted)
            doc.predicted_label = predicted

            # Extract metadata entities
            metadata = extract_metadata_with_gemini(extracted)
            doc.metadata = metadata

            print(f"[Document Processed] {doc.file.name} - Predicted: {predicted}, Metadata: {metadata}")

            # Move file to category folder
            if predicted and predicted != "Unknown":
                target_dir = os.path.join(settings.MEDIA_ROOT, 'documents', predicted)
                os.makedirs(target_dir, exist_ok=True)
                new_path = os.path.join(target_dir, os.path.basename(doc.file.name))
                shutil.move(file_path, new_path)
                doc.file.name = f'documents/{predicted}/{os.path.basename(doc.file.name)}'

            doc.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/upload.html', {'form': form})
