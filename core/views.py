# core/views.py
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from .utils.extract_text import extract_text_from_file

def home(request):
    documents = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'core/home.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            file_path = request.FILES['file']
            doc.save()  # Save to generate path

            full_path = doc.file.path  # Absolute path to saved file
            extracted = extract_text_from_file(full_path)
            doc.extracted_text = extracted
            doc.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/upload.html', {'form': form})
