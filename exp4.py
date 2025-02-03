##  Lists and arrays: Create a program that prompts the user for a list of numbers and then sorts them in ascending order.

# Prompt the user for a list of numbers
numbers = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
num_list = list(map(int, numbers.split()))

# Sort the list in ascending order
num_list.sort()

# Display the sorted list
print("Sorted numbers in ascending order:", num_list)
