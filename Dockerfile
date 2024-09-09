# Use the latest official Python image
FROM python:3 AS BASE

# Set the working directory inside the container
WORKDIR /usr/src/app

# Define the volume for the working directory
VOLUME ["/usr/src/app"]

# Copy the Python script into the container
COPY mandelbrot.py /usr/src/app/

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the required Python libraries
RUN apt-get update && apt-get install -y python3-tk && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

RUN apt-get update && apt-get install -y x11-apps

# Command to keep the container runnnig.
CMD ["sh", "-c", "python mandelbrot.py && tail -f /dev/null"]

