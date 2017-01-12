def fibonacci(n, computed = {0: 0, 1: 1}):
    # this function is slow - O(2^n) slow
    # to speed it up, save the values.

    if n not in computed:
        computed[n] = fibonacci(n - 1, computed) + fibonacci(n - 2, computed)
    return computed[n]


print(fibonacci(5))
