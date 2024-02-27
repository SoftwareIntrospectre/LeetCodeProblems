"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""

# from typing import str

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            print(True)
            return True
        
        else:
            print(False)
            return False
        
# solution_instance = Solution()
# solution_instance.isAnagram("care", "race")
# solution_instance.isAnagram("cart", "trace")
# solution_instance.isAnagram("racecar", "carrace")