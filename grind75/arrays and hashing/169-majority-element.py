
"""
169. Majority Element
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
 
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

 
Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

class Solution:
    """
    Moore Voting Algorithm O(n) + O(1)
    sol: https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly/
    153ms
    Runtime 69.78% 
    Memory 67.31% 
    """
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
    
    """
    Accepted - Hashing O(n) + O(n)
    156ms
    Runtime 61.84%
    Memory 67.31%
    """
    def majorityElement2(self, nums: List[int]) -> int:
        dic = {}
        freq = len(nums)/2
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1
        for key in dic:
            if dic[key] > freq:
                return key
        return 0


extra_cases = [
    TestCase(args=Args(nums=[0, 0, 0, 1, 2]), answer=0)
]
LeetCode(PROBLEM, Solution).check(extra_cases)
