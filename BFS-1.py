# BFS-1
# Problem 1 Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        self.result = []
        self.dfs(root, 0 )
        return self.result

    def dfs(self, root: Optional[TreeNode], lvl : int ) -> None:
        #base
        if root == None:
            return

        #logic
        if lvl == len(self.result):
            temp = [] 
            temp.append(root.val)
            self.result.append(temp)
        else:
            self.result[lvl].append(root.val)

        self.dfs(root.left, lvl + 1)
        self.dfs(root.right , lvl + 1)
# TC = O(n), SC O(h)

# Problem 2 Course Schedule (https://leetcode.com/problems/course-schedule/)
from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True

        q = Queue()
        indegrees = [0 for i in range(numCourses)]
        Map = dict()
        count = 0
        for preq in prerequisites:
            From = preq[1] 
            To = preq[0]
            indegrees[To] = indegrees[To] + 1
            if From not in Map:
                Map[From] = []
            Map[From].append(To)

        for i in range(numCourses):
            if indegrees[i] ==0:
                count = count +1
                q.put(i)

        if count == 0:
            return False

        while q.qsize()>0:
            curr = q.get()
            if curr in Map:
                edges = Map[curr]
                for edge in edges:
                    indegrees[edge] = indegrees[edge] - 1
                    if indegrees[edge] == 0:
                        q.put(edge)
                        count = count + 1

        return count == numCourses

        