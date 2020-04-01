# test_math.py
import Math
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the add function from the math library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = Math.add(1, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        """
        Test that the multiplication of two integers returns the correct total
        """
        result = Math.multiply(1, 2)
        self.assertEqual(result, 2)

    def test_divide(self):
        """
        Test that the multiplication of two integers returns the correct total
        """
        result = Math.divide(6, 3)
        self.assertEqual(result, 2)
        self.assertRaises(ZeroDivisionError, Math.divide, 1, 0)

    def test_is_even(self):
        """
        Test that the multiplication of two integers returns the correct total
        """
        result = Math.is_even(6)
        self.assertTrue(result)
        result = Math.is_even(3)
        self.assertFalse(result)

    def test_power(self):
        """
        Test that the multiplication of two integers returns the correct total
        """
        result = Math.power(6, 6)
        self.assertEqual(result, 46656)

    def test_is_prime(self):
        """
        Test that the multiplication of two integers returns the correct total
        """
        self.assertRaises(ValueError, Math.is_prime, -3)
        result = Math.is_prime(0)
        self.assertFalse(result)
        self.assertTrue(Math.is_prime(3))
        self.assertFalse(Math.is_prime(4))
        self.assertTrue(Math.is_prime(7))

    def test_factorial(self):
        """
        Test that the multiplication of two integers returns the correct total
        """
        result = Math.factorial(7)
        self.assertEqual(result, 5040)

    def test_factors(self):
        """
        Test that the multiplication of two integers returns the correct total
        """

        self.assertRaises(ValueError, Math.factors, -3)
        result = Math.factors(1)
        self.assertListEqual(list(range(1, 1)), result, msg=None)
        result = Math.factors(12)
        answer = [1, 12, 3, 4, 6]
        self.assertListEqual(answer, result, msg=None)

if __name__ == '__main__':
    unittest.main()