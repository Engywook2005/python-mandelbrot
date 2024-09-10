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

# Install required packages, including python3-tk for Tkinter and x11-apps for testing X11
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the Python Mandelbrot app. tail -f /dev/null keeps the container alive.
CMD ["sh", "-c", "python mandelbrot.py && tail -f /dev/null"]

