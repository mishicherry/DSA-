"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most 
significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Approach:
        -> Reverse the given array(digits).
        -> Set one = 1 and i = 0
        -> Use while loop. while one.
        -> First condition - if i < len(digits).
              A. Nested if : if i == 9: set i = 0 
              B. Else: increment digit by 1 and set one = 0
              
        -> Second Condition.
            Else i > len(digits)--  Append Digit append(!) and set one = 0
            
        Leetcode :  https://leetcode.com/problems/plus-one/submissions/
         
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = digits[::-1]
        one, i = 1, 0
        
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                    
                else:
                    digits[i]+=1
                    one = 0
                    
            else:
                digits.append(1)
                one = 0
                
            i+=1
            
        return digits[::-1]
            
