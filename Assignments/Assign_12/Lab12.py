import turtle

class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

#Drawing Point
p = Point(-100, 100, 'blue')
p.draw()

class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

#Testing
# b = Box(100, 110, 50, 40, 'red')
# b.x
# b.y
# b.width
# b.height
# b.color

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)



class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

#Testing
# b= BoxFilled(1, 2, 3, 4,'blue', 'red')
# b.x
# b.y
# b.width
# b.height
# b.color
# b.fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

#Drawing Boxes 
b= Box(-100, 100, 50, 20, "blue")
b.draw()

b = BoxFilled(1, 2, 100, 200, "red", "Blue")
b.draw()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()

#Drawing Circles
c = Circle(200, 100, 50, 'Pink')
c.draw()

c = CircleFilled(300, 200, 100, 'Pink', 'Purple')
c.draw()
