
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def mergeTrees(self, t1, t2):
        if t1==None and t2==None:
            return None
        elif t1==None:
            return t2
        elif t2==None:
            return t1
        else:
           current = TreeNode(t1.val+t2.val)
           current.left=self.mergeTrees(t1.left,t2.left)
           current.right=self.mergeTrees(t1.right,t2.right)
           return current

