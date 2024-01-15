import re

def is_password_strong(password):

    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

  
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    if not any(char in '!@#$%^&*()-_=+[]{}|;:\'",.<>?/~`' for char in password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets the strength criteria."


password_input = input("Enter your password: ")

result = is_password_strong(password_input)
print(result)
