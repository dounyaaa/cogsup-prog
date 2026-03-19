"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    return (n%d==0)
    pass

def is_prime(n):
    is_prime=True
    for i in range(2, n):
        if (n%i==0):
            is_prime=False
            return
    return is_prime
    pass

list_of_primes = [i+1 for i in range(1000) if is_prime(i+1)]
print(list_of_primes)