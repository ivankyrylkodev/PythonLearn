def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for i in range(len(s)):
        if i > 0 and s[i-1].isnumeric() and not s[i].isnumeric():
            return False
        if not s[i-1].isnumeric()  and s[i] == "0":
            return False
        if s[i] in "!@#$%^&*()_+=-[]{};':\"\\|,.<>/?":
            return False
    
    if len(s) < 2 or len(s) > 6:
        return False
    elif s[0].isnumeric() or s[1].isnumeric():
        return False
    else:
        return True



main()