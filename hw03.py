from pathlib import Path
import os 
import sys
from colorama import Fore, Back, Style

# print(Fore.RED + 'Це червоний текст')
# print(Back.GREEN + 'Це текст на зеленому фоні')
# print(Style.RESET_ALL)
# print('Це звичайний текст після скидання стилю')

def folder_structure(directory, indent="  "):
  pass


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print(f"Передані параметри не є дійсними, {" ".join(sys.argv)}")
    print("Приклад: python hw03.py шлях/до/вашої/дирикторії")
    sys.exit(1)

  path_to_directory = Path(sys.argv[1])
  print(f"{path_to_directory}/")
  folder_structure(path_to_directory)