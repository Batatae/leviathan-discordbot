dif = {
    "miau":(5, 10),
    "juaj":3
}

letter = input("Digite: ").lower()

if letter in dif:
    print(f"miau miau, {dif[letter][0]} e {dif[letter][1]}")