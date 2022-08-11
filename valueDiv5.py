#Given list is  [10, 20, 33, 46, 55]
#Divisible by 5
#10
#20
#55

list = [10, 20, 33, 46, 55]
print('Given list is {}'.format(list))
print('Divisible by 5')
for i in list:
    if (i % 5) == 0:
        print(i) 
