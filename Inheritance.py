class Employee:
    
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print('{} {} {}'.format(self.id, self.name, self.salary))


class Developer(Employee):
    
    def __init__(self, name, id, salary, raise_):
        self.raise_ = raise_
        Employee.__init__(self, name, id, salary)

    def display(self):
        Employee.display(self)
        print('Raise: {}'.format(self.raise_))


class Manager(Employee):
    def __init__(self, name, id, salary, raise_):
        Employee.__init__(self, name, id, salary)
        self.raise_ = raise_

    def display(self):
        Employee.display(self)
        print('Raise: {}'.format(self.raise_))


class Company:

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def display(self):
        print(self.name)
        for emp in self.employees:
            emp.display()

    def raise_salary(self):
        for emp in self.employees:
            emp.salary *= emp.raise_


d1 = Developer('Madhur', 1, 10000, 1.4)
d1.display()

m1 = Manager('Heena', 2, 20000, 1.7)
m1.display()


c1 = Company('Codekul', [d1, m1])

c1.display()

c1.raise_salary()

c1.display()
