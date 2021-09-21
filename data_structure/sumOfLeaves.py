class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeaves(node):
    global answer
    answer= 0

    def dfs(root,isLeft):
        global answer

        if not root :
            return None
        if not root.left and not root.right and isLeft:
            answer += root .val
        dfs(root.left,1)
        dfs(root.right,0)
    dfs(node,0)
    return answer


if __name__ == "__main__":

    tree1 = TreeNode(3)

    tree1.left = TreeNode(9)
    tree1.right = TreeNode(20)

    tree1.left.left = TreeNode(5)

    tree1.right.left = TreeNode(15)
    tree1.right.right = TreeNode(7)

    print(f"sumOfLeaves: {sumOfLeaves(tree1)}")