FROM python:3.9-slim

WORKDIR /app

# Copy the preprocessing script
COPY preprocess.py preprocess.py

# No dependencies to install
COPY requirements.txt requirements.txt

# Set the entrypoint to run the preprocessing script
ENTRYPOINT ["python", "preprocess.py"]
