
#Write a paragraph about introducing you and your selected domain (include Full Name, domain name, register number, year …….).
''' Iam Balla Koushik Pursuing MCA at christ University. I choosed the domain Edu-platform. My register number is 2347217 (2023-24)'''

#Write a python program to count the frequency of any specific word (in your domain) in the paragraph.'''
Eduplatform = "Myself Koushik Balla, I have Choosed eduplatform, 2347217, 2023, eduplatform is a learning platform"
'''Convert the paragraph to lowercase to make the search case-insensitive'''
Eduplatform_lower = Eduplatform.lower()

'''assigning the word to be counted'''
word_to_count = "eduplatform"

'''Split the paragraph into words'''
words =Eduplatform_lower.split()

'''initialize a variable to store the count'''
word_count = 0

'''loop through the words and count the occurrences of the specific word'''
for word in words:
    if word == word_to_count:
        word_count += 1
print("The number of times word repeated is: ",word_count)


#Write a python program to display all the datatypes of selected specific elements in the paragraph. (For example:– name - string, reg.no - int, marks - float, etc.)
def get_data_types_in_list(input_list):
    # Create an empty set to store the data types of elements in the list
    data_types = set()
    # # Iterating through each element in the input_list through each element item in the input_list
    for item in input_list:
        #The __name__ attribute of the class object gives the name of the type as a string.'''
        data_types.add(type(item).__name__)
    return data_types
Edu_2 = ["user","resource","modules","assessments","grades","certificates","payment","reviews"]
# Calling the get_data_types_in_list function
result = get_data_types_in_list(Edu_2)
print(result)
 


#Write a python program to count the number of alphabets, numeric and other special symbols in the paragraph
alpha = 0
number =0
special = 0
Eduplatform = "onlinecoaching,2023"
for i in Eduplatform:
    if (i.isalpha()):
        alpha +=1
    elif (i.isdigit()):
        number+=1
    else:
        special+=1
print("Number of Alphabets is: ",alpha)
print("number of digits are:",number)
print("number of special characters are:",special)



#creating a set with domain contents
set1 = {"user","course","enrollment","payment","discussionforum","notifications","assessment","tutor","grades"}
#printing a created set.
print(set1)

#poping a element from set.
set1.pop()
print(set1)

#discarding the element tutor from set.
set1.discard("tutor")
print(set1)

#removing a item from set
set1.remove("payment") 
print(set1)

#clearing the set.
set1.clear()
print(set1)



#updating the set with 5 attributes of my domain name
set1 = {"user","course","enrollment","payment","discussionforum","notifications","assessment","tutor","grades"}
set2 = {"modules","certificate","progress","comments","resources"}
set1.update(set2)
print(set1)
list1 = list(set1)
sortedlist1 = sorted(list1 ,reverse=True)
sorted_set = set(sortedlist1)
print(sorted_set)

#creating a tuple, packing and unpacking
tup1 = (1010,"edu","grades")
(id,platform,assessments) = tup1
print(id)
print(platform)
print(assessments)

#Enter your domain name as characters and count any number of characters and print the count (for example – (‘p’,’r’,’o’,’g’,’r’,’a’,’m’) count of ‘r’ = 2)
char_of_domain = ('e','d','u','p','l','a','t','f','o','r','m','a','p','p')
char_to_search = "a"
char_count = char_of_domain.count(char_to_search) 
print(f"Count of '{char_to_search}' = {char_count}")

#Enter your domain name, execute all the slicing possibilities and also negative indexing.
tup1 = ("user","resource","modules","assessments","grades","certificates","payment","reviews")
print(tup1[0:4])
print(tup1[0:7])
print(tup1[::-1])
print(tup1[0:1])
print(tup1[-3:])
print(tup1[1:6:2])
print(tup1[-4:-1])
print(tup1[2:4])
print(tup1[5])


