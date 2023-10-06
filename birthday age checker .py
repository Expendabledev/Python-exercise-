from datetime import datetime

def calcu_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

birthdate1 = input("Enter your birthdate (YYYY-MM-DD): ")

try:
    birthdate = datetime.strptime(birthdate1, "%Y-%m-%d")
    age = calcu_age(birthdate)
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD format.")
