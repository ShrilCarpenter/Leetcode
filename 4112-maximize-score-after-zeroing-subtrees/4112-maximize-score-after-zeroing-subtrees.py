import math
import sys

# Increase recursion depth for deep trees (e.g., N up to 10^5)
sys.setrecursionlimit(10**6)


class Solution:

  def maxScore(
      self, parent: list[int], op: list[int], score: list[int]
  ) -> int:
    n = len(parent)
    child = [[] for _ in range(n)]

    # Build the adjacency list representing the tree
    for i in range(1, n):
      child[parent[i]].append(i)

    def dfs(i: int) -> int:
      # Base case: leaf node
      if not child[i]:
        return score[i]

      total = 0
      mn = math.inf

      # Gather results from all child subtrees
      for j in child[i]:
        val = dfs(j)
        total += val
        if val < mn:
          mn = val

      # Apply node operation rules
      if op[i] == 1:
        total -= mn
      elif mn < 0:
        total -= mn

      return score[i] + total

    return dfs(0)
