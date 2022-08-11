#Write a program to find how many times substring “Emma” appears in the given string.
#Given: str_x = "Emma is good developer. Emma is a writer"
#Expected Output: Emma appeared 2 times

def count_instances(str,substr):
    count = 0
    split = str.split()
    for i in split:
        if i == substr:
            count += 1
    print('Given string: {}'.format(str))
    print('{} appeared {} times.'.format(substr,count))

str_x = "Emma is good developer. Emma is a writer"
count_instances(str_x,'Emma')
