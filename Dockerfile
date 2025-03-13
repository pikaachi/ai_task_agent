# Use official Python image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Install system dependencies (for some Python packages)
RUN apt-get update && apt-get install -y gcc g++ build-essential

# Copy the project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI runs on
EXPOSE 8000

# Run the API using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
