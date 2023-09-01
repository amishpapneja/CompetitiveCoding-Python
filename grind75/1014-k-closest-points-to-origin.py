
"""
1014. K Closest Points to Origin
Medium
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
 
Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

 
Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104


"""
import math
import heapq
class Solution:
    """
    Accepted
    Keep inserting the negative distances into a heap (will work as a max heap)
    as soon at it gets of height k, remove one element before next insertion
    K height Max heap -  O n(logk) 
    
    https://leetcode.com/problems/k-closest-points-to-origin/solutions/1578232/all-possible-3-python-solutions-interviewer-expectations/
    
    Runtime 76.75%
    Memory 42.67%
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        for point in points:
            if len(h)<k:
                heapq.heappush(h, (-math.dist([0,0],point), point))
            else:
                heapq.heappushpop(h,(-math.dist([0,0],point), point))
        print(h)
        return [h[i][1] for i  in range(k)]
        
    """
    Accepted
    
    O(n log n)
    20ms
    Beats 93.12%
    Memory Beats 20.03%
    """
    def kClosest3(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key = lambda pt: dist([0,0], pt))[0:k]
    
    """
    85/87 passed - tupple dupicates problem 
    case
    [[2,2],[2,2],[3,3],[2,-2],[1,1]]
    """
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        for point in points:
            distance = math.dist([0,0], point)
            dic[tuple(point)] = distance
        sorted_x = sorted(dic.items(), key=lambda kv: kv[1])
        res = [list(k) for k,v in sorted_x]
        return res[0:k]

LeetCode(PROBLEM, Solution).check()
