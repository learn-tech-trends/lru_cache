from functools import lru_cache
import time
start = time.time()
@lru_cache(maxsize=20)
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fib = fibonacci(35)
print(fib)
end = time.time()
print(f'Time taken : {end-start} seconds')
