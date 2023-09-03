
"""
543. Diameter of Binary Tree
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
 
Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

 
Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Runtime 97.34%
    Memory 93.64%
    
    O(n)
    Modified DFS - Every point, check the addition of both child nodes' height, see if it is maximum
    return maximum diameter in the end
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.height(root)
        return self.diameter

    def height(self, root):
        if root is None:
            return 0
        l, r = self.height(root.left), self.height(root.right)
        self.diameter = max(self.diameter, l + r)
        return max(l, r) + 1
    
    """
    Not Accepted - 100/104
    Reason, we were calculating the heights of both subchilds from root
    and assuming longest path will always go via the root. Instead check it at every node while performing dfs
    
    Case
    [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
    
    """
    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        leftH = height(root.left)
        rightH = height(root.right)
        return height(root.left) + height(root.right)

def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1

LeetCode(PROBLEM, Solution).check()
