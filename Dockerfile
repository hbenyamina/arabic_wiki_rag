# Use an official Python runtime with CUDA support as a parent image
FROM nvidia/cuda:12.1.0-cudnn8-devel-ubi8

# Set the working directory in the container to /app
WORKDIR /app

# Install Python
RUN apt-get update && apt-get install -y python3-pip

# Copy the current directory contents into the container at /app
COPY src/ /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python3", "app.py"]