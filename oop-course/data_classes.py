from dataclasses import dataclass


@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str

    def notify_about_project(self):
        print(f"Notifying {self.name}")


class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


p = Project("DDD app", 20000, "Happy Tex")
e = Employee("Yehia", 30, 1200, p)
p.notify_about_project()
print(e.project)
