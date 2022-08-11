def donuts(count):
  string = 'Number of donuts: {}'
  if count >= 10:
    string = string.format('many')
  else:
    string = string.format(count)
  print(string)

donuts(4)#, 'Number of donuts: 4'
donuts(9)#, 'Number of donuts: 9')
donuts(10)#, 'Number of donuts: many')
donuts(99)#, 'Number of donuts: many')