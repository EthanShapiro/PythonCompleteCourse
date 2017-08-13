# Ancient algorithm to get all prime numbers within
# up to a given number

def get_primes(limit):
    # create generator of numbers to save space
    # NOTE 2 is first prime so start there
    nums = (x for x in range(2, limit))

    # Create a composite list
    composite = []

    # loop through numbers and add composite to
    # new list
    for p in nums:
        if p in composite:
            continue
        # temp num to increase
        num = p
        # add all numbers up limit that are composite
        while num < limit:
            num += p
            if num not in composite:
                composite.append(num)
    # Create primes
    primes = []

    # get all numbers not in composite
    for num in range(2, limit):
        if num not in composite:
            primes.append(num)

    return primes

primes = get_primes(30)

print(primes)
