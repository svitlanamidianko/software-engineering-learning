import math

# BIGFACTOR represents the product of all prime factors under 100.  This allows
# us to do a fast pre-check and immediately eliminate any numbers which are
# divisible by a small number

BIGFACTOR = 1
for num in range(1, 101):
    if BIGFACTOR % num != 0:
        BIGFACTOR = BIGFACTOR * num

class InvalidInput(Exception): 
    '''The value cannot be larger than 62'''
    pass
def is_prime(x):
    ''' Test whether x is a prime number.'''
    # Check for all possible prime factors under 100:
    if x % BIGFACTOR == 0:
        return False
    # The fast check failed, now perform exhaustive check.
    print('here', x)
    max_factor = int(math.sqrt(x))
    print('max fa', max_factor)
    for a in range(101, max_factor, 100):
        if not (x % a):
            return False
    return True


def get_next_prime(x):
    ''' Find the smallest prime number which is greater than or equal to x.'''
    if x > 62: 
        raise InvalidInput
    if x % 2 == 0:
        x = x + 1
    while not is_prime(x):
        print('we are trying to add 2 to:', x)
        x = x + 2

    return x
