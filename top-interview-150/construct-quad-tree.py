
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# dp = {}

def checkAllEqual(row , col , n, grid):
    vals = set()
    # if tuple([row,col,n]) in dp.keys():
    #     return dp[(row,col,n)]
    
    for i in range(row,row+n):
        for j in range(col,col+n):
            vals.add(grid[i][j])
            if len(vals) == 2:
                break
    if len(vals)==2:
        # dp[tuple([row,col,n])]=-1
        return -1
    val = vals.pop()
    # dp[tuple([row,col,n])]=val
    return val


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.helper(0,0,n,grid)

    def helper(self, i, j, n, grid):
        # recursion
        # return the root of this particular subgrid
        res = checkAllEqual(i , j , n, grid)

        if res==-1:
            # break into four parts
            topleft = self.helper(i , j , n//2 , grid)
            topright = self.helper(i, j + (n//2) , n//2 , grid)
            bottomleft = self.helper(i + (n//2), j, n//2, grid)
            bottomright = self.helper(i + (n//2), j+(n//2) , n//2 , grid)
            root = Node(0,False,topleft,topright,bottomleft,bottomright)
            return root

        root = Node(res,True,None, None, None, None)
        return root

           