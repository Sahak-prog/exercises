date1 = {'month': 5, 'year': 2020}
print(f"Date 1: is{date1}")
date2 = {'month': 8, 'year': 2021}
print(f'Date 2: is {date2}')
date3_month = int(input("Enter the month of the third date: "))
date3_year = int(input("Enter the year of the third date: "))
date3 = {'month': date3_month, 'year': date3_year}
if date1['year'] <= date3['year'] <= date2['year']:
    if date1['year'] == date3['year']:
        if date1['month'] <= date3['month']:
            print("The third date falls between the first and second dates.")
        else:
            print("The third date is before the first date.")
    elif date2['year'] == date3['year']:
        if date3['month'] <= date2['month']:
            print("The third date falls between the first and second dates.")
        else:
            print("The third date is after the second date.")
    else:
        print("The third date falls between the first and second dates.")
else:
    print("The third date is outside the range of the first and second dates.")