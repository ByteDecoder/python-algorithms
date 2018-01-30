def get_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fib(n-1) + get_fib(n-2)
