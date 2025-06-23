from cat import get_cats_info
from colorama import Fore
from directory_view import show_dir_structure
from pathlib import Path
from salary import salary_info

if __name__ == "__main__":
    
    curr_dir = Path(__file__).parent
    file_path = curr_dir / 'salaries.txt'

    total, average = salary_info(file_path)

    print(Fore.BLUE + " === Task 1 . Salary Info === " + Fore.RESET)
    print(f"Total Salary: {total}")
    print(f"Average Salary: {average}")

    file_path = curr_dir / "cats_info.txt"

    cats_info = get_cats_info(file_path)

    print(Fore.BLUE + " === Task 2 . Cats Info === " + Fore.RESET)
    print(cats_info)

    print(Fore.BLUE + " === Task 3. Directory view === " + Fore.RESET)
    dir = input("Enter directory path (leave empty for current directory): ")
    if not dir:
        dir = curr_dir
    else:
        dir = Path(dir)

    print("Directory structure:")
    print(show_dir_structure(dir, 0))
   
