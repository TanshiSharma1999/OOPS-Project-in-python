'''
Create a class "Programmer" for storing info of
few programmers working at Google

'''
class Programmer:
    def __init__(self,em_id,name,branch,salary):
        self.company="Google"
        self.em_id=em_id
        self.name=name
        self.branch=branch
        self.salary=salary
        
    def result(self):
        print(f"Employee Id: {self.em_id}")    
        print(f"Employee Name: {self.name}")
        print(f"Office Branch {self.branch}")    
        print(f"Employee salary: {self.salary}")   
        print("_"*50)     

em1=Programmer(101,"Tanshi","Pune",4000000)        
em1.result()
em2=Programmer(102,"Rohan","Mumbai",5000000)        
em2.result()
em3=Programmer(103,"Vibhuti","New-Delhi",5500000)        
em3.result()