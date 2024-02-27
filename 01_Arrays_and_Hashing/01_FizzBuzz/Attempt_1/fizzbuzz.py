from typing import List

"""
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]

Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
    
        counter = 1
        while counter < n + 1:
            if counter % 3 == 0 and counter % 5 == 0:
            # print("FizzBuzz")
                result.append("FizzBuzz")
        
            elif counter % 3 == 0:
            #  print("Fizz")
                result.append("Fizz")
                
            elif counter % 5 == 0:
            # print("Buzz")
                result.append("Buzz")
                
            else:
                result_n = str(counter)
            #  print(counter)
                result.append(result_n)
                
            counter += 1
            
        print(result)   
        return result
    

# solution_instance = Solution()
    
# # Test case 1: n = 1
# solution_instance.fizzBuzz(1)

# # Test case 2: n = 9
# solution_instance.fizzBuzz(9)
                                                
# # Test case 3: n = 17
# solution_instance.fizzBuzz(17)
