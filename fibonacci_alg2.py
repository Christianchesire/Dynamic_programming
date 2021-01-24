""" Using functool lru cache """

from functools import lru_cache

@lru_cache(maxsize = 1000)
def fib(n):
    if n <= 2:
      return 1
    else:
      return fib(n-1) + fib(n-2)

for i in range(1,201):
    print("fib({}) = ".format(i), fib(i))

