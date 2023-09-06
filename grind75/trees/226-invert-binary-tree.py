
"""
226. Invert Binary Tree
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given the root of a binary tree, invert the tree, and return its root.
 
Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:


Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


"""

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    """
    Accepted
    
    Runtime 94.72%
    Memory  5.05%
    
    Time complexity: O(n)
    Space complexity: O(n)
    Approach: DFS
    swap left and right nodes as you traverse down the tree. call dfs on left and right nodes and swap them
    
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self._dfs(root)

    def _dfs(self, root: TreeNode):
        if root is None:
            return
        temp = self._dfs(root.right)
        root.right = self._dfs(root.left)
        root.left = temp
        return root
LeetCode(PROBLEM, Solution).check()
