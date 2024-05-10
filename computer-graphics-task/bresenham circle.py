#circle and line drawing
def bresenham_circle(x0, y0, radius):
      x = radius
      y = 0
      err = 0
      while x >= y:
       print(x0 + x, y0 + y)
       print(x0 + y, y0 + x)
       print(x0 - y, y0 + x)
       print(x0 - x, y0 + y)
       print(x0 - x, y0 - y)
       print(x0 - y, y0 - x)
       print(x0 + y, y0 - x)
       print(x0 + x, y0 - y) 
       y += 1
       err += 1 + 2*y
       if 2*(err-x) + 1 > 0:
        x -= 1
        err += 1 - 2*x

import matplotlib.pyplot as plt

def bresenham_circle(x0, y0, radius):
  x = radius
  y = 0
  err = 0

  points = []

  while x >= y:
    points.append((x0 + x, y0 + y))
    points.append((x0 + y, y0 + x))
    points.append((x0 - y, y0 + x))
    points.append((x0 - x, y0 + y))
    points.append((x0 - x, y0 - y))
    points.append((x0 - y, y0 - x))
    points.append((x0 + y, y0 - x))
    points.append((x0 + x, y0 - y))

    y += 1
    err += 1 + 2*y
    if 2*(err-x) + 1 > 0:
      x -= 1
      err += 1 - 2*x

  return points

points = bresenham_circle(50, 50, 30)

# plot the points
plt.scatter([x for x, y in points], [y for x, y in points])

# draw the circle
circle = plt.Circle((50, 50), 30, fill=False)
plt.gcf().gca().add_artist(circle)

plt.show()
# from bresenham import bresenham
import matplotlib.pyplot as plt

# Define the start and end points of the line
start = (1, 1)
end = (8, 5)

# Use Bresenham's algorithm to generate the points of the line
# line_points = list(bresenham(start[0], start[1], end[0], end[1]))

# Unzip the points into separate lists of x and y coordinates
# x, y = zip(*line_points)

# Plot the line
plt.plot(x, y, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bresenham Line')
plt.grid(True)
plt.show()