class Employee:

    raise_amt = 1.05

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getSalary(self):
        return self.salary

    def applyRaise(self):
        self.salary = int(self.salary * self.raise_amt)

    def __str__(self):
        return "Employee: "+str(self.id) +" - "+self.name

