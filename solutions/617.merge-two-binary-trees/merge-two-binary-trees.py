# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        v1 = t1.val if t1 != None else 0
        v2 = t2.val if t2 != None else 0
        t = TreeNode(v1+v2)
        t.left  = self.mergeTrees((t1.left if t1 and t1.left else None), (t2.left if t2 and t2.left else None))
        t.right= self.mergeTrees((t1.right if t1 and t1.right else None), (t2.right if t2 and t2.right else None))
        return t

# so = Solution()
# t1 = TreeNode(1)
# t2 = TreeNode(2)
# so.mergeTrees(t1, t2)