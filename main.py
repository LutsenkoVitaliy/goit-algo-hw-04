from pathlib import Path

parent_folder_path = Path('./')
path = 'Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000'

with open (parent_folder_path / 'salary_file.txt', 'w', encoding='utf-8') as salary_file:
  salary_file.write(path)

def total_salary(path):
  try: 
    with open(path, 'r', encoding='utf-8') as salary_file:
      salaries = []

  except FileNotFoundError:
    return (0,0)
  except PermissionError:
    return (0,0)
  except Exception as e:
    return (0,0)
  
total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
