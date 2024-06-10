import csv


def read_data(file_path):
    employees = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")
    return employees


def validate_data(employees):
    valid_employees = []
    for employee in employees:
        try:
            if all(field in employee for field in ['name', 'worked_hours', 'pay_per_hour']):
                employee['worked_hours'] = float(employee['worked_hours'])
                employee['pay_per_hour'] = float(employee['pay_per_hour'])
                if employee['worked_hours'] >= 0 and employee['pay_per_hour'] >= 0:
                    valid_employees.append(employee)
                else:
                    print(f"Error: Worked hours or salary are negative numbers: {employee}")
            else:
                print(f"Error: Data missing from the employee: {employee}")
        except ValueError:
            print(f"Error: Wrong format in the employee data: {employee}")
    return valid_employees
