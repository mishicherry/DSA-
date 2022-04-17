"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter 
what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Approach:
         -> Take a pointer which will point the index.
         -> Now traverse through the list and check whether the element is equal to val or not.
         -> If not equal to val, then change the index of element with pointer.
         -> Return pointer[index]
         
         TC: O(N),   SC: O(1)
         
         Leetcode: https://leetcode.com/problems/remove-element/       
"""
#Code
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        poi = 0
        
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[poi] = nums[i]
                
                poi += 1
                
        return poi
                
        
