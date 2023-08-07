# Create a LIST with your domain attributes, insert the elements using the append (), insert(), extend() and add any iterables (tuples, sets, dictionaries etc.) to the list (Use all the methods ).
edu_plat= ["user", "course", "enrollment", "payment"]
edu_plat.append("resources")
edu_plat.insert(2, "modules")
edu_plat.extend(["address", "phone"])
edu_plat.append(("course", "batch"))
edu_plat.insert(0, {"assessment": "grades", "duration": 3})
print("List after inserting elements and iterables:", edu_plat)

#Write a program to swap the first and last elements in a list.

num_list = [13, 95,6, 23, 12, 15, 3]
num_list[0], num_list[-1] = num_list[-1], num_list[0]
print("List after swapping first and last elements:", num_list)

#Write a program to find the sum of the digits in a list.
sum_of_digits = sum(num_list)
print("Sum of digits in the list:", sum_of_digits)

#Write a program to find the smallest element in a list.
smallest_element = min(num_list)
print("Smallest element in the list:", smallest_element)

#2Sort the dictionaries in ascending order based on the Key of the dictionary.
# Sample dictionary
my_dict = {'user': 3, 'tutor': 1, 'assessment': 2, 'grapes': 4}

# Sort the dictionary in ascending order based on keys
sorted_dict = dict(sorted(my_dict.items()))

# Print the sorted dictionary
print(sorted_dict)

#Create the dictionary with Numeric as Value in Key – Value pair and find the sum of all the values in the Dictionary.
# Create the dictionary with numeric values
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40,
    'e': 50
}

# Find the sum of all the values in the dictionary
sum_of_values = sum(my_dict.values())

# Print the sum
print("Sum of all values:", sum_of_values)

# Write a Python code to demonstrate the sorting in descending order of values with lambda function.
# Sample dictionary with numeric values
my_dict = {
    'user': 30,
    'course': 20,
    'enrollment': 40,
    'resourses': 10
}

# Sort the dictionary in descending order of values using lambda function
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

# Print the sorted dictionary
print(sorted_dict)

