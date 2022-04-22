"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Approach:
        1. Using Hash-Map: TC: O(N),   SC:O(N)
            -> Create a dictionary.
            -> Set result and maxCount to be 0.
            -> Iterate through the array.
            -> increment count by 1.
            -> Increment result by 1 if count > than maxCount.
            -> Set maxCount by taking max of count and maxCount
            -> Return result(res).
        
        2.Simple Solution:   TC: O(N),   SC:O(1)
            -> Set result and count to be 0.
            -> Iterate through the array.
            -> If count == 0. Set res = n
            -> Increament count by 1 when res = n otherwise decrement by -1
            -> Return result(res).
        
        Leetcode: https://leetcode.com/problems/majority-element/
"""
#Using hashmap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        res, maxCount = 0, 0
        
        for i in nums:
            count[i] = 1 + count.get(i, 0)
            res = i if count[i] > maxCount else res
            maxCount = max(count[i], maxCount)
            
        return res
     
#Simple approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res, count = 0, 0
        
        for n in nums:
            if count == 0:
                res = n
                
            count += (1 if n == res else -1)
            
        return res
