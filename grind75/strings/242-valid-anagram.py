
"""
242. Valid Anagram
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""

class Solution:
    
    """
    Accepted
    Runtime 72.70%
    Memory 60.58%
    O(n) 3 pass : iterate one string to increment char values, other string decrements
    check for non zero offsets -> false oterhwise true
    """
    def isAnagram(self, s: str, t: str) -> bool:
        lis = [0]*26
        for ch in s:
            lis[ord(ch)-97] += 1
        for ch in t:
            lis[ord(ch)-97] -= 1
        for i in lis:
            if i is not 0:
                return False
        return True

LeetCode(PROBLEM, Solution).check()
