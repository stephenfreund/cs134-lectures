# Created by:  Shikha Singh
# Adapted from www.cs111.wellesley.edu/spring19

# Prompt the user to enter their  name and store it for use later
name = input('Enter your name: ')

# Prompt the user to enter their age and store it for use later
age = int(input('Enter your age: '))

# Tell the user how old they will be in 10 years
ageInTen = age + 10

# print outputs
print('Hello, ' + name +'.')  # print a sentence with str concatenation

# Identify the bug in the following piece of code:
print('In 10 years, you will be', age, 'years old.') # print using , as seperator 

