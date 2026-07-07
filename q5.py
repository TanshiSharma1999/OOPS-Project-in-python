
'''Write a class Train which has 
methods to book a ticket, get status(no of seats)
and get fare information of train running under indian railways'''



from random import randint
class Train:
    def __init__(self,train_num,fro,to):
        self.train_num=train_num
        self.fro=fro
        self.to=to

    def book(self):
        print(f"Ticket is booked in train no:{self.train_num} from {self.fro} to {self.to} ")


    def getStatus(self):
        print(f"Train no: {self.train_num} is running on time. ")
    
    def getFare(self):
        print(f"Ticket fare for train no:{self.train_num} is {randint(167,678)} ")


t1=Train(12,"New Delhi","Mumbai")
t1.book()
t1.getStatus()
t1.getFare()
