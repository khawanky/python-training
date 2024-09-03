class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def calculate_paycheck( self):
        return self.salary/52

    def __str__(self):
        return f"Employee: first_name={self.fname} last_name={self.lname} salary={self.salary}"

