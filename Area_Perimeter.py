class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height
    
  def area(self):
    return self.width*self.height
  def perimeter(self):
    return 2*(self.width+self.height)

while True:
    print("1. Area of rectangle: ")
    print("2. Area of square: ")
    print("3. Perimeter of rectangle: ")
    print("4. Perimeter of square: ")
    print("5. Exit")
    try:
        opt=int(input("Enter 1-4:  "))
        if opt==1:
            w=float(input("Enter width of rectangle: "))
            h=float(input("Enter the height of rectangle: "))
            r1=Rectangle(w,h)
            print(f"Area of rectangle= {r1.area()}")
        elif opt==2:
           s=float(input("Enter side of a square: "))
           s1=Rectangle(s,s)
           print(f"Area of square= {s1.area()}")
        elif opt==3:
            w=float(input("Enter width of rectangle: "))
            h=float(input("Enter the height of rectangle: "))
            r1=Rectangle(w,h)
            print(f"Perimeter of rectangle= {r1.perimeter()}")
        elif opt==4:
           s=float(input("Enter side of a square: "))
           s1=Rectangle(s,s)
           print(f"Perimeter of square= {s1.perimeter()}")

        elif opt==5:
           print("Bye!")
           break
        else:
           print("Invalid Input! Enter 1-4!!!")

    except:
       print("Invalid Input! Enter 1-4!!!")
