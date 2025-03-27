def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def menu():
    print("\nPlease select an option")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def  main():
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            print(num1,"+",num2,"=",sum(num1,num2))
        elif choice == "2":
            print(num1,"-",num2,"=",sub(num1,num2))
        elif choice == "3":
            print(num1,"*",num2,"=",mul(num1,num2))

        elif choice == "4":
            
