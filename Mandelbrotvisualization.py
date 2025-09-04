"""
Mandelbrot Set Visualizer
Jad Sabbagh
Generates and plots the Mandelbrot set using matplotlib.
"""


import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
max_iter = 125
def in_mandelbrot(c):
    z = 0
    for i in range(max_iter):
        z = z ** 2 + c
        if abs(z) > 2:
            return i  # not in set
    return max_iter  # in set


'''
# test numbers
c1 = complex(1, 1)
c2 = complex(0.1, 0.2)
c3 = complex(-0.75, 0.1)
print(in_mandelbrot(c1))
print(in_mandelbrot(c2))
print(in_mandelbrot(c3))
'''

#range of mandelbrot set
real_start,real_end= -2, 1
im_start,im_end=-1.5,1.5

#prepping screen
width,height = 1000,1000

#mapping pixels
final = []
for y_axis in range(height):
    imaginary = im_start + (im_end-im_start) * y_axis / (height-1)
    row = []
    for x_axis in range(width):
        real = real_start + (real_end - real_start) * x_axis / (width - 1)
        c_num = complex(real,imaginary)
        row.append(in_mandelbrot(c_num))
    final.append(row)

'''
for row in final:
    print(row)
#for tesing
'''
#plotting with matplotlib
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(final, cmap='Blues', extent=(real_start, real_end, im_start, im_end))
ax.set_title("Mandelbrot Set")
ax.set_xlabel("Re(c)")
ax.set_ylabel("Im(c)")

canvas = FigureCanvas(fig)
canvas.draw()
buffer = canvas.tostring_argb()
plt.show()
