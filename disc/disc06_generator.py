def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

# The (lambda t: ...) part is a function and (gen_fib()) is then a call on this func. In the func, an iterator is taken as an argument (specifically here, the gen_fib() func is a generator). This func returns a list which creates every item of itself by calling next() on the iterator.
print((lambda t: [next(t) for _ in range(10)])(gen_fib()))

print(next(filter(lambda n: n > 2025, gen_fib())))