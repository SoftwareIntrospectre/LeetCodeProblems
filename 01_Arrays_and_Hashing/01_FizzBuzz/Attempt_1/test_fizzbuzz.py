import unittest
from fizzbuzz import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()


    def test_fizzBuzz(self):

        # Test case 1: n = 1
        self.assertEqual(self.solution.fizzBuzz(1), ["1"])

        # Test case 2: n = 9
        self.assertEqual(self.solution.fizzBuzz(9), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz"])
                                                      
        # Test case 3: n = 17
        self.assertEqual(self.solution.fizzBuzz(17), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17"])

if __name__ == "__main__":
    unittest.main()