import os
# clear the terminal 
os.system('clear')

def francois_algorithm(n):
    while n != 0:
        sequence = [1, 2]   # Note [1%2]=[1] and [2%2]=[0]
        if n > 2:
            for index in range(3, n+1):
                sequence[index % 2] = sequence[0] + sequence[1]
        return sequence[n % 2]
    
# Test the function
n = 10
result = francois_algorithm(n)
print(f"The modified François sequence up to the {n}th term:")
print(result)
