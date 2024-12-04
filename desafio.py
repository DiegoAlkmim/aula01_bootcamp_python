""" Write a Python program that asks the user to enter their name, their monthly salary, 
and the bonus amount they received. The program should then print a message greeting 
the user by name and informing them of the salary amount compared to the bonus received. """

import time

nome = input("Enter your name: ")

salario = float(input("Enter your salary: "))

bonus = float(input("Enter the bonus percentage: "))

calculo_bonus = 1000 + salario * bonus

print("We are calculating your bonus...")

time.sleep(5)

print(f"CONGRATULATIONS {nome} !!! Your salary is {salario} and your value bonus is {calculo_bonus}")