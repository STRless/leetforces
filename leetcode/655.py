# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Topic: Tree, DFS
# Time Complexity: O(n) where n is number of nodes in tree
# Space Complexity: O(nm) where n is number of columns and m is height
class Solution:
    def findTreeHeight(self, root):
        maxHeight = 0
        if root.left:
            maxHeight = max(maxHeight, self.findTreeHeight(root.left)+1)
        if root.right:
            maxHeight = max(maxHeight, self.findTreeHeight(root.right)+1)
        return maxHeight
    
    def positionInMatrix(self, matrix, height, root, x, y):
        matrix[x][y] = str(root.val)
        if root.left:
            self.positionInMatrix(matrix, height, root.left, x+1, y-(2**(height-x-1)))
        if root.right:
            self.positionInMatrix(matrix, height, root.right, x+1, y+(2**(height-x-1)))

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        treeHeight = self.findTreeHeight(root)

        m = treeHeight + 1
        n = 2**(treeHeight+1) - 1
        ans = [["" for _ in range(n)] for _ in range(m)]
        self.positionInMatrix(ans, treeHeight, root, 0, (n-1)//2)
        return ans