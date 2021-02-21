import csv
import os
import unittest
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name, title, level):
        self.id = id
        self.name = name
        self.title = title
        self.level = level

    @abstractmethod
    def calculate_pay(self):
        pass

    def __str__(self):
        return f'{self.name}-{self.title}-{self.calculate_pay()}'

class BonusEmployee(ABC):
    def __init__(self, sales, percent):
        self.bonus = int(sales) * int(percent) / 100

class SalaryEmployee(Employee):
    def __init__(self, id, name, title, level, salary):
        super().__init__(id, name, title, level)
        self.salary = int(salary)

    def calculate_pay(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, title, level, salary, worked_hours):
        super().__init__(id, name, title, level)
        self.salary = int(salary)
        self.worked_hours = int(worked_hours)

    def calculate_pay(self):
        return self.salary * self.worked_hours

class BonusSalaryEmployee(SalaryEmployee, BonusEmployee):
    def __init__(self, id, name, title, level, salary, sales, percent):
        SalaryEmployee.__init__(self, id, name, title, level, salary)
        BonusEmployee.__init__(self, sales, percent)

    def calculate_pay(self):
        return super().calculate_pay() + self.bonus

class BonusHourlyEmployee(HourlyEmployee, BonusEmployee):
    def __init__(self, id, name, title, level, salary, worked_hours, sales, percent):
        HourlyEmployee.__init__(self, id, name, title, level, salary, worked_hours)
        BonusEmployee.__init__(self, sales, percent)

    def calculate_pay(self):
        return super().calculate_pay() + self.bonus


class FactoryEmployee:
    CLASS_MAPPING = {
        'salary': SalaryEmployee,
        'hourly': HourlyEmployee,
        'bonus_salary': BonusSalaryEmployee,
        'bonus_hourly': BonusHourlyEmployee
    }
    @staticmethod
    def get_employee(employee_type, *args, **kwargs):
        EmployeeClass = FactoryEmployee.CLASS_MAPPING[employee_type]
        kwargs = {k: v for k, v in kwargs.items() if k in EmployeeClass.__init__.__code__.co_varnames}
        return EmployeeClass(*args, **kwargs)

    @staticmethod
    def get_employee_type(line):
        employee_type = 'hourly' if line['hourly'] == 'Yes' else 'salary'

        if line.get('commision_sales'):
            employee_type = f'bonus_{employee_type}'
        return employee_type

    @classmethod
    def get_employees(cls, csv_path):
        with open(csv_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                employee_type = cls.get_employee_type(line)
                yield cls.get_employee(employee_type, **line)


csv_path = os.path.normpath('employee_data.csv')

for employee in FactoryEmployee.get_employees(csv_path):
    print(employee)

class TestSalary(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = SalaryEmployee(1, "Kim Johnson", "DevOps", 'intern', 1000)
    def test_print(self):
        self.assertEqual(str(self.employee) == "Kim Johnson-DevOps-1000")



# employee_1 = FactoryEmployee.get_employee('salary', 1, "Kim Johnson", "DevOps", 'intern', 1000)
# employee_2 = FactoryEmployee.get_employee('hourly', 2, "Jack Roth", "Software Engineer", 'mid', 50, 20)
#
# employee_3 = FactoryEmployee.get_employee('bonus_salary', 3, "John Page", "Sales manager", 'senior', 7000, 80000, 8)
# employee_4 = FactoryEmployee.get_employee('bonus_hourly', 4, "Tim Roth", "Sales representive", 'mid', 60, 15, 50000, 4)
#
# print(employee_1)
# print(employee_2)
# print(employee_3)
# print(employee_4)


# salary_employee = SalaryEmployee(1, "Kim Johnson", "DevOps", 'intern', 1000)
# hourly_employee = HourlyEmployee(2, "Jack Roth", "Software Engineer", 'mid', 50, 20)
#
# bonus_salary_employee = BonusSalaryEmployee(3, "John Page", "Sales manager", 'senior', 7000, 80000, 8)
# bonus_hourly_employee = BonusHourlyEmployee(4, "Tim Roth", "Sales representive", 'mid', 60, 15, 50000, 4)
#
# print(salary_employee)
# print(hourly_employee)
# print(bonus_salary_employee)
# print(bonus_hourly_employee)