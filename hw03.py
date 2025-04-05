from pathlib import Path
import sys
from colorama import init,Fore, Back

init(autoreset=True)

def folder_structure(directory, indent="  "):
  if not directory.exists() or not directory.is_dir():
    print(Back.RED + "Вказана директорія не існує або не являється директорією")
    return
  
  for element in directory.iterdir():
    if element.is_dir():
      print(Fore.BLUE + indent + f"{element.name}/")
      folder_structure(element, indent + "  ")
    
    if element.is_file():
      print(Fore.GREEN + indent + f"{element.name}")



if __name__ == "__main__":
  if len(sys.argv) != 2:
    print(Back.RED + f"Передані параметри не є дійсними: {' '.join(sys.argv)}")
    print(Back.RED + "Приклад: python hw03.py шлях/до/вашої/директорії")
    sys.exit(1)

  path_to_directory = Path(sys.argv[1])
  print(Fore.BLUE + f"{path_to_directory}/")
  folder_structure(path_to_directory)
