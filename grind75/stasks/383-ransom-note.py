
"""
383. Ransom Note
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
�
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

�
Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.


"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
        for char in magazine:
            dic[char] += 1
        for char in ransomNote:
            dic[char] -= 1
        for char in dic:
            if dic[char] < 0:
                return False
        return True

LeetCode(PROBLEM, Solution).check()
