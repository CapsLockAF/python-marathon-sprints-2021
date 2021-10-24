# Create function-generator divisor that should return all divisors
# of the positive number.
# If there are no divisors left function should return None.
# three = divisor(3)
# next(three) => 1
# next(three) => 3
# next(three) => None

def divisor(n):
    yield 1
    for i in range(2, n+1):
        if n / i == int(n / i):
            yield i
    while True:
        yield None

