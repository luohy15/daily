from typing import List

def find(arr, idx, visited, res):
    if visited[idx] == 2:
        return False
    if visited[idx] == 1:
        return True
    visited[idx] = 2
    for depend in arr[idx]:
        if not find(arr, depend, visited, res):
            return False
    visited[idx] = 1
    res.append(idx)
    return True

class Solution(object):
    """
    课程表2
        dfs拓扑排序
    time: O(n+m)
    space: O(n+m)
    其中n是节点数，m是边数
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        arr = [[] for _ in range(numCourses)]
        for p in prerequisites:
            arr[p[0]].append(p[1])
        visited = [0 for _ in range(numCourses)]
        res = []
        for i in range(numCourses):
            if not find(arr, i, visited, res):
                return []
        return res
