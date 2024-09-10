
# Mandelbrot App in Docker

This guide will walk you through setting up and running a Python Mandelbrot app inside a Docker container, with graphical rendering handled by your local machine's X Server.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Docker
- X11 (X Server) configured on your local machine (explained in detail below)
- (Optional) `xhost` utility for managing X Server access permissions.

### X11 (X Server) Installation and Configuration

If you do not have X11 installed and configured, follow these steps:

1. **For Linux Users**:
    - On most Linux distributions, X11 is installed by default. You can verify if it’s running by typing:
      ```bash
      xclock
      ```
      If the clock window appears, X11 is working.
    - If X11 is not installed, you can install it using your package manager:
      - For Ubuntu/Debian:
        ```bash
        sudo apt-get install xorg
        ```
      - For Fedora:
        ```bash
        sudo dnf install xorg-x11-server-Xorg
        ```

2. **For Mac Users**:
    - MacOS does not come with X11 by default, but you can install XQuartz, which provides X11 on Mac. Download it from:
      - https://www.xquartz.org/
    - After installation, make sure to restart your computer, then launch XQuartz and verify it is running.

3. **For Windows Users**:
    - Windows requires a third-party X Server, such as Xming or VcXsrv:
      - Xming: https://sourceforge.net/projects/xming/
      - VcXsrv: https://sourceforge.net/projects/vcxsrv/
    - After installing, run the X Server before running any graphical applications in Docker.

### Managing X Server Permissions

By default, only authorized clients can connect to the X Server. To allow Docker to access it, you might need to run the following command:

```bash
xhost +local:docker
```

This grants local Docker containers permission to access your display.

If `xhost` shows `LOCAL:` without needing the above command, your Docker containers already have permission to use X11.

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

_Note: All necessary Python dependencies, including `python3-tk`, will be installed in the container via the Dockerfile:_

```dockerfile
RUN apt-get update && apt-get install -y python3-tk &&     pip install --no-cache-dir -r requirements.txt
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

## Troubleshooting

### X Server Permissions

- **Cannot open display**: If you get an error like `Cannot open display`, it means that your Docker container is not allowed to communicate with your X Server. Ensure you have granted permission using:
  ```bash
  xhost +local:docker
  ```

- **Security Considerations**: Allowing local connections (`xhost +local:docker`) gives all local processes, including Docker containers, access to your X Server. If security is a concern, you can restrict access by running:
  ```bash
  xhost -local:docker
  ```
  Or you can give access to only specific users:
  ```bash
  xhost +SI:localuser:your_username
  ```

### Verifying X Server is Running

- **Linux**: You can verify if X11 is working by running a simple graphical app like `xeyes`:
  ```bash
  xeyes
  ```
  If the eyes follow your mouse, X11 is working.

- **Mac (XQuartz)**: Ensure that XQuartz is running, and that you have restarted your system after installation.

- **Windows**: Make sure that Xming or VcXsrv is running, and check the settings to allow local connections.

## Cleanup

To stop the container, simply close the app window or press `Ctrl + C` in the terminal where the container is running.
