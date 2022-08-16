def main():
    while True:
        try:
            fuel = input("Fraction: ").strip()
            x = int(fuel.split('/')[0])
            y = int(fuel.split('/')[1])
            if x > y or y == 0:
                pass
            else:
                get_level(x,y)
        except ValueError:
            pass

def get_level(x,y):
    percent = round((x/y)*100)
    if percent <= 1:
        print('E')
    elif percent >= 99:
        print('F')
    else:
        print(str(percent)+'%')
    quit()

main()