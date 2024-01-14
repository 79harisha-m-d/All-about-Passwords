import random
import string
import datetime

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, used=False):
    status = "Used" if used else "Unused"
    filename = f"{status.lower()}_passwords.txt"
    with open(filename, "a") as file:
        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} ({status}): {password}\n")

def read_last_5_days(used=False):
    status = "Used" if used else "Unused"
    filename = f"{status.lower()}_passwords.txt"
    passwords = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            passwords = [line.strip() for line in lines if f"({status}):" in line]
    except FileNotFoundError:
        pass 
    return passwords[-5:]

if __name__ == "__main__":
    
    new_password = generate_password()
    print(f"Generated Password: {new_password}")

    
    used_password = input("Have you used this password? (yes/no): ").lower()

    if used_password == "yes":
        save_password(new_password, used=True)
    else:
        save_password(new_password)

  
    last_5_days_passwords_unused = read_last_5_days()
    print("\nUnused passwords generated for the last 5 days:")
    for password_entry in last_5_days_passwords_unused:
        print(password_entry)

  
    last_5_days_passwords_used = read_last_5_days(used=True)
    print("\nUsed passwords generated for the last 5 days:")
    for password_entry in last_5_days_passwords_used:
        print(password_entry)
