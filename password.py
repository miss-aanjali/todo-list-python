import string

def check_password_strength(password):
    length = len(password) >= 8
    digit = any(char.isdigit() for char in password)
    uppercase = any(char.isupper() for char in password)
    symbol = any(char in string.punctuation for char in password)

    score = 0
    if length:
        score += 1
    if digit:
        score += 1
    if uppercase:
        score += 1
    if symbol:
        score += 1

    if score <= 1:
        return "Weak"
    elif score == 2 or score == 3:
        return "Medium"
    else:
        return "Strong"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print("Password strength:", strength)

main()
