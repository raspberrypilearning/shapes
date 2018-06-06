from shapes import Paper, Triangle, Rectangle, Oval

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
rect1.draw()

tri = Triangle(5, 5, 100, 5, 100, 200)
tri.draw()

Paper.display()