import os
# clear the terminal 
os.system('clear')

def francois_algorithm(n):
    if n == 1:
        return [2]
    elif n == 2:
        return [2, 1]
    
    sequence = [2, 1]
    
    for _ in range(3, n + 1):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    return sequence

# Test the function
n = 10
result = francois_algorithm(n)
print(f"The modified François sequence up to the {n}th term:")
print(result)
