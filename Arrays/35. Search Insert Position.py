"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it
were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Approach:

1. Simple Approach--  TC: O(N),   SC: O(1)
        -> Travere through the array using for loop.
        -> If target present in the index, Return i.
        -> If not present in the array:
               i. Return i, if target value is smaller then the ith element.
               ii. Return len(nums): if target value is greater then the last index.
               
               
2. Using Binary Search--  TC(log N),  SC: O(1)
         -> Take l(lower) = start index, r(upper) = end index.
         -> calculate mid = (l+r)/2
         -> Now check whether target is equals to mid .If it is equal, Return nums[mid]
         -> If not equal: Check if target > mid (l = mid+1),
                          else target < mid (r = mid-1)
         -> If target val not found in the array. Return l. beacuse l will traverse the array in forward direction and r will go in the reverse direction
         
         Leetcode : https://leetcode.com/problems/search-insert-position/
"""
# Simple approach
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        
        for val in range(n):
            if nums[val] == target:
                return val
            elif target < nums[val]:
                return val
            elif target > nums[-1]:
                return len(nums)
            
                
# Binary Search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        while l <= r:
            mid = (l+r)//2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
                
        return l
                
                
                
        
        
