class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        global answer
        answer=0

        def dfs(root,isLeft):
            global answer   

            if not root :
                return None
            if isLeft:
                answer += root.val
            dfs(root.left,1)
            dfs(root.right,0)   
        dfs(root,0)
        return answer        

      