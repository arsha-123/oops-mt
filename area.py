class Area():                                                               #first creating a class Area
    length=0
    width=0

    def calculateArea(self):                                              # creating a method calculateArea
        print("area")

    

class Rectangle(Area):                                                    #creating a new class Rectangle under class Area
    def __init__(self,l,w):
        self.length=l
        self.width=w

    def calculateArea(self):                                             #overridding calculateArea method
        print("Area of rectangle =",self.length*self.width)


class Circle(Area):                                                      #creating a new class circle under class Area
    def __init__(self,l):
        self.length=l
    

    def calculateArea(self):                                              # again overridding calculateArea method
        print("Area of circle =",3.14*(self.length/2)*(self.length/2))

rect=Rectangle(50,20)
cir=Circle(20)
rect.calculateArea()
cir.calculateArea()