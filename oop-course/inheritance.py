class Employee:
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)


class SlotsInspectorMixin:
    __slots__ = ()
    def has_slots(self):
        return hasattr(self, "__slots__")


class Developer(Employee, SlotsInspectorMixin):
    __slots__ = ("framework", )

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework


    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus

emp2 = Developer("Yehia" , 44, 1000, 'Flask')
emp2.increase_salary(10, 50)

print(isinstance(emp2, Developer))
print(issubclass(Employee, Developer))

print(emp2.has_slots())
print(Developer.__mro__)

