import os
from data_input import read_data, validate_data
from processing import calculate_gross_salary, calculate_deductions, calculate_net_salary
from generate_pdf import create_pdf_file


def main():
    file_path = 'employees.csv'
    # Put your file path here.

    if not os.path.exists(file_path):
        print(f"The file {file_path} doesn't exist. Please create the file with your employees names.")
        return

    employees = read_data(file_path)
    valid_employees = validate_data(employees)

    for employee in valid_employees:
        gross_salary = calculate_gross_salary(employee['worked_hours'], employee['pay_per_hour'])
        deductions = calculate_deductions(gross_salary)
        net_salary = calculate_net_salary(gross_salary, deductions)

        print(f"Receipt for {employee['name']}:")
        print(f"Gross salary: {gross_salary}")
        print(f"Deductions: {deductions}")
        print(f"Net Salary: {net_salary}\n")

        create_pdf_file(employee['name'], gross_salary, deductions, net_salary)


if __name__ == "__main__":
    main()
