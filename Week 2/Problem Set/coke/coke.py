insert_coin = 0

while insert_coin < 50:
    print("Amount Due: ", 50 - insert_coin)
    add_coin = int(input("Insert Coin: "))
    if add_coin == 5 or add_coin == 10 or add_coin == 25:
        insert_coin += add_coin
    else:
        continue

print("Change Owed: ", insert_coin - 50)