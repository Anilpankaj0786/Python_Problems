# sum of prime digits
n = int(input("Enter the digit: "))
sum_prime = 0

while n > 0:
    digit = n % 10  # Extract the last digit
    if digit in {2, 3, 5, 7}:  # Check if the digit is prime
        sum_prime += digit
    n //= 10  # Remove the last digit

print("Sum of prime digits:", sum_prime)
