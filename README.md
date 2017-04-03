# Shapes

You can download and run the file and it will run a demo program. 

Alternatively, create a new Python file in the same folder as **shapes.py** and use it like this:

```python
from shapes import Paper, Triangle, Rectangle, Oval
# You need to create a Paper object to draw your shapes on
paper = Paper()

# Random size and location triangle
tri = Triangle(paper)
tri.randomise()
tri.draw()

# Specific size and location rectangle
rect = Rectangle(paper, height=40, width=90, x=110, y=20, color="yellow")
rect.draw()

# Default oval
oval = Oval(paper)
oval.draw()

```
