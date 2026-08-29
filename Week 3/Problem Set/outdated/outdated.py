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
        user_date = input("Date: ").strip()
        if "/" in user_date:
            m, d, y = user_date.split("/")
            if 0 < int(m) < 12:
                if (int(m) in [1, 3, 5, 7, 8, 10, 12] and 0 < int(d) <= 31) or (int(m) == 2 and 0 < int(d) < 29) or (int(m) in [4, 6, 9, 11] and 0 < int(d) <= 30):
                    print(f"{int(y)}-{int(m):02}-{int(d):02}")
                    break
                else:
                    pass
            else:
                pass
        else:
            md, y = user_date.split(",")
            str_m, d = md.split(" ")
            if str_m in months:
                m = months.index(str_m) + 1
                if (int(m) in [1, 3, 5, 7, 8, 10, 12] and 0 < int(d) <= 31) or (int(m) == 2 and 0 < int(d) < 29) or (int(m) in [4, 6, 9, 11] and 0 < int(d) <= 30):
                    print(f"{int(y)}-{int(m):02}-{int(d):02}")
                    break
                else:
                    pass
            else:
                pass
    except EOFError:
        break
