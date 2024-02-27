import unittest

from valid_anagram import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_isAnagram(self):
        self.assertEqual(self.solution.isAnagram("care", "race"), True)
        self.assertEqual(self.solution.isAnagram("thermonastically", "hematocrystallin"), True)
        self.assertEqual(self.solution.isAnagram("subtraction", "obscurantist"), False)

if __name__ == "__main__":
    unittest.main()