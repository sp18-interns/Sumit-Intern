def dayofweek(year, month, day):
    x, y = month, day
    if x == 1:
        x = 13
        year -= 1
    elif x == 2:
        x = 14
        year -= 1
    rem = year % 100
    div = year // 100
    f = (y + int(13 * (x + 1) / 5.0) + rem + int(rem / 4.0))
    fg = f + int(div / 4.0) - 2 * div
    fdiv = f + 5 - div
    if year > 1600:
        h = fg % 7
    else:
        h = fdiv % 7
    if h == 0:
        h = 7
    return h


print(dayofweek(1989, 5, 9))
