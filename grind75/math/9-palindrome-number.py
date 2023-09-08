
"""
9. Palindrome Number
Easy
"""
from collections import deque
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given an integer x, return true if x is a palindrome, and false otherwise.
 
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 
Constraints:

-231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    
    # ACcrted
    # modulos solution - no extra space
    def isPalindrome(self, x: int) -> bool:
        val = x
        res = 0
        while val >=1:
            digit = int(val % 10) # get the last digit | Example: 12 % 10 = 2
            res = (res * 10) + digit # multiply the result by 10 and add the digit | example: (1 * 10) + 2 = 12
            val = val /10 # remove the last digit | Example: 12 / 10 = 1
        return x == res
    
    # Accepted
    # modulos solution 
    # This uses stack to back track the digits of x for reverse calculation to generate the reverse of x
    # - O(n) where n is the number of digits in x
    def isPalindrome2(self, x: int) -> bool:
        val = x
        res = 0
        mult = 1
        stk = deque()
        while val >=1:
            stk.append(val % 10)
            val = int(val / 10)
        while stk:
            res += stk.pop() * mult
            mult *= 10
        return x == res
    
    # String reverse solution
    # COmplexity: O(n) where n is the length of the string representation of x
    def isPalindrome3(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

LeetCode(PROBLEM, Solution).check()
