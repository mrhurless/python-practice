"""
implement a program that prompts the user for a date, anno Domini, in 
month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
wherein the month in the latter might be any of the values in the list 
below:


Then output that same date in YYYY-MM-DD format. If the user’s input is 
not a valid date in either format, prompt the user again. Assume that every 
month has no more than 31 days; no need to validate whether a month has 
28, 29, 30, or 31 days.
"""

def main():

    months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]

    while True:
        try:
            date = input('Date: ').strip().title()

            if date.find('/') > 0:
                date_parts = date.split('/')
                m, d, y = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
                if check_date_nums(m, d, y):
                    print(str(y) + '-' + f"{m:02d}" + '-' + f"{d:02d}")
                    break
                else:
                    pass
            else:
                split = date.split()

                if split[0] in months and split[1][-1] == ',' and int(split[2]) <= 9999:
                    d = int(split[1][:-1])
                    if 1 < d < 32:
                        m = months.index(split[0]) + 1
                        y = int(split[2])
                        
                        print(f'{y:04d}' + '-' + f"{m:02d}" + '-' + f"{d:02d}")
                        break
                    else:
                        pass
                else:
                    pass

        except ValueError:
            pass


def check_date_nums(m, d, y):
    
    valid = False

    if 0 < m < 13 and 1 < d < 32 and 999 < y < 10000:
        valid = True
    else:
        pass
    
    return valid

main()