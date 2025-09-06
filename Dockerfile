
# Step 1: Use official Python image
FROM python:3.11-slim

# Step 2: Set environment variables
ENV GEMINI_API_KEY=AIzaSyB9v2CdzM_96oRIvekI3-nMSa17BKMUhs4

# Step 3: Set work directory
WORKDIR /app

# Step 4: Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    pkg-config \
    python3-dev \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Step 5: Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Step 6: Copy project files
COPY . .

# Step 7: Collect static files (optional if using static)
# RUN python manage.py collectstatic --noinput

# Step 8: Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
