
# Mandelbrot App in Docker

This guide will walk you through setting up and running a Python Mandelbrot app inside a Docker container, with graphical rendering handled by your local machine's X Server.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Docker
- X11 (X Server) configured on your local machine
- Python dependencies for the Mandelbrot app

## Getting Started

### 1. Clone the repository

First, clone the repository containing the Mandelbrot app:

```bash
git clone https://github.com/your-repo/mandelbrot-app.git
cd mandelbrot-app
```

### 2. Build the Docker image

You need to build the Docker image that will contain the Python Mandelbrot app. In the root directory of the project, run the following command:

```bash
docker build -t mandelbrot-image .
```

### 3. Run the Docker container with X11 forwarding

To allow graphical rendering from the Docker container to your local machine, you'll need to set up X11 forwarding.

If your X Server allows local connections (checked using `xhost`), you can run the container without any further permissions needed:

```bash
docker run -it --rm     -e DISPLAY=$DISPLAY     -v /tmp/.X11-unix:/tmp/.X11-unix     mandelbrot-image
```

This command mounts the X11 socket and forwards the display environment variable to allow the Docker container to communicate with your X Server.

#### **What is an X Server?**

An X Server is a graphical windowing system used on Unix and Linux systems. It manages windows, input devices, and display graphics. In this case, the X Server is running on your local machine, and the Docker container uses it to display the Mandelbrot app's graphical output.

### 4. Verify the app is running

Once the container is running, your Mandelbrot app should display a graphical window on your local machine. You can check the logs of the container to ensure there are no errors:

```bash
docker logs <container_id>
```

### 5. Troubleshooting

If you encounter issues with the graphical window not rendering, ensure that:

- Your X Server is running (`xclock` or `xeyes` can be used to check if it works).
- The Docker container has proper permissions to access your X Server (`xhost +local:docker` can be used, if necessary).

## Cleanup

To stop the container, simply close the app window or press `Ctrl + C` in the terminal where the container is running.
