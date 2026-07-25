"""def is_even(n):
    if n % 2== 0:
        return True
    else:
        return False
print(is_even(1))"""
"""
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result= result*i
    return result

print(factorial(64))"""
   
def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, n):
        if n % i==0:
            return False
        else:
            return True
print(is_prime(4))"""

    
