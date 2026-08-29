def main():
    frac = get_fraction()
    if frac <= 1:
        print("E")
    elif frac >= 99:
        print("F")
    else:
        print(f"{frac}%")

def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").strip().split("/")
            if int(x) < 0 or int(y) < 0 or int(x) > int(y):
                pass
            else:
                return int(int(x) / int(y) * 100)
        except (ValueError, ZeroDivisionError):
            pass

main()