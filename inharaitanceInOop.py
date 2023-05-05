class Employee:
    def __init__(self, name, id):
        self.name = name 
        self.id = id
        
    def showDetails(self):
        print(f"The name of the employee: {self.id} is {self.name}")
class programmer(Employee):
    def showLanguage(self):
        print("The default language is python")

e1 = Employee("sohan", 1)
e1.showDetails()
e2 = Employee("sulota", 2)
e2.showDetails()
e3 = programmer("our child", 3)
e3.showLanguage()