# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a=[]

        def dfs(r):
            if r:
                dfs(r.left)
                a.append(r.val)
                dfs(r.right)

        dfs(root)

        head=cur=TreeNode(0)
        for x in a:
            cur.right=TreeNode(x)
            cur = cur.right

        return head.right
