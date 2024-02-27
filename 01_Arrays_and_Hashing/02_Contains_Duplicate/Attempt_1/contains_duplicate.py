from typing import List

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #print("original list: ", nums)
        sorted_list = sorted(nums)
        #print("sorted list: ", sorted_list)

        list_range = len(sorted_list)
        for num in range(list_range - 1):
            if sorted_list[num] == sorted_list[num + 1]:
                print(True)
                return True

        print(False)  
        return False
        
# solution_instance = Solution()
# nums1 = [1, 2, 3, 4, 5, 1]
# nums2 = [1, 2, 3, 4]
# nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

# result1 = solution_instance.containsDuplicate(nums1)
# result2 = solution_instance.containsDuplicate(nums2)
# result3 = solution_instance.containsDuplicate(nums3)
