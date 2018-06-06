# This code requires Python 3 and tkinter (which is usually installed by default)
# This code will NOT work on trinket.io as the tkinter module is not supported
# Raspberry Pi Foundation 2017
# CC-BY-SA 4.0

try:
    from tkinter import Tk, Canvas, BOTH    
except ImportError:
    print("tkinter did not import successfully - check you are running Python 3 and that tkinter is available.")
    exit(1)

# create the tkinter object which will used in the Paper class.
try:
    tk = Tk()
except ValueError:
    print("Error: could not instantiate Paper object")
    exit(1)

import random

class Paper():

    def __init__(self, width=600, height=600):

        """Create a Paper object which allows shapes to be drawn onto it.
        """
        # Call the constructor from the superclass (tkinter's Tk)

        # Set some attributes
        tk.title( "Drawing shapes" )
        tk.geometry(str(width)+"x"+str(height))
        tk.paper_width = width
        tk.paper_height = height

        # Create a tkinter canvas object to draw on
        tk.canvas = Canvas(tk)
        tk.canvas.pack(fill=BOTH, expand=1)

    # return the instance of tk 
    def __get__(self, instance, owner):
        return tk

    # allows Paper.display() to be called triggering the tk mainloop
    @staticmethod
    def display():
        """
        Displays the paper object
        """
        tk.mainloop()

class Shape():

    # Static class variable removing the need to pass in a Paper object
    # to draw the shapes on
    paper = Paper()

    # Constructor for Shape
    def __init__(self, width=50, height=50, x=None, y=None, color="black"):

        """Creates a generic 'shape' which contains properties common to all
        shapes such as height, width, x y coordinates and colour.
        """

        # Set some attributes
        self.height = height
        self.width = width
        self.color = color

        # Put the shape in the centre if no xy coords were given
        if x is None:
            self.x = (self.paper.paper_width/2) - (self.width/2)
        else:
            self.x = x
        if y is None:
            self.y = (self.paper.paper_height/2) - (self.height/2)
        else:
            self.y = y

    # This is an internal method not meant to be called by users
    # (It has a _ before the method name to show this)
    def _location(self):
        """Internal method used by the class to get the location
        of the shape. This shouldn't be called by users, hence why its
        name begins with an underscore.
        """

        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        return [x1, y1, x2, y2]

    # Randomly generate what the shape looks like
    def randomize(self, smallest=20, largest=200):

        """Randomly generates width, height, position and colour for a shape. You can specify
        the smallest and largest random size that will be generated. If not specified, the
        generated shape will default to a random size between 20 and 200.
        """

        self.width = random.randint(smallest, largest)
        self.height = random.randint(smallest, largest)

        self.x = random.randint(0, self.paper.paper_width-self.width)
        self.y = random.randint(0, self.paper.paper_height-self.height)

        self.color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])

    # Getters and setters for Shape attributes
    def set_width(self, width):
        """Sets the width of the shape"""

        self.width = width

    def set_height(self,height):
        """Sets the height of the shape"""

        self.height = height

    def set_x(self, x):
        """Sets the x position of the shape"""

        self.x = x

    def set_y(self, y):
        """Sets the y position of the shape"""

        self.y = y

    def set_color(self, color):
        """Sets the colour of the shape"""

        self.color = color

    def get_color(self):
        """Returns the colour of the shape"""

        return self.color


# Rectangle class is a subclass of Shape
class Rectangle(Shape):

    # This is how to draw a rectangle
    def draw(self):

        """Draws a rectangle on the canvas. The properties of the rectangle
        can be set using the getter and setter methods in Shape"""

        x1, y1, x2, y2 = self._location()

        # Draw the rectangle
        self.paper.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)


class Oval(Shape):

    def draw(self):

        """Draws an oval on the canvas. The properties of the oval
        can be set using the getter and setter methods in Shape"""

        x1, y1, x2, y2 = self._location()

        # Draw the oval
        self.paper.canvas.create_oval(x1, y1, x2, y2, fill=self.color)


class Triangle(Shape):

    # Every constructor parameter has a default setting
    # e.g. color defaults to "black" but you can override this
    def __init__(self, x1=0, y1=0, x2=20, y2=0, x3=20, y3=20, color="black"):

        """Overrides the Shape constructor because triangles require three
        coordinate points to be drawn, unlike rectangles and ovals."""

        try:
            super().__init__(color=color)
        except ValueError:
            print("Error: could not instantiate Triangle")

        # Remove height and width attributes which make no sense for a triangle
        # (triangles are drawn via 3 xy coordinates)
        del self.height
        del self.width

        # Instead add three coordinate attributes
        self.x = x1
        self.y = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def _location(self):

        """Internal method used by the class to get the location
        of the triangle. This shouldn't be called by users, hence why its
        name begins with an underscore.
        """

        return [self.x, self.y, self.x2, self.y2, self.x3, self.y3]

    def draw(self):

        """Draws a triangle on the canvas. The properties of the triangle
        can be set using the getter and setter methods in Shape"""

        x1, y1, x2, y2, x3, y3 = self._location()
        # Draw a triangle
        self.paper.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=self.color)

    def randomize(self):

        """Randomly chooses the location of all 3 triangle points as well
        as the colour of the triangle"""

        # Randomly choose all the points of the triangle
        self.x = random.randint(0, self.paper.paper_width)
        self.y = random.randint(0, self.paper.paper_height)
        self.x2 = random.randint(0, self.paper.paper_width)
        self.y2 = random.randint(0, self.paper.paper_height)
        self.x3 = random.randint(0, self.paper.paper_width)
        self.y3 = random.randint(0, self.paper.paper_height)

        # Randomly choose a colour of this triangle
        self.color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])

    # Change the behaviour of set_width and set_height methods for a triangle
    # because triangles are not drawn in the same way
    def set_width(self, width):
        """Overrides the setter method for width"""

        print("Width is not defined for Triangle objects")

    def set_height(self, height):
        """Overrides the setter method for height"""

        print("Height is not defined for Triangle objects")


# This if statement means
# "if you run this file (rather than importing it), run this demo script"
if __name__ == "__main__":

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

    Paper.display()