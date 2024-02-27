"""
solution_instance = Solution()
nums1 = [1, 2, 3, 4, 5, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

result1 = solution_instance.containsDuplicate(nums1)
result2 = solution_instance.containsDuplicate(nums2)
result3 = solution_instance.containsDuplicate(nums3)

"""

import unittest

from contains_duplicate import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_containsDuplicate(self):
        self.assertEqual(self.solution.containsDuplicate([1,2,3,4,5,1]), True)
        self.assertEqual(self.solution.containsDuplicate([64,7,92]), False)
        self.assertEqual(self.solution.containsDuplicate([8,6,7,5,3,0,9,12,84,9723,6]), True)

if __name__ == "__main__":
    unittest.main()