'''
write a class "Calculator" capable of finding square,cube,
and square root of a number.
'''

class Calculator:

    def __init__(self,num):
        self.num=num

    def result(self):    
        print(f"Square of the number is {self.num*self.num}")
        print(f"Cube of the number is {self.num*self.num*self.num}")
        print(f"SquareRoot of the number is {self.num**0.5}")

number=float(input("Enter a number: "))
n1=Calculator(number)
n1.result()