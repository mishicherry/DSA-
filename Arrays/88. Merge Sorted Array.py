"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 
respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Approach:
         1. Using For Loop:    TC: O(N)   SC: 0(1)
           -> First traverse second array from 0 to N.
           -> Assign nums1[i+m] ie i[index of nums2] + len of nums1 = nums2[i].
           -> sort nums1
           
         2. Using while loop:   TC: O(N)   SC: 0(1)
           -> Take last index(end) = m+n-1
           -> First while loop will run when m, n > 0
             -- If nums1[m] > nums2[n], then assign end to nums1[m]
             -- Otherwise assign end = nums2[n]
           -> Second while loop will run when n>0 and assign end = nums2[n]
           
        Leetcode:  https://leetcode.com/problems/merge-sorted-array/submissions/
"""
#1.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i + m] = nums2[i]
        
        nums1.sort()
        
#2
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        end = m + n - 1
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[end] = nums1[m-1]
                m-=1
                
            else:
                nums1[end] = nums2[n-1]
                n-=1
                
            end-=1
            
        while n > 0:
            nums1[end] = nums2[n-1]
            n, end = n-1, end-1
        
    
