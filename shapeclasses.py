#-------------------
#Shape classes
#-------------------
from abc import ABC,abstractmethod
import math
import turtle
t = turtle.Turtle()
pi = 3.1428
turtle.tracer(0)


#Template for all shape objects sets up the inheritance and polymorphism
class Shape(ABC):
    def __init__(self,colour,is_filled):
        self.colour = colour
        self.is_filled = is_filled

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass
  
  
class Square(Shape):
    def __init__(self,colour,is_filled,width,turtle_obj):
        super().__init__(colour,is_filled)#Inheritance
        self.t = turtle_obj
        self.width = width
        
    def area(self,width):#polymorphism
        return width*width
    
    def perimeter(self,width):#polymorphism
        return width*4
    
    def draw(self):#polymorphism
        self.t.fillcolor(self.colour)
        self.t.begin_fill()
        for x in range(5):
            self.t.forward(self.width)
            self.t.left(90)#angle it turns every movement
        self.t.end_fill()
        turtle.update()
        
class Circle(Shape):
    def __init__(self,colour,is_filled,radius,turtle_obj):
        super().__init__(colour,is_filled)#inheritance
        self.t = turtle_obj
        self.radius = radius

    def area(self):#polymorphism
        return 2*pi*self.radius**2
    
    def perimeter(self):#polymorphism
        return 2*pi*self.radius
    
    def draw(self):#polymorphism
        total_distance = self.perimeter()
        draw = total_distance/360#360 degrees in a circle 
        self.t.fillcolor(self.colour)
        self.t.begin_fill()
        for x in range(361):
            self.t.forward(draw)
            self.t.left(1)#turns 1 degree every movement
        self.t.end_fill()
        turtle.update()
        
class EquilateralTriangle(Shape):
    def __init__(self,colour,is_filled,sides,turtle_obj):
        super().__init__(colour,is_filled)#inheritance
        self.t = turtle_obj
        self.sides = sides
        
    def perimeter(self):#polymorphism
        return self.sides*3
    
    def area(self):#polymorphism
        return 0.5 * self.sides * (self.sides*self.sides*2 ** 0.5)#half base x perpindicular height,perpheight is got with pythagores theorem
    
    def draw(self):#polymorphism
        t.fillcolor(self.colour)
        t.begin_fill()
        for x in range(3):
            t.forward(self.sides)
            t.left(120)#angle it need to turn
        t.end_fill()
        turtle.update() #displays shape
 
class Triangle(Shape):
    
    
    def __init__(self,colour,is_filled,side_a,side_b,side_c,turtle_obj):
        super().__init__(colour,is_filled)
        #This whole if statement checks if the triangle entered is valid(Triangle Inequality Theorem)
        if not side_a > 0 and side_b > 0 and side_c > 0 and\
        side_a + side_b > side_c and\
        side_a + side_c > side_b and\
        side_b + side_c > side_a:
            raise ValueError("Invalid dimensions entered")#raises
            
        else:
            self.t = turtle_obj
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
            
    def find_angles(self):
        sides_and_angles = []
        #useing law of cosine to find the angles
        angle_a = math.degrees(math.acos((self.side_b*self.side_b + self.side_c*self.side_c - self.side_a*self.side_a) / (2*self.side_b*self.side_c)))
        angle_b = math.degrees(math.acos((self.side_c*self.side_c + self.side_a*self.side_a - self.side_b*self.side_b) / (2*self.side_a*self.side_c)))
        angle_c = math.degrees(math.acos((self.side_b*self.side_b + self.side_a*self.side_a - self.side_c*self.side_c) / (2*self.side_b*self.side_a)))
        #adding the tuples to a list for use later on in .draw
        sides_and_angles.append((self.side_a,angle_a))
        sides_and_angles.append((self.side_b,angle_b))
        sides_and_angles.append((self.side_c,angle_c))
        return sides_and_angles
    def area(self):
        return 0.5 * self.base * (((self.sides**2) + (self.base/2 ** 2)) ** 0.5)#half base x perpindicular height,perpheight is got with pythagores theorem
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
    def draw(self):
        self.find_angles()#returns list of tuples with the sides of triangle and corresponding angles
        print("sides_and_angles =", self.find_angles(), type(self.find_angles()))
        self.t.fillcolor(self.colour)
        if self.is_filled:
            self.t.begin_fill()
        
        for side,angle in self.find_angles():
            self.t.left(180-angle)
            self.t.forward(side)
            
        self.t.end_fill()
        turtle.update()

Triangle(colour = "red",is_filled = False, side_a = 50,side_b = 70,side_c = 40 ,turtle_obj = t).draw()
