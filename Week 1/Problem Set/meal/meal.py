def main():
    time = input("What time is it? ").strip().lower()
    con_time = convert(time)
    if 7 <= con_time <= 8:
        print("breakfast time")
    elif 12 <= con_time <= 13:
        print("lunch time")
    elif 18 <= con_time <= 19:
        print("dinner time")


def convert(time):
    time = time.split(":")
    return int(time[0]) + int(time[1])/60


if __name__ == "__main__":
    main()