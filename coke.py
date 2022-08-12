def main():
    due = 50
    print('Amount Due:' + str(due))

    while due <= 50:
        coin = int(input('Insert Coin: '))
        acceptable = [5,10,25]
        
        if coin in acceptable:
            if due > coin:
                due = due - coin
            elif coin == due:
                due = due - coin
                print(f'Amount Due: {due}')
                break
            else:
                change = abs(due - coin)
                print('Change Owed: ' + str(change))
                break       
        print('Amount Due: ' + str(due)) 

main()