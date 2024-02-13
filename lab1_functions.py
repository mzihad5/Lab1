# File: lab1_functions.py

def calculate_age():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = int(input("Enter the current year: "))
        age = current_year - birth_year
        print("Your age is:", age)
    except ValueError:
        print("Invalid input. Please enter valid years.")

# Test the function
if __name__ == "__main__":
    calculate_age()
