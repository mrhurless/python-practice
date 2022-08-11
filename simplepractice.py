number1 = 20
number2 = 30

def solve(x,y):
    if (x*y) < 1000:
        return (x*y)
    else:
        return (x+y)


#solve(number1, number2)

print("The result is "+ str(solve(number1,number2)))