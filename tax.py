#Taxable Income	Rate (in %)
#First $10,000	0
#Next $10,000	10
#The remaining	20

#Expected Output:

#For example, suppose the taxable income is 45000 the income tax payable is
#10000*0% + 10000*10%  + 25000*20% = $6000.

def calc_tax(income):
    tax = 0
    if (income > 10000) and (income <= 20000):
        tax = (income - 10000) *.1
    elif income > 20000:
        tax = (10000*.1) + ((income - 20000)*.2)
    return str(tax)

income = int(input("Enter your income: "))
print("Your tax amount is: $" + calc_tax(income))
