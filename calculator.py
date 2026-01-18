def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return("Error! divided by zero")
    else:
        return a / b
        
def main():
    print("Simple calculator")
    print("1. Addition")
    print("2. Subtruction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter a number between 1-4: ")
    a= float(input("Enter the first number: "))
    b= float(input("Enter the second number: "))
    
    if choice == "1":
        print("Result", add(a,b))
    elif choice == "2":
        print("Result", sub(a,b))
    elif choice == "3":
        print("Result", mul(a,b))
    elif choice == "4":
        print("Result", div(a,b))
    else:
        print("Your choice is incorrect,please choose a right one!")

main()
            