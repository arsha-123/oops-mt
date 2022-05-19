class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b

class UseCalculator(Calculator):

    a=int(input("First number: "))
    b=int(input("Second number: "))

    

    obj=Calculator(a,b)
    choice=1
    while choice!=0:
        print("0. Exit")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        choice=int(input("Enter choice: "))
        if choice==1:
            print("Result= ",obj.add())
        elif choice==2:
            print("Result= ",obj.sub())
        elif choice==3:
            print("Result= ",obj.mul())
        elif choice==4:
           print("Result= ",obj.div())
        elif choice==0:
            print("Quit")
        else:
            print("invalid")
 
 