num = input("Enter a number: ")
if num[-1] == '5' and sum(int(d) for d in num if d.isdigit()) % 7 == 0:
    print(f"{num} ends with 5 and sum of digits divisible by 7.")
else:
    print("The conditions aren't both satisfied.")
