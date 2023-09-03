
"""
104. Maximum Depth of Binary Tree
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

 
Constraints:

The number of nodes in the tree is in the range [0, 104].
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
    DFS O(n) + O(h)
    https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/1770060/c-recursive-dfs-example-dry-run-well-explained/
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return dfs(root)
    
def dfs(root: Optional[TreeNode]):
    if root is None:
        return 0
    return max(dfs(root.left), dfs(root.right)) + 1

LeetCode(PROBLEM, Solution).check()
