#Strings and string manipulation: Create a program that prompts the user for a string and then prints out the string reversed.

# Prompt the user for a string
user_input = input("Enter a string: ")

# Reverse the string using slicing
reversed_string = user_input[::-1]

# Display the reversed string
print("Reversed string:", reversed_string)
