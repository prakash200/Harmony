# Use a Python base image
# FROM python:3.9-slim-buster

# # Set the working directory
# WORKDIR /app

# # Copy requirements.txt and install dependencies
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# # Copy the rest of the application code
# COPY . .

# # Expose the port your application will listen on
# EXPOSE 8000

# # Command to run the application
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# Using Python base image
FROM python:3.9-buster

# Mapping the working directory
WORKDIR /app

# Copying requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expose the port your application will listen on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]