# core/views.py
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

def home(request):
    documents = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'core/home.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/upload.html', {'form': form})
