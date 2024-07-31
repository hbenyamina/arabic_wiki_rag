# Use an official Python runtime with CUDA support as a parent image
FROM python:3.9.19-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Install Python
RUN apt-get update && apt-get install -y python3-pip

# Copy the current directory contents into the container at /app
COPY src/ /app

# Install any needed packages specified in requirements.txt
# Copy the current directory contents into the container at /app
COPY src/ /app
# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app

# Create a virtual environment and activate it
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN echo 'export PATH="/venv/bin:$PATH"' >> /etc/profile

# Install any needed packages specified in requirements.txt
RUN pip3 install uv
RUN uv pip install --no-cache-dir -r /app/requirements.txt

# Run app.py when the container launches
CMD ["python3", "app.py"]