class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None

    @property
    def salary(self):
        return self._salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary*12
        return self._annual_salary

    @salary.setter
    def salary(self,salary):
        if salary<1000:
            raise ValueError('Minimum wage is $1000')
        self._annual_salary = None
        self._salary=salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def __str__(self):
        return f"{self.name} is {self.age} years old. He is a {self
              .position} with {self.salary}$ salary"

    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"

emp = Employee('Ji', 38, 'Manager', 1000)

print(repr(emp))
print(emp.annual_salary)

emp.increase_salary(20)
print(repr(emp))
print(emp.annual_salary)

