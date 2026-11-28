# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:
        def inorder(root):
            if root is None:
                return []
            return (inorder(root.left)+[root.val]+inorder(root.right))

        arr1 = inorder(root1)
        arr2 = inorder(root2)

        return sorted(arr1 +arr2)
        
