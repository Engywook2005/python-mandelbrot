# Use the latest official Python image
FROM python:3 AS BASE

# Set the working directory inside the container
WORKDIR /usr/src/app

# Define the volume for the working directory
VOLUME ["/usr/src/app"]

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to keep the container runnnig.
CMD ["sh", "-c", "python ./hello-world.py && tail -f /dev/null"]

