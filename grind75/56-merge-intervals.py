
"""
56. Merge Intervals
Medium
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
 
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

 
Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104


"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       # n log n + o(n)
        intervals.sort(key = lambda l:l[0])
        res = []
        print(intervals)
        size = len(intervals)
        i = 1
        curInt = intervals[0]
        while i < size:
            nexInt = intervals[i]
            lower, upper = nexInt[0], nexInt[1]
            if curInt[1] >= lower:
                curInt = [
                    min(curInt[0], lower),
                    max(curInt[1], upper)
                ]
            else:
                res.append(curInt)
                curInt = nexInt
            i += 1
        res.append(curInt)
        return res  

extra_cases = [
    TestCase(args=Args(intervals=[
        [1,1], [1,1], [1,5]
    ]), answer= [[1,5]]),
    TestCase(args=Args(intervals=[
        [1,1], [1,1], [1,5], [5,10]
    ]), answer= [[1,10]]),
    TestCase(args=Args(intervals=[
        [1,4],[0,4]
    ]), answer= [[0,4]]),
    TestCase(args=Args(intervals=[
        [1,4],[2,3]
    ]), answer= [[1,4]])
    
]
LeetCode(PROBLEM, Solution).check(extra_cases)
