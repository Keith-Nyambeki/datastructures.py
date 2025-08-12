# Step 1: Create an empty list called my_list
my_list = []  # This initializes an empty list
print("Step 1 - Empty list:", my_list)

# Step 2: Append the elements 10, 20, 30, 40 to my_list
my_list.append(10)  # Adds 10 at the end
my_list.append(20)  # Adds 20 at the end
my_list.append(30)  # Adds 30 at the end
my_list.append(40)  # Adds 40 at the end
print("Step 2 - After appending elements:", my_list)

# Step 3: Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)  # Inserts 15 at position 2 (index 1)
print("Step 3 - After inserting 15 at index 1:", my_list)

# Step 4: Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])  # Adds all elements from [50, 60, 70]
print("Step 4 - After extending with [50, 60, 70]:", my_list)

# Step 5: Remove the last element from my_list
my_list.pop()  # Removes the last element
print("Step 5 - After removing the last element:", my_list)
# Step 6: Sort my_list in ascending order
my_list.sort()  # Sorts the list from smallest to largest
print("Step 6 - After sorting:", my_list)

# Step 7: Find and print the index of the value 30
index_30 = my_list.index(30)  # Finds the position of 30 in the list
print("Step 7 - The index of 30 in my_list is:", index_30)

