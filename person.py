def greet():
    print("Hello to You")
    print("My name is Bella")
    username= input("May I know your name:")

#call the fn
greet()


#class for students
class students():
    #properties/attributes
    name=""
    age=14
    schoolclass="4th grade"
    school = "The High Gate"
    teacher="Mr Derzelle"

    # constructor
    def __init__(self):
        print("Adding a new student")

    # Another Function
    def change_details(self):
        print("Please enter your age: ")
        self.age=int(input())
        print("Please enter the name of the students")
        self.name=input()


    def show_details(self):
        print("The details of student are:")
        print(self.name)
        print(self.age)
        print(self.schoolclass)
        print(self.house)
        print(self.teacher)

#studednt class definition is over
#Making 2 objects/instances of student class 

Rohan= students()

Rohan.show_details()

Jake= students()

Jake.show_details()