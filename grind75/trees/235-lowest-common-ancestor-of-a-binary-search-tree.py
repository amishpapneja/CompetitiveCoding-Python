
"""
235. Lowest Common Ancestor of a Binary Search Tree
Medium
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 
Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

 
Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

class Solution:
    
    """
    Accepted
    One pass - log(n)
    Check both p and q values -> if both small, go left else go right
    else
    Runtime 94.72%
    Memory 22.57%
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return dfs(root,p,q)

    
    """
    Accepted 
    3pass - log(n)
    Find both p and q and put them into two lists of Nodes ( traversal result)
    find the common
    Runtime 65.67%
    Memory 22.57%
    """
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lis1=[]
        findInBst(lis1, root, p.val)
        lis2=[]
        findInBst(lis2, root, q.val)
        return compare(lis1,lis2)


def dfs(root, p, q):
    if p.val > root.val and q.val > root.val:
        root = root.right
    elif p.val < root.val and q.val < root.val:
        root = root.left
    else:
        return root
    return dfs(root,p,q)

def compare(lis1, lis2):
    set2 = set(lis2)
    common_elemnt = None
    for i in range(len(lis1) - 1, -1, -1):
        item = lis1[i]
        if item in set2:
            common_elemnt = item
            break
    return common_elemnt

def findInBst(lis, root, val):
    while root is not None:
        if root.val == val:
            lis.append(root)
            return
        else:
            if root.val < val:
                lis.append(root)
                root = root.right
            else:
                lis.append(root)
                root = root.left
LeetCode(PROBLEM, Solution).check()
