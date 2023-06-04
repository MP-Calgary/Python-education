import random

def generate_random_set(num_integers):
    random_set = set()
    while len(random_set) < num_integers:
        random_set.add(random.randint(1, 500))
    return random_set

# Example usage
num_integers = 25  # Number of integers to generate in the set

random_set = generate_random_set(num_integers)

# Print the generated set
print("Random Set:", random_set)
