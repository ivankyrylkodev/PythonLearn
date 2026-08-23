expression = input("Expression: ").strip().lower()

x, symb, y = expression.split(" ")

match symb:
    case "+":
        print(float(x) + float(y))
    case "-":
        print(float(x) - float(y))
    case "*":
        print(float(x) * float(y))
    case "/":
        print(float(x) / float(y))
    case _:
        print("Unknown operation")