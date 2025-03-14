def calculate_fine(returned, due):
    day_r, month_r, year_r = map(int, returned_date)
    day_d, month_d, year_d = map(int, due_date)

    if year_r < year_d or (year_r == year_d and month_r < month_d) or (year_r == year_d and month_r == month_d and day_r <= day_d):
        return 0
    elif year_r == year_d and month_r == month_d:
        return (day_r - day_d) * 15
    elif year_r == year_d and month_r > month_d:
        return (month_r - month_d) * 500
    else:
        return 10000


returned_date = input().split()
due_date = input().split()

fine = calculate_fine(returned_date, due_date)
print(fine)
