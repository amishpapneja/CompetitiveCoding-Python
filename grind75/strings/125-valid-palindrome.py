
"""
125. Valid Palindrome
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
 
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.


"""

class Solution:
    """
    String cleaning + Two pointer [2pass] - O(2n) + O(1)
    Runtime 44.51%
    Memory 90%
    """
    def isPalindrome(self, s: str) -> bool:
        s = prep_string(s).lower()
        if len(s) == 0 or len(s) == 1:
            return True
        i,j = [0, len(s) -1]
        while(i < j):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
def prep_string(s:str) -> str:
        res = ""
        alpha_num = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for ch in s:
            if ch in alpha_num :
                res += ch
        return res
    
extra_cases = [
    TestCase(args=Args(s="aba"),answer=True),
    TestCase(args=Args(s="aazaa"),answer=True),
    TestCase(args=Args(s="aa"),answer=True)
]
LeetCode(PROBLEM, Solution).check(extra_cases)
