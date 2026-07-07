# "can self of the class be named something else?"
# "yes"


class checkSelf:
    def __init__(slf,name):
        slf.name=name
        print(f"Yo {(slf.name).capitalize()}, Its all good! Chill Bro. ")
        print("Change all self to anything but better call it self for readability")

name=input('Enter your name:')


person1=checkSelf(name)