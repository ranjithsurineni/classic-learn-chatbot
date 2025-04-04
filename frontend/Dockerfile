# Use official Python base image
FROM python:3.9

# Set working directory
WORKDIR /frontend

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "main.py"]
