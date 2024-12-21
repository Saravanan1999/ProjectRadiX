FROM python:3.9-slim

WORKDIR /app

# Copy the training script
COPY train.py train.py

# No dependencies to install
COPY requirements.txt requirements.txt

# Set the entrypoint to run the training script
ENTRYPOINT ["python", "train.py"]
