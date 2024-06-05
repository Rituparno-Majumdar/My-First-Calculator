def add(num1, num2):
    """This will produce the sum of two numbers"""
   
    result = num1 + num2
    print(f'Result is {result}')


def subtract(num1, num2):
    """This will produce the subtraction of two numbers """
    
    result = num1 - num2 
    print(f'Result is {result}')


def multiply(num1, num2):
    """This will produce the multiplication of two numbers"""
    
    result = num1 * num2
    print(f'Result is {result}')


def divide(num1, num2):
    """This will produce the division of two numbers"""
        
    try:
        result = num1 / num2
        print(f'Result is {result}')
    except ZeroDivisionError:
        print("You can't divide a number by zero")

def main():
    print("Welcome to Simple Calculator. ")
    
    while True:

        print('\n 1. Addition')
        print('\n 2. Subtraction')
        print('\n 3. Multiplication')
        print('\n 4. Division')
        print('\n 5. Exit')
        
        choice = input('Choose your operation: ')
        
        if choice == '5':
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
           
            continue
        
        if choice == '1':
            add(num1, num2)
        elif choice == '2':
            subtract(num1, num2)
        elif choice == '3':
            multiply(num1, num2)
        elif choice == '4':
            divide(num1, num2)
        else:
            print("Invalid Option1")
        

if __name__ == "__main__":
    main()
