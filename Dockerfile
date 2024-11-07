# Dockerfile
FROM python:3.9-slim

# Install the qrcode library
RUN pip install qrcode[pil]

# Copy the script into the container
COPY generate_qr.py /app/generate_qr.py

# Set the working directory
WORKDIR /app

# Run the script by default
CMD ["python", "generate_qr.py"]
