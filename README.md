# Salary and Bonus Calculator

This is a simple Python program that prompts the user for their name, monthly salary, and bonus percentage. It calculates the total bonus amount, greets the user, and displays their salary and the calculated bonus.

---

## Features

- Prompt the user to input:
  - Their **name**.
  - Their **monthly salary**.
  - The **bonus percentage**.
- Calculate the total bonus based on the salary and bonus percentage.
- Display a personalized message with the salary and bonus information.
- Includes a brief delay for better user experience.

---

## Prerequisites

- Python 3.x installed on your machine.

---

## How to Run

1. Copy the following code into a Python file, e.g., `salary_bonus_calculator.py`:

   ```python
   import time

   nome = input("Enter your name: ")

   salario = float(input("Enter your salary: "))

   bonus = float(input("Enter the bonus percentage: "))

   calculo_bonus = 1000 + salario * bonus

   print("We are calculating your bonus...")

   time.sleep(5)

   print(f"CONGRATULATIONS {nome} !!! Your salary is {salario} and your value bonus is {calculo_bonus}")
