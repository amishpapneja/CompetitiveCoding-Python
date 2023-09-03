
"""
75. Sort Colors
Medium
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
 
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

 
Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

 
Follow up: Could you come up with a one-pass algorithm using only constant extra space?

"""

class Solution:
    """
    Runtime 88.87%
    Memory 69.10%
    Dutch Algo - 1 pass 
    https://leetcode.com/problems/sort-colors/solutions/3464652/beats-100-c-java-python-javascript-two-pointer-dutch-national-flag-algorithm/
    """
    def sortColors(self, nums: List[int]) -> None:
        l,m, r = 0, 0, len(nums)-1
        while m <= r:
            if  nums[m] == 0:
                temp = nums[l]
                nums[l] = 0
                nums[m] = temp
                l += 1
                m += 1
            elif nums[m] == 2:
                temp = nums[r]
                nums[r] = 2
                nums[m] = temp
                r -= 1
            else:
                m += 1
        return nums
    """
    Accepted
    O(n) O (n) 2 pass solution
    one pass for counting occurences, one pass to create the list and assignning in place using [:]
    """
    def sortColors2(self, nums: List[int]) -> None:
        ct0 = nums.count(0)
        ct1 = nums.count(1)
        ct2 = nums.count(2)
        nums[:] = [0] * ct0 + [1] * ct1 + [2] * ct2
        """
        Do not return anything, modify nums in-place instead.
        """
        pass

LeetCode(PROBLEM, Solution).check()
