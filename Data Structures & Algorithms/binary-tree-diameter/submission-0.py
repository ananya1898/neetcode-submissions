# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global maxDiameter
        maxDiameter=0
        self.findHeight(root)
        return maxDiameter
  
    def findHeight(self,root):
        global maxDiameter

        if not root:
            return 0
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)
        
        maxDiameter = max(maxDiameter,left+right)

        return 1 + max(left,right)


        