import re

# Write a program to find all email addresses in a string.
line_in_1 = 'he Uladzislau_Vysotski@epam.com asdfv SD fd uladzislau_vysotski@gmail.com'
for i in re.findall(r'[\w\.-]+@[\w\.-]+', line_in_1):
    print(i)
print()

# Write a program to find all three, four, five characters long words string.
line_in_2 = 'I am in love with the craps'
print(re.findall(r'\b\w{3,5}\b', line_in_2))
print()

# Write a program to separate and print the numbers of a given string.
line_in_3 = 'Avasd 20 adfahdf 27'
for i in re.findall(r'\d+', line_in_3):
    print(i)
print()

# Write a program to replace whitespaces with an underscore and vice versa.
line_in_4 = 'I love_to do.'
print(line_in_4)
line_in_4 = line_in_4.replace(" ", "_")
print(line_in_4)
line_in_4 = line_in_4.replace("_", " ")
print(line_in_4)
