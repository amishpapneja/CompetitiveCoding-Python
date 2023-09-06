
"""
409. Longest Palindrome
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
 
Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

 
Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.


"""

class Solution:
    
    """
    Clean Solution - Single pass O(n)
    https://leetcode.com/problems/longest-palindrome/solutions/3156147/c-easiest-beginner-friendly-sol-o-n-time-and-o-128-o-1-space/
    """
    def longestPalindrome(self, s: str) -> int:
        odd_count = 0
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
            if d[ch] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
        if odd_count > 1:
            return len(s) - odd_count + 1
        return len(s)
    
    """
    Accepted
    O(n) time + O(128) = O(1)space
    
    hashing all the frequencies,
    add all the even ones
    if odd values are found -> add all the values - (subtract lenOfOdd-1) because we can only use one odd frequency,
    so we strip one from each of the odd letters found, and keep just one
    Caveat -> This solution is a 3pass O(n) coz we use list comprehension two times to calculate even and odd counts
    
    Runtime:  61.55%
    Memory:  7.13%
    """
    def longestPalindrome2(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        dic = {}
        for c in s:
            if c in dic:
                dic[c] = dic[c] + 1
            else:
                dic[c] = 1
        
        evenSum = sum([x  for x in dic.values() if x%2==0])
        oddList = [x  for x in dic.values() if x%2 is not 0]
        res = evenSum
        if len(oddList) > 0:
            res += sum(oddList) - (len(oddList) - 1) 
        return res
extra_cases = [
    TestCase(Args(s="aaaa"), answer=4),
    TestCase(Args(s="aaaaa"), answer=5),
    TestCase(Args(s="AB"), answer=1)
]

LeetCode(PROBLEM, Solution).check(extra_cases)
