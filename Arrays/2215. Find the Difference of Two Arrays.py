"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
"""

Solution:

Method1:
def findDifference(nums1, nums2):
        return [(set(nums1) - set(nums2)), (set(nums2) - set(nums1))]

nums1 = list(map(int, input().split())))
nums2 = list(map(int, input().split())))
print(findDifference(nums1, nums2)) 

#TC= O(n), SC= O(1)


#Method2:
nums1 = list(map(int, input().split())))
nums2 = list(map(int, input().split())))

num1 = set(nums1)
num2 = set(nums2)
result = []
        
n1 = num1.difference(num2)
n2 = num2.difference(num1)
        
N1 = list(n1)
N2 = list(n2)
        
result.append(N1)
result.append(N2)
        
return result

#TC= O(n),  SC= O(n)
