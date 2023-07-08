def calculate_primes(number):
    numbers = [True] * (number + 1)
    numbers[0] = numbers[1] = False
    primes = []

    for factor in range(2, int(number ** 0.5) + 1):
        if numbers[factor]:
            for multiple in range(factor * 2, number + 1, factor):
                numbers[multiple] = False

    for index in range(2, number + 1):
        if numbers[index]:
            primes.append(index)

    return primes

# Prompt the user for input
n = int(input("Enter a number: "))

# Calculate primes up to n
result = calculate_primes(n)

# Display the primes on one line with commas
print("Prime numbers up to", n, ":")
print(", ".join(map(str, result)))
