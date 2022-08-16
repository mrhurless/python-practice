def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0.00

    while True:    
        try:
            item = input("Item: ").strip().lower().title()
            if item in menu:
                total = round(total + menu[item],2)
                print("Total: " + "${:.2f}".format(total))
            else:
                pass
        except EOFError:
            break

main()