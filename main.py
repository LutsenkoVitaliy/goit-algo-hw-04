from pathlib import Path

parent_folder_path = Path('./')

#ПЕРШЕ ЗАВДАННЯ
path = 'Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000'

with open (parent_folder_path / 'salary_file.txt', 'w', encoding='utf-8') as salary_file:
  salary_file.write(path)

def total_salary(path):
  try: 
    with open(path, 'r', encoding='utf-8') as salary_file:
      salaries = []
      lines = [el.strip() for el in salary_file.readlines()]

      for el in lines:
        name, salary = el.split(',')
        salaries.append(int(salary))
    
    total = sum(salaries)
    average = round(total / len(salaries))
    return (total, average)

  except FileNotFoundError:
    return (0,0)
  except PermissionError:
    return (0,0)
  except Exception as e:
    return (0,0)
  
total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# ДРУГЕ ЗАВДАННЯ
path = '60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5'
