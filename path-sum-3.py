# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dp = {}

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # return the number of paths where the sum of values equals targetSum
        # either the root lies on such a path or not 
        # if it lies of such a path then calculate all such paths 
        # it it not lies on such a path then calculate values for left and right and sum them 
        if not root:
            return 0
        paths_root = self.helper(root,targetSum)
        paths_right = self.pathSum(root.right,targetSum)
        paths_left = self.pathSum(root.left,targetSum)

        return paths_right + paths_left + paths_root

    def isLeaf(self, node):
        if node.left==None and node.right==None: 
            return True
        return False
    def helper(self, root, targetSum):
        # how many paths starting at root give me targetSum
        # if tuple([root,targetSum]) in self.dp.keys():
        #     return self.dp[tuple([root,targetSum])]
        if not root:
            return 0
        if self.isLeaf(root):
            if targetSum-root.val != 0:
                return 0
            return 1
        temp = 0
        if targetSum-root.val==0:
            temp = 1
        return temp + self.helper(root.left, targetSum-root.val) + self.helper(root.right, targetSum-root.val) 
        