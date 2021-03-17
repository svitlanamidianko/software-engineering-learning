import numpy as np
import prime

# This application uses two large prime numbers to implement public key
# cryptography. It generates a public key and a private key.  The
# keys are symmetric, so if one key is used to encrypt, then the other can be
# used to decrypt.
ii64 = np.iinfo(np.int64)
print('The min and max that np.int64 can hold is ',ii64.min, ii64.max)
p1 = prime.get_next_prime(np.int64(2**63 - 1))
print('---p1 is',p1)
p2 = prime.get_next_prime(np.int64(2**62 - 1))

print('---p2 is',p2)

# Now we have found two large prime numbers and can start to perform public
# key cryptography.
# ...
# Pretend that there was more code here.
