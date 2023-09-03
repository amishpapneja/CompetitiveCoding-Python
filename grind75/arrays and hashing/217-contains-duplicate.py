
"""
217. Contains Duplicate
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 
Example 1:
Input: nums = [1,2,3,1]
Output: true
Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


"""

class Solution:
    
    # one liner
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)
    
    """
    Check second occurence using Set - O(n) + O(n)
    Runtime 99.04%
    Memory 63.05%
    """
    def containsDuplicate2(self, nums: List[int]) -> bool:
        dic = set()
        for num in nums:
            if num in dic:
                return True
            else:
                dic.add(num)
        return False

LeetCode(PROBLEM, Solution).check()
