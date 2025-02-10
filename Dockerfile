FROM python:slim as python

# Set the working directory

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app

# Install any needed packages specified in requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container

EXPOSE 80

# Define environment variable

ENV NAME World

# Run app.py when the container launches

CMD ["python", "main.py"]

# Build the image

# docker build -t webpydocker .

# Run the image

# docker run -p 4000:80 webpydocker
