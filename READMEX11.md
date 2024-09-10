# Mandelbrot Python in Docker with X11 Forwarding

## Overview
This project runs a Mandelbrot generator Python script inside a Docker container with X11 forwarding to display the output on the host machine using XQuartz on macOS.

### Prerequisites
- Docker installed on your system
- XQuartz installed and running on macOS
- socat (if needed for troubleshooting)

### Setup Steps

1. Ensure XQuartz is Running
   Start XQuartz with the following command:
   
   `open -a XQuartz`

2. Allow Connections to XQuartz
   Temporarily disable access control for troubleshooting purposes by running:
   
   `xhost +`
   
   For a more secure setup (after troubleshooting), you can allow local connections only:
   
   `xhost +local:`

3. Set the DISPLAY Environment Variable
   On your host, check the DISPLAY variable:
   
   `echo $DISPLAY`
   
   It should be something like `localhost:0`. If it’s not set, run:
   
   `export DISPLAY=:0`

4. Find Your Local IP Address
   Run this command to get your local network IP address:
   
   `ifconfig en0 | grep inet | grep -v inet6`
   
   The result will be something like `10.0.0.177`. Use this IP for setting up Docker.

5. Build the Docker Image
   To build the Docker image with your updated Python script:
   
   `docker build --no-cache -t mandelbrot-image .`

6. Run the Docker Container with X11 Forwarding
   Use your local IP address to ensure Docker can connect to XQuartz. Run:
   
   `docker run -it --rm -e DISPLAY=10.0.0.177:0 -v /tmp/.X11-unix:/tmp/.X11-unix mandelbrot-image`

7. Test X11 Applications in Docker
   Inside the Docker container, you can test X11 forwarding with:
   
   `xeyes`
   
   Or run the Mandelbrot Python script:
   
   `python3 mandelbrot.py`

### Troubleshooting

1. XQuartz Display Not Connecting
   - If you encounter `cannot open display localhost:0`, try using your local IP address as the DISPLAY variable when running the Docker container.

2. Check XQuartz Logs
   - Open the XQuartz terminal (`Applications > Terminal` in XQuartz) to monitor logs for any errors.

3. socat for Port Forwarding (Optional)
   - If there are still issues with X11 forwarding, you can install and use `socat` to forward X11 traffic:
   
     `brew install socat`
     
     `socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:"$DISPLAY"`
     
     Then run the Docker container as usual.

### Final Solution
The issue was resolved by setting the DISPLAY variable in the Docker container to the local IP address of the host machine, like this:
   
   `docker run -it --rm -e DISPLAY=10.0.0.177:0 -v /tmp/.X11-unix:/tmp/.X11-unix mandelbrot-image`

This ensures that Docker can connect to XQuartz and display graphical applications from within the container.

