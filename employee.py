class Employee:
    name=""
    age=0
    salary=0
    def setData(self):
        self.name = input ("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = int(input("Enter salary: "))
    def showData(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Salary :",self.salary)
if __name__ == '__main__':
    emp = Employee()
    emp.setData()
    emp.showData()