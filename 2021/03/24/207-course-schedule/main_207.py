from typing import List

def hasCycle(arr, idx, visited):
    if visited[idx] == 2:
        return True
    if visited[idx] == 1:
        return False
    visited[idx] = 2
    for dependid in arr[idx]:
        if hasCycle(arr, dependid, visited):
            return True
    visited[idx] = 1
    return False

class Solution(object):
    """
    课程表
        DAG判断环（dfs）
    time: O(n+m)
    space: O(n+m)
    其中n是节点数，m是边数
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        arr = [[] for _ in range(numCourses)]
        for p in prerequisites:
            arr[p[0]].append(p[1])
        visited = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if hasCycle(arr, i, visited):
                return False
        return True