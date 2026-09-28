numbers = int(input("Enter the number: "))
digit_sum = 0

while numbers > 0:
    last_digit = numbers % 10
    digit_sum += last_digit
    numbers //= 10

print(f"The sum of the digits is: {digit_sum}")

