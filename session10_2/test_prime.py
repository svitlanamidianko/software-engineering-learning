import unittest
import prime
class BadInput(unittest.TestCase):
    def test_too_large(self): 
        self.assertRaises(prime.InvalidInput, prime.get_next_prime, 63)

if __name__ == '__main__':
    unittest.main()