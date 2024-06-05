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
    if num2 == 0:
        print("Can't divide a number by zero")
    else:
        print(f'Result is {result}')


def divide(num1, num2):
    """This will produce the division of two numbers"""
    
    result = num1/num2
    print(f'Result is {result}')
    

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
        
        
        num1 = int(input("enter the first digit:  "))
        num2 = int(input("enter the second digit:  "))
        
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
