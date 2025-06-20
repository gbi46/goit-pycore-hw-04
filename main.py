from cat import get_cats_info
from pathlib import Path
from salary import salary_info

if __name__ == "__main__":
    
    curr_dir = Path(__file__).parent
    file_path = curr_dir / 'salaries.txt'

    total, average = salary_info(file_path)

    print(" === Task 1 . Salary Info === ")
    print(f"Total Salary: {total}")
    print(f"Average Salary: {average}")

    file_path = curr_dir / "cats_info.txt"

    cats_info = get_cats_info(file_path)

    print(" === Task 2 . Cats Info === ")
    print(cats_info)
