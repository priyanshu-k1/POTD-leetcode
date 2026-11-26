# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(root):
            if not root:
                return [True,0]
            leftBal,leftHeight = dfs(root.left)
            rightBal,rightHeight = dfs(root.right)
            
            is_balanced = leftBal and rightBal and abs(leftHeight - rightHeight) <= 1
                
            return [is_balanced, 1 + max(leftHeight, rightHeight)]
        return dfs(root)[0]
        
        
        return False

        