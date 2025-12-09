#Iqra Quereshi 
#0157EC231014

import json
import sys
import random
from datetime import datetime


DATA_FILE = "students.json"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin_password"


QUIZ_QUESTIONS = {
    "DSA": [
        {"question": "What is the time complexity of searching in a Hash Table (average case)?", "options": ["O(n)", "O(log n)", "O(1)", "O(n^2)"], "answer": "O(1)"},
        {"question": "Which data structure uses LIFO principle?", "options": ["Queue", "Stack", "Array", "Linked List"], "answer": "Stack"},
        {"question": "What is the maximum number of nodes in a binary tree of height 'h'?", "options": ["2^h - 1", "2^(h+1) - 1", "h^2", "h log n"], "answer": "2^(h+1) - 1"},
        {"question": "The process of visiting all the nodes of a tree exactly once is called:", "options": ["Traversing", "Searching", "Sorting", "Cloning"], "answer": "Traversing"},
        {"question": "Which sorting algorithm has the worst-case time complexity of O(n^2)?", "options": ["Merge Sort", "Quick Sort", "Insertion Sort", "Heap Sort"], "answer": "Insertion Sort"},
        {"question": "A graph with no cycles is called a:", "options": ["Tree", "Forest", "DAG", "Connected Graph"], "answer": "Forest"},
    ],
    "DBMS": [
        {"question": "Which SQL command is used to retrieve data from a database?", "options": ["UPDATE", "INSERT", "SELECT", "DELETE"], "answer": "SELECT"},
        {"question": "What is a 'foreign key'?", "options": ["A key used in a remote database", "A primary key in another table", "An encryption key", "A column that holds non-unique values"], "answer": "A primary key in another table"},
        {"question": "Which normal form (NF) eliminates transitive dependencies?", "options": ["1NF", "2NF", "3NF", "BCNF"], "answer": "3NF"},
        {"question": "ACID properties in DBMS stand for:", "options": ["Atomicity, Consistency, Isolation, Durability", "Access, Concurrency, Integrity, Distribution", "Array, Class, Inheritance, Data", "None of the above"], "answer": "Atomicity, Consistency, Isolation, Durability"},
        {"question": "A schema describes:", "options": ["A database's structure", "A file system", "A programming language", "Network topology"], "answer": "A database's structure"},
    ],
    "PYTHON": [
        {"question": "Which of the following is an immutable data type in Python?", "options": ["list", "dictionary", "tuple", "set"], "answer": "tuple"},
        {"question": "What is the correct way to open a file for reading in Python?", "options": ["open('file.txt', 'r')", "file_open('file.txt')", "read('file.txt')", "fopen('file.txt', 'r')"], "answer": "open('file.txt', 'r')"},
        {"question": "Which keyword is used to define a function in Python?", "options": ["fun", "define", "def", "function"], "answer": "def"},
        {"question": "What does 'pip' stand for in Python?", "options": ["Preferred Installer Program", "Python Installation Package", "Pre-Installed Program", "None of the above"], "answer": "Preferred Installer Program"},
        {"question": "Which method is used to remove an item from a dictionary in Python?", "options": ["remove()", "pop()", "delete()", "clear()"], "answer": "pop()"},
        {"question": "Which symbol is used for exponentiation in Python?", "options": ["^", "**", "//", "%%"], "answer": "**"},
    ]
}


def load_data():
   
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
         
            for user in data:
                if 'scores' not in data[user]:
                    data[user]['scores'] = []
            return data
    except FileNotFoundError:
        return {}
    except PermissionError:
        print(f"\nFATAL ERROR: Permission denied to read file '{DATA_FILE}'.")
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

# ----------------------------------------------------------------------
# Authentication Functions
# ----------------------------------------------------------------------

def register(data):
    
    username = input("Enter unique username: ")
    if username in data or username == ADMIN_USERNAME:
        print("Username already exists or is reserved! Try a different one.")
        return

    
    student = {
        "name": input("Enter full name: "),
        "email": input("Enter email: "),
        "branch": input("Enter branch/course: "), # Changed to branch to match image spec
        "year": input("Enter academic year: "),
        "contact": input("Enter contact/phone number: "), # Changed to contact
        "password": input("Enter password: "),
        "scores": [] # Initialize scores list for the new user
    }

    data[username] = student
    save_data(data)
    if username in data:
        print("Registration successful!")

def login(data):
   
    username = input("Enter username: ")
    password = input("Enter password: ")

   
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("\n*** Welcome, Admin! ***")
        return username, "admin" # Return username and user_type
    
    
    if username in data and data[username]["password"] == password:
        print(f"\nWelcome, {data[username]['name']}!")
        return username, "user" 
    else:
        print("Invalid username or password.")
        return None, None


