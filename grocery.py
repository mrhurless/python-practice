def main():
    list = dict()

    while True:
        try:
            item = input().strip().upper()
            if not item in list:
                list.update({item:1})
            else:
                list[item] += 1 
        except EOFError:
            print('\n')
            for key,value in sorted(list.items()):
                print(str(value) + ' ' + key)
            break
main()