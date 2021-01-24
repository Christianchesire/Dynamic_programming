
""" Defining fibonacci using memoization """

# Creating an empty dictionary, to store values for inceased calculation speed
memo = {}
def fib(n):
    if n in memo:
      return memo[n]
    elif n <= 2:
      return 1
    else:
     value = fib(n-1) + fib(n-2)
     memo[n] = value
     return value

print(fib(3))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
