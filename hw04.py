def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
  if len(args) != 2:
    return "Невірний формат команди. Приклад: add [ім'я] [номер телефону]"
  
  name, phone = args
  contacts[name] = phone
  return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Невірний формат команди. Приклад: change [ім'я] [оновлений номер телефону]"
  
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact update."
    
    return "Contact not foun."

def show_contact(args, contacts):
    if len(args) != 1:
        return "Невірний формат команди. Приклад: phone [ім'я]"

    return contacts.get(args[0], "Contact not found.")

def show_all_contacts(contacts):
    if not contacts:
        return "No contacts in phone book."
    
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
      user_input = input("Enter a command: ").strip().lower()
      command, *args = parse_input(user_input)

      if command in ["close", "exit"]:
        print("Good bye!")
        break
      elif command == "hello":
        print("How can I help you?")
      elif command == "add":
        print(add_contact(args, contacts))
      elif command == "change":
        print(change_contact(args, contacts))
      elif command == "phone":
        print(show_contact(args, contacts))
      elif command == "all":
        print(show_all_contacts(contacts))
      else:
        print("Invalid command.")


if __name__ == "__main__":
  main()
