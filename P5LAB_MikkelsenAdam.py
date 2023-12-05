def days_in_feb(user_year):
    days = int(28)
    if (user_year % 4) == 0:
        if (user_year % 100) == 0:
            if (user_year % 400) == 0:
                days = 29
        else:
            days = 29
    else:
        days = 28
    return days

if __name__ == '__main__':
    user_year = int(input())
    print(f'{user_year} has {days_in_feb(user_year)} days in February.')
    