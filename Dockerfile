# Use an official Python runtime with CUDA support as a parent image
FROM python:3.9.19-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Install Python
RUN apt-get update && apt-get install -y python3-pip


RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN echo 'export PATH="/venv/bin:$PATH"' >> /etc/profile

COPY requirements.txt /app



RUN pip3 install uv
RUN uv pip install --no-cache-dir -r /app/requirements.txt

COPY src/ /app
CMD ["python3", "api.py"]