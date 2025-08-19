number = int(input("Enter a number: "))
last_digit = int(str(number)[-1])

if last_digit == 4:
    print("The last digit is 4.")
else:
    print(f"The last digit is {last_digit}, not 4.")  
    