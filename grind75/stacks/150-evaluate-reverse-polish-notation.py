
"""
150. Evaluate Reverse Polish Notation
Medium
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

 
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

 
Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


"""
from collections import deque
import operator

class Solution:
    """
    Clean solution using operation map
    Runtime  84.83%
    Memory Beats 81.57%
    """
    
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
                '+' : lambda x, y : x + y,
                '-' : lambda x, y : x - y,
                '*' : lambda x, y : x * y,
                '/' : lambda x, y : int(x / y)
                }

        stack = []
        for i in tokens:
            if i in "+-*/":
                b = stack.pop()
                a = stack.pop()
                stack.append(op[i](a, b))
            else:
                stack.append(int(i))
                
        return stack.pop()
    
    """
    
    
    """
    
    def evalRPN2(self, tokens: List[str]) -> int:
        stk = deque()
        for token in tokens:
            if token in "+-*/":
                # print(token)
                #operation
                # print(stk)
                j, i = int(stk.pop()), int(stk.pop())
                res = None
                if token is "+":
                    res = i + j
                elif token is "-":
                    res = i - j
                elif token is "*":
                    res = i * j
                elif token is "/":
                    res = i / j
                stk.append(res)
            else:
                stk.append(token)
        # print(stk)
        return stk.pop()    

extra_case = [
    TestCase(args=Args(
        tokens= [
            "5"
        ]),answer= "5")
]
LeetCode(PROBLEM, Solution).check(extra_case)
