# Use official slim Python image
FROM python:3.10-slim

# Install system packages including poppler
RUN apt-get update && apt-get install -y \
    poppler-utils \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit uses port 8501
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "ats.py", "--server.port=8501", "--server.address=0.0.0.0"]
