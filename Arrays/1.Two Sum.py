"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Approch:

#1 Brute Force Approach--
    -> Take an empty list.
    -> First Iterate(i) the given list nums from start index(0) to end index(n)
    -> Second Iterate(j) the given list nums for second index(1) to end index(n)
    -> Then check whether i+j = target
    -> if yes then return 
    
    TC: O(n2),  SC: O(1)
    
 # Using Hash Map--
    -> First create an empty dictionary.
    -> Iterate the given list from 0 to n
    -> Also store the value and index in the dictionary
    -> Do diff = target - i
    -> Check whether the diff is in Dictionary or not.
    -> If yes the return the index.
    
    TC: O(n),  SC: O(n)
    
    Leetcode:  https://leetcode.com/problems/two-sum/
 """
Code:

#Brute Force--
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [ ]
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
        
        return res 
    
    
  #Hash Map--
  class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        
        for i, j in enumerate(nums):
            diff = target - j
            
            if diff in check:
                return [check[diff], i]
            
            check[j] = i
            
        return 
