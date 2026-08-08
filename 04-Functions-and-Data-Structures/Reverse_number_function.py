def reverse_no():
    num = int(input("Enter a number: "))  # 234
    rev = 0
    rem = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10  # Use floor division to ensure num remains an integer
    return rev

print(reverse_no())
