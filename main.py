from pathlib import Path
from salary import salary_info

if __name__ == "__main__":
    
    curr_dir = Path(__file__).parent
    file_path = curr_dir / 'salaries.txt'

    total, average = salary_info(file_path)

    print(" === Task 1 . Salary Info === ")
    print(f"Total Salary: {total}")
    print(f"Average Salary: {average}")