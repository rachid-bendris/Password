import hashlib
import json
def hash_password(password):
  # utiliser SHA-256 pour hasher le mot de passe
  hash_object = hashlib.sha256(password.encode())
  hex_dig = hash_object.hexdigest()
  return hex_dig

def is_valid_password(password):
  # vérifier les exigences de sécurité
  if len(password) < 8:
    return False
  if not any(char in '!@#$%^&*' for char in password):
    return False
  if not any(char.isupper() for char in password):
    return False
  if not any(char.isdigit() for char in password):
    return False
  if not any(char.islower() for char in password):
    return False
  
  return True

def add_password(file_name):
  password = input("Choose a password: ")
  while not is_valid_password(password):
    print("Error: Invalid password. Requirements: 8 characters minimum, at least one upper case letter, one lower case letter, one number, one special character (!, @, #, $, %, ^, &, *).")
    password = input("Choose a new password: ")
  hashed_password = hash_password(password)
  with open(file_name, 'a') as f:
    f.write(hashed_password + '\n')
  print("Password added successfully.")

def display_passwords(file_name):
  with open(file_name, 'r') as f:
    for line in f:
      print(line.strip())

def manage_passwords(file_name):
  while True:
    user_input = input("Enter 1 to add a password, 2 to display passwords, or 0 to exit: ")
    if user_input == '1':
      add_password(file_name)
    elif user_input == '2':
      display_passwords(file_name)
    elif user_input == '0':
      break
    else:
      print("Invalid input.")

# exécuter le programme en gérant les mots de passe dans un fichier nommé "passwords.txt"
manage_passwords("passwords.txt")
