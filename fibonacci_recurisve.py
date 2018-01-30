# Adding memoization to improve the function performance
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
def get_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fib(n-1) + get_fib(n-2)

# Decorating the function with memoization
get_fib = memoize(get_fib)
