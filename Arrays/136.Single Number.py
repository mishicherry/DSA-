"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Approach:
          1. Using Bitwise operator(XOR):      TC: O(N)     SC: O(1)
            -> XOR of a number with itself is 0. 
            
          2. Using Count():           TC: O(N)     SC: O(1)
            -> Trverse through the array check.
            -> Check if count of an element = 1.
            -> If it is equal to 1, return num[i].
            
         Leetcode:  https://leetcode.com/problems/single-number/submissions/
"""
#BITWISE
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        
        for i in nums:
            res = i ^ res
            
        return res
      
#Count()
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
         for i in nums:
            if(nums.count(i) == 1):
                return(i)
