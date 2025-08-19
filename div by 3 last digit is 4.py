num = input("Enter a number: ")
if num[-1] == '4' and sum(int(d) for d in num if d.isdigit()) % 3 == 0:
    print(f"{num} ends with 4 and sum of digits divisible by 3.")
else:
    print("The conditions aren't both satisfied.")

