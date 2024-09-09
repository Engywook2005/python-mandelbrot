import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Force matplotlib to use the TkAgg backend
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Create a colormap for ROYGBIV
colors = [(1, 0, 0),  # Red
          (1, 0.5, 0),  # Orange
          (1, 1, 0),  # Yellow
          (0, 1, 0),  # Green
          (0, 0, 1),  # Blue
          (0.29, 0, 0.51),  # Indigo
          (0.56, 0, 1)]  # Violet
cmap = LinearSegmentedColormap.from_list('ROYGBIV', colors, N=256)

# Mandelbrot function
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Create Mandelbrot image
def create_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return n3

# Interactive plot settings
class MandelbrotPlotter:
    def __init__(self):
        self.xmin, self.xmax, self.ymin, self.ymax = -2.0, 1.0, -1.5, 1.5
        self.width, self.height = 800, 800
        self.max_iter = 256
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Click to zoom Mandelbrot set")
        self.plot()

        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)

    def plot(self):
        self.ax.clear()
        mandelbrot_set = create_mandelbrot(self.xmin, self.xmax, self.ymin, self.ymax, self.width, self.height, self.max_iter)
        self.ax.imshow(mandelbrot_set.T, extent=[self.xmin, self.xmax, self.ymin, self.ymax], cmap=cmap, origin='lower')
        self.fig.canvas.draw()

    def onclick(self, event):
        if event.inaxes:
            # Zoom on the clicked point
            zoom_factor = 0.5
            x_range = (self.xmax - self.xmin) * zoom_factor
            y_range = (self.ymax - self.ymin) * zoom_factor

            self.xmin = event.xdata - x_range / 2
            self.xmax = event.xdata + x_range / 2
            self.ymin = event.ydata - y_range / 2
            self.ymax = event.ydata + y_range / 2

            self.plot()

# Run the interactive plot
mandelbrot_plotter = MandelbrotPlotter()
plt.show()  # This should now open an interactive window
