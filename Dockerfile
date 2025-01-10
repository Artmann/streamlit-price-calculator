# Use official Python image as the base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt (if you have one) and app.py to the container
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit uses
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.headless", "true", "--server.port", "8501", "--server.address", "0.0.0.0", "--logger.level=debug", "--server.enableCORS", "false"]