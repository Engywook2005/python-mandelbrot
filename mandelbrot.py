import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

import numpy as np
import matplotlib.pyplot as plt

class MandelbrotPlotter:
    def __init__(self):
        # Setup the plot
        self.fig, self.ax = plt.subplots()

    def mandelbrot(self, c, max_iter):
        z = 0
        n = 0
        while abs(z) <= 2 and n < max_iter:
            z = z*z + c
            n += 1
        return n

    def plot(self, re_min, re_max, im_min, im_max, width, height, max_iter):
        re, im = np.linspace(re_min, re_max, width), np.linspace(im_min, im_max, height)
        mandelbrot_set = np.empty((width, height))
        
        for i in range(width):
            for j in range(height):
                c = complex(re[i], im[j])
                mandelbrot_set[i, j] = self.mandelbrot(c, max_iter)

        # Display the mandelbrot set
        self.ax.imshow(mandelbrot_set.T, extent=[re_min, re_max, im_min, im_max], cmap='inferno')
        self.ax.set_title("Mandelbrot Set")
        
        # Save the figure as a file
        self.fig.savefig('mandelbrot_plot.png')  # Save the plot to a PNG file

if __name__ == "__main__":
    mandelbrot_plotter = MandelbrotPlotter()
    mandelbrot_plotter.plot(-2.0, 1.0, -1.5, 1.5, 1000, 1000, 100)