def attempt_quiz(data, username):
  
    print("\n--- Available Quiz Categories ---")
    categories = list(QUIZ_QUESTIONS.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    
    while True:
        try:
            choice = input("Select a category number to attempt the quiz: ")
            category_index = int(choice) - 1
            if 0 <= category_index < len(categories):
                category = categories[category_index]
                break
            else:
                print("Invalid category number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    print(f"\nStarting {category} Quiz...")
    
    questions_list = QUIZ_QUESTIONS[category]
    
    random.shuffle(questions_list)
    
   
    NUM_QUESTIONS = min(7, len(questions_list))
    quiz_questions = questions_list[:NUM_QUESTIONS]
    
    score = 0
    total_marks = NUM_QUESTIONS
    
 
    for i, q_data in enumerate(quiz_questions, 1):
        print(f"\nQuestion {i}/{NUM_QUESTIONS}: {q_data['question']}")
        
        
        options = q_data['options']
        random.shuffle(options)
        
      
        option_map = {} 
        for j, option in enumerate(options, 1):
            print(f"  {j}. {option}")
            option_map[str(j)] = option
            
      
        while True:
            user_choice = input("Enter the number of your answer: ")
            if user_choice in option_map:
                user_answer = option_map[user_choice]
                break
            else:
                print("Invalid option number. Try again.")

        if user_answer == q_data['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {q_data['answer']}")

    
    print("\n--- Quiz Finished! ---")
    print(f"Your final score: {score}/{total_marks}")
    
  
    record_score(data, username, category, score, total_marks)

def record_score(data, username, category, marks, total_marks):
   
    if username in data:
        score_record = {
            "category": category,
            "marks": marks,
            "total_marks": total_marks,
            "percentage": f"{ (marks/total_marks)*100:.2f}%" if total_marks else "0.00%",
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        data[username]['scores'].append(score_record)
        save_data(data)
        print("Quiz score recorded successfully.")
    else:
        print("Error: User not found.")

def show_profile(data, username):
    
    if username not in data:
        print("Error: Profile not found.")
        return

    user_data = data[username]
    print("\n--- Student Profile ---")
    
  
    for key, value in user_data.items():
        if key not in ["password", "scores"]:
            print(f"{key.replace('_', ' ').title()}: {value}")
    
    print("\n--- Quiz History ---")
    if user_data.get('scores'):
        for i, score in enumerate(user_data['scores'], 1):
            print(f"  {i}. Category: {score['category']}, Marks: {score['marks']}/{score['total_marks']} ({score['percentage']}), Date: {score['datetime']}")
    else:
        print("  No quiz scores recorded yet.")

    print("-----------------------")

def update_profile(data, username):
   
    if username not in data:
        print("Error: User not found.")
        return

    print("\n--- Update Profile ---")
    
  
    updatable_keys = ["name", "email", "branch", "year", "contact"]
    
    for key in updatable_keys:
        current_value = data[username].get(key, 'N/A')
        new_value = input(f"Enter new {key.replace('_', ' ').lower()} (current: {current_value}, press Enter to skip): ")
        if new_value:
            data[username][key] = new_value
    
   
    new_password = input("Enter new password (press Enter to keep old one): ")
    if new_password:
        data[username]["password"] = new_password
            
    save_data(data)
    
    
    global STUDENTS_DATA 
    STUDENTS_DATA = load_data() 
    
    print("Profile updated successfully!")



def main():
    global STUDENTS_DATA
    STUDENTS_DATA = load_data()
    logged_in_user = None
    user_type = None 

    while True:
        print("\n--- Quiz App Menu ---")
        
        
        if not logged_in_user:
            print("1. Register (1. registration)")
            print("2. Login (2. login (user and admin))")
            print("4. Exit (4. exit)")
            menu_options = ["1", "2", "4"]
       
        elif user_type == "user":
            print("3. Attempt Quiz (3.2 attempt quiz)")
            print("5. Update Profile (3.5 update profile, email, branch, year, contact, name)")
            print("6. Show Profile/Score History (3.6 profile/3.3 score)")
            print("7. Logout (3.4 logout)")
            print("8. Exit (4. exit)")
            menu_options = ["3", "5", "6", "7", "8"]
       
        elif user_type == "admin":
            print("3. Manage Users (Placeholder)")
            print("7. Logout (3.4 logout)")
            print("8. Exit (4. exit)")
            menu_options = ["3", "7", "8"]

        choice = input("Enter your choice: ")

        if choice == "1" and not logged_in_user:
            register(STUDENTS_DATA)

        elif choice == "2" and not logged_in_user:
            logged_in_user, user_type = login(STUDENTS_DATA)

        
        elif choice == "3" and user_type == "user":
            attempt_quiz(STUDENTS_DATA, logged_in_user)
            
        elif choice == "5" and user_type == "user":
            update_profile(STUDENTS_DATA, logged_in_user)

        elif choice == "6" and user_type == "user":
            show_profile(STUDENTS_DATA, logged_in_user)

        elif choice == "7" and logged_in_user:
            print(f"User '{logged_in_user}' logged out successfully (3.4 logout).")
            logged_in_user = None
            user_type = None
            
        elif choice in ("4", "8"): 
            print("Exiting system... Goodbye!")
            break
            
        elif choice in menu_options:
           
            if choice == "3" and user_type == "admin":
                print("\nAdmin options are under development. Use Logout/Exit for now.")

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()