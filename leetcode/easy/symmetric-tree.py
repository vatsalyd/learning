# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        left =[]
        right= []

        def leftinorder(node):
            if node is None:
                left.append(None)
                return
            left.append(node.val)    
            leftinorder(node.left)
            
            leftinorder(node.right)
        def rightinorder(node):
            if node is None:
                right.append(None)
                return
            right.append(node.val)    
            rightinorder(node.right)
            
            rightinorder(node.left)
        leftinorder(root.left)
        rightinorder(root.right)
        return left == right
            
            
