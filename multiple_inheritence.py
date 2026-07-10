class Employee:
    company="Tata"
    salary=4000000
    def show(self):
        print(f"The name of the company is {self.company} and the salary is {self.salary}")

class language:
    language="python"
    def showLanguage(self):
        print(f"He is good with {self.language} language")

class Programmer(Employee,language):
    def show(self):
        print(f"The name of his company is {self.company} and he is good with {self.language} language and the salary is {self.salary}.")


b=Programmer()
b.show()
