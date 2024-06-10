def calculate_gross_salary(worked_hours, pay_per_hour):
    return worked_hours * pay_per_hour


def calculate_deductions(gross_salary):
    deductions = gross_salary * 0.10  # deductions are 10%
    return deductions


def calculate_net_salary(gross_salary, deductions):
    return gross_salary - deductions


