from typing import List

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