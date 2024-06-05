# Simple Calculator

A simple command-line calculator that can perform addition, subtraction, multiplication, and division of two numbers.

## Features

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/simple-calculator.git
    cd simple-calculator
    ```

2. Run the calculator:
    ```sh
    python calculator.py
    ```

3. Follow the on-screen instructions to perform calculations.

## Functions

### add(num1, num2)
This function takes two numbers and prints their sum.

```python
def add(num1, num2):
    """This will produce the sum of two numbers"""
    result = num1 + num2
    print(f'Result is {result}')
