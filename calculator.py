def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    return x/y


print ("Simple Calculator")
while True:
        print("\nPlease select an option")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter your choice: ")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
       
        if choice == "1":
            print("Result is: ",num1,"+",num2,"=",sum(num1,num2))
        elif choice == "2":
            print("Result is: ",num1,"-",num2,"=",sub(num1,num2))
        elif choice == "3":
            print("Result is: ",num1,"*",num2,"=",mul(num1,num2))

        elif choice == "4":
            print("Result is: ",num1,"/",num2,"=",div(num1,num2))  
            break
        elif choice == "5":
            print("Exiting the program")

        else:
            print("Invalid choice. Please try again.")

