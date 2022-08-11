#sum current and previous number in range(10)

print("Printing current and previous number sum in a range(10)")
for i in range(10):
    current = i
    if i == 0:
        prev = 0
    sum = current + prev
    print('Current Number {} Previous Number  {}  Sum:  {}'.format(current, prev, sum))
    prev = i
  