'''
Create a class with a class attribute 
a create an object from it and set "a"
directly using object.a =o.
Does this change the class attribute?
'''

class Demo:
    a=4

o=Demo()
print(o.a)
o.a =0#instance attribute is set
print(o.a)#no it will not change class attribute but create an instance attribute  

print(Demo.a)#it will stay same