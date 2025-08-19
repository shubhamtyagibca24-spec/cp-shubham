a = float(input("Enter angle a (degrees): "))
b = float(input("Enter angle b (degrees): "))
c = float(input("Enter angle c (degrees): "))

if a <= 0 or b <= 0 or c <= 0 or a + b + c != 180:
    print("Invalid triangle: angles must be positive and sum to 180°.")
else:
    largest = max(a, b, c)
    if largest == 90:
        print("it is right-angled.")
    elif largest < 90:
        print("it is acute.")
    else:
        print("it is obtuse.")