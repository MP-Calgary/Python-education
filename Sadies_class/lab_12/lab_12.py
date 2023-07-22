def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    prime_numbers = [num for num, is_prime in enumerate(primes) if is_prime]
    return prime_numbers

# Example usage
limit = int(input("Enter a number: "))
prime_numbers = sieve_of_eratosthenes(limit)
print("Prime numbers up to", limit, "are:")
print(prime_numbers)
