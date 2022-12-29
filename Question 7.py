# Question 7: Create a custom exception class which can handle "IndexError" as well as "ValueError" such that it can display its own custom error message when we use index which is not valid in a list. Take list as list_a = [1, 2, 3, 4, 5].

# Final output type 1:

# Enter the index = 10
# The index 10 is incorrect and index should lie between -5 and 4.

# Final output type 2:

# Enter the index = abc
# Use an Integer value as the input.

#Program:
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

list_a = [1, 2, 3, 4, 5]

try:
    index = int(input("Enter an index for the list: "))
    if index < 0 or index >= len(list_a):
        raise CustomException("The index is incorrect and index should lie between -5 and 4.")
    print(list_a[index])
except CustomException as e:
    print(e.message)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
