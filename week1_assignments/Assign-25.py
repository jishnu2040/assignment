"""
    25. create a custom exception class and raise this exception when user press one in the menu and 
        handles this exception. 
"""

class ChooseInvalidOptionError(Exception):
  pass
 
# method
def menu():
  print("Select an option : ")
  print("1. Option 1")
  print("2. Option 2")
  print("3. Option 3")
  print("4. Option 4")
  choice = input("Enter your choice: ")
  if choice == "1":
      raise ChooseInvalidOptionError("Option 1 is not available for now.")
  elif choice == "2":
      print("You selected Option 2.")
  elif choice == "3":
      print("You selected Option 3.")
  elif choice == "4":
      print("You selected Option 4.")
  else:
      print("Invalid choice.")
 
# calling method in try except
try:
  menu()
except ChooseInvalidOptionError as e:
  print("Error:", e)
finally:
  print("Menu closed")