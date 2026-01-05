# Task 2: Demonstrate List Slicing
# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

original_list = []

for i in range(1,11):
    original_list.append(i)
print(f"Original list: {original_list}")

extracted_list = original_list[0:5]
print(f"Extracted first five elements: {extracted_list}")

revered_ext_list = []
counter = -1
for i in extracted_list:
    revered_ext_list.append(extracted_list[counter])
    counter -= 1
print(f"Reversed extracted elements: {revered_ext_list}")



