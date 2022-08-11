#Given a two list of numbers, write a program to create a new list such that 
# the new list should contain odd numbers from the first list 
# and even numbers from the second list.
#Given:
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

#Expected Output:
#result list: [25, 35, 40, 60, 90]

def new_list(src1, src2):
    newList = []
    for i in src1:
        if i % 2 != 0:
            newList.append(i)
    for i in src2:
        if i % 2 == 0:
            newList.append(i)
    return newList        

print(new_list(list1,list2))

