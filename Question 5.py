# Question 6. Write a python program to remove items in a list containing the character 'a' or 'A'. 
# Use lambda function for it. For this program pass in as argument the list:
#  list_a = ["car", "place", "tree", "under", "grass", "price"] to the lambda function named remove_items_containing_a_or_A.

# Final output:

# ['tree', 'under', 'price']



list_a = list(map(str,input().split(',')))

remove_items_containing_a_or_A = lambda x: [item for item in x if 'a' not in item.lower()]

filtered_list = remove_items_containing_a_or_A(list_a)
print("Filtered list:", filtered_list)