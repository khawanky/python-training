from datetime import date

class Employee:
    minimum_wage = 1000

    @classmethod
    def change_min_wage(cls, new_wage):
        if new_wage> 3000:
            raise ValueError('Company is bankrupt.')
        cls.minimum_wage = new_wage

    # Factory function (like a custom constructor)
    @classmethod
    def new_employee(cls, name,dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,salary):
        if salary<1000:
            raise ValueError('Minimum wage is $1000')
        self._salary=salary
#
# print(Employee.__dict__)
# e = Employee("asd", 23, 1000)
# Employee.__dict__["increase_salary"](e,20)
#
# print(e.minimum_wage)
# Employee.change_min_wage(200)
# print(e.minimum_wage)



e = Employee.new_employee("asd", date(1991, 8, 12))
print(e.name)
print(e.age)
print(e.salary)

