class Parent1:
    a = 1   # Parent class variable

class Child1(Parent1):
    b = 2   # Inherits Parent1 and adds b

class Child2(Child1):
    c = 3   # Inherits Child1 and adds c

inst1 = Child2()  # Create Child2 object

# Access inherited and own variables
print(inst1.a, inst1.b, inst1.c)