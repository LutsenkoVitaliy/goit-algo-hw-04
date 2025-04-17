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
        salaries.append(float(salary))
    
    total = sum(salaries)
    average = round(total / len(salaries)) if salaries else 0
    return (total, average)

  except FileNotFoundError:
    print('FileNotFoundError')
    return (0,0)
  except PermissionError:
    print('PermissionError')
    return (0,0)
  except Exception as e:
    print(f'Exception {e}')
    return (0,0)
  
total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# ДРУГЕ ЗАВДАННЯ
path = '60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5'

with open(parent_folder_path / 'cats_file.txt', 'w', encoding='utf-8') as cats_file:
  cats_file.write(path)

def get_cats_info(path):
  with open(path, 'r', encoding='utf-8') as cats_file:
    try:
      cats_info_libary = []
      lines = [el.strip() for el in cats_file.readlines()]

      for el in lines:
        id,name,age = el.split(',')
        cats_info_libary.append({'id': id, 'name': name, 'age': age})

      return cats_info_libary
    
    except FileNotFoundError:
      print('FileNotFoundError')
      return []
    except PermissionError:
      print('PermissionError')
      return []
    except Exception as e:
      print('Exception')
      return []
    

cats_info = get_cats_info("./cats_file.txt")
print(cats_info)
