"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


Approach:  
      -> Take two pointers ie- left, right. Where left(defines the place to be replaced), right(will traverse through the array)
      -> Now, when ar[right] != ar[right-1].. ie- next element is not eqaul to the previous element then assign ar[left] = ar[right]
      -> Then left will only increase when the next value is not equal to the previous value.
      
      TC: O(N),   SC:O(1)
      
      Leetcode:  https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        
        for right in range(1, n):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left +=1
                
        return left
