"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Approach:

1. Brute Force Approach:
    (A) Using 3 nested Loops--     TC: O(N^3)      SC: O(1)
        -> Take max_sum = -9999
        -> First Loop (i) from start index[0] to end index[n], Second Loop (j) from i to n.
        -> Take sum = 0.
        -> Third Loop (k) from i to j.
        -> Now sum = sum + arr[k].
        -> Now, check if sum > max_sum--  if greater assign max_sum = sum
        -> Return max_sum
     
     
    (B) Using 2 nested Loop--      TC: O(N^2)     SC:O(1)
        -> Take max_Sum = -9999
        -> First loop (i) from start index[0] to end index [n],  Second loop (j) from i to n.
        -> Take sum = 0
        -> Now sum = sum + arr[j].
        -> Now, check if sum > max_sum--  if greater assign max_sum = sum
        -> Return max_sum
        
        
2. Kadane's Algorithm(DP)      TC: O(N)      SC: O(1)
        -> First Take max_sum = element of starting index, curr_sum = 0
        -> Traverse through the array and increment curr_sum by adding i
        -> If curr_sum < 1: curr_sum will be 0
        -> Check max(max_sum , curr_sum)
        -> Return max_sum
      
      Leetcode:  https://leetcode.com/problems/maximum-subarray/
"""
#Brute Force I:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = -999
        n = len(nums)
        
        for i in range(0, n):
            for j in range(i, n):
                
                res = 0
                for k in range(i,j+1):
                    res = res + nums[k]
                
                if res > max_sum:
                    max_sum = res
                               
        return max_sum
      
#Brute force II:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = -999
        n = len(nums)
        
        for i in range(0, n):
            
            add = 0
            for j in range(i, n):
                add = add + nums[j]
                
                if add > max_sum:
                    max_sum = add
                
        return max_sum
      
#Kadane's Algorithm:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        curr_sum = 0
        
        for i in nums:
            if curr_sum < 0:
                curr_sum = 0
                
            curr_sum += i
            
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
            





















