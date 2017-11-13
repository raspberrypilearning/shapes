# Shapes

You can download and run the file and it will run a demo program.

Alternatively, create a new Python file in the same folder as **shapes.py** and use it like this:

```python
from shapes import Triangle, Rectangle, Oval

# Random size and location triangle
tri = Triangle()
tri.randomize()
tri.draw()

# Specific size and location rectangle
rect = Rectangle(height=40, width=90, x=110, y=20, color="yellow")
rect.draw()

# Default oval
oval = Oval()
oval.draw()

# Oval with setters
oval2 = Oval()
oval2.set_height(200)
oval2.set_width(100)
oval2.set_color("fuchsia")
oval2.set_x(30)
oval2.set_y(90)
oval2.draw()

```
