#Iqra Quereshi 
#0157EC231014

import json
import sys


DATA_FILE = "students.json"



def load_data():
   
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
      
        return {}
    except PermissionError:
        print(f"\nFATAL ERROR: Permission denied to read file '{DATA_FILE}'.")
        print("Please check your file permissions or run the script in a writable directory.")
       
        sys.exit(1) 
    except json.JSONDecodeError:
        print(f"\nWARNING: Data file '{DATA_FILE}' is corrupted. Starting with an empty database.")
        return {}

def save_data(data):
  
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except PermissionError:
     
        print(f"\nERROR: Permission denied to write to file '{DATA_FILE}'.")
        print("Registration/Update failed. Check your file permissions.")
    except Exception as e:
        
        print(f"\nAn unexpected error occurred while saving data: {e}")



def register(data):
   
    username = input("Enter username: ")
    if username in data:
        print("Username already exists! Try a different one.")
        return

    student = {
        "name": input("Enter full name: "),
        "age": input("Enter age: "),
        "gender": input("Enter gender: "),
        "email": input("Enter email: "),
        "phone": input("Enter phone number: "),
        "address": input("Enter address: "),
        "course": input("Enter course name: "),
        "roll_no": input("Enter roll number: "),
        "year": input("Enter academic year: "),
        "password": input("Enter password: ")
    }

    data[username] = student
    save_data(data)
   
    if username in data:
        print("Registration successful!")

def login(data):
    
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in data and data[username]["password"] == password:
        print(f"\nWelcome, {data[username]['name']}!")
        return username
    else:
        print("Invalid username or password.")
        return None

def show_profile(data, username):
   \
    print("\n--- Student Profile ---")
    for key, value in data[username].items():
        if key != "password":
            print(f"{key.replace('_', ' ').title()}: {value}")
    print("-----------------------")

def update_profile(data, username):
    \
    print("\n--- Update Profile ---")
    for key in data[username]:
        if key != "password":
            current_value = data[username][key]
            new_value = input(f"Enter new {key.replace('_', ' ').lower()} (current: {current_value}, press Enter to skip): ")
            if new_value:
                data[username][key] = new_value
    
    
    new_password = input("Enter new password (press Enter to keep old one): ")
    if new_password:
        data[username]["password"] = new_password
        
    save_data(data)
    print("Profile updated successfully!")


def main():
    data = load_data()
    logged_in_user = None

    while True:
        print("\n--- Student Management System ---")
     
        print("1. Register")
        print("2. Login")
        if logged_in_user:
            print("3. Show Profile")
            print("4. Update Profile")
            print("5. Logout")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register(data)

        elif choice == "2":
            if not logged_in_user:
                logged_in_user = login(data)
            else:
                print(f"You are already logged in as {logged_in_user}.")

        elif choice == "3":
            if logged_in_user:
                show_profile(data, logged_in_user)
            else:
                print("Please login first.")

        elif choice == "4":
            if logged_in_user:
                update_profile(data, logged_in_user)
               
                data = load_data() 
            else:
                print("Please login first.")

        elif choice == "5":
            if logged_in_user:
                print(f"User '{logged_in_user}' logged out successfully.")
                logged_in_user = None
            else:
                print("No user is logged in.")

        elif choice == "6":
            print("Exiting system... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()