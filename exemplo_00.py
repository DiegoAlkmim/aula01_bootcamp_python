# Create a program where the user enters their name and it returns the number of characters.

# Prompt the user to enter their name
nome = input("Enter your name: ")

# Check if the user entered something
if nome.strip():  # Remove leading and trailing spaces
    print(f"Your name has {len(nome)} characters.")
else:
    print("You did not enter a valid name.")
