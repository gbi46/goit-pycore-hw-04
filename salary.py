from collections import namedtuple
from file_helper import clean_data, load_data

def get_salaries(data) -> list[int]:
    salaries = list()

    for salary in data:
        clean_salary = int(salary.split(',')[1].strip())
        salaries.append(clean_salary)

    return salaries
    
def salary_info(path):
    file_data = load_data(path)
    cleaned_data = clean_data(file_data)
    salaries = get_salaries(cleaned_data)

    total_salary = sum(salaries)
    avg_salary = total_salary // len(salaries)

    SalaryData = namedtuple("SalaryData", ['total', 'average'])

    return SalaryData(total=total_salary, average=avg_salary)
