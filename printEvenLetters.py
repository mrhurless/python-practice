#Write a program to accept a string from the user and display characters 
# that are present at an even index number.

#For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

string = input('Enter a string: ')
print('Original string is {}'.format(string))
print('Printing only even index characters:')
for index, i in enumerate(string):
    if index % 2 == 0:
        print(i)
    