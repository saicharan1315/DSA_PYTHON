class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printLeafNodes(node):
    # Base case: if the node is None, return
    if node is None:
        return

    # If the node is a leaf node, print its value
    if node.left is None and node.right is None:
        print(node.val)
        return

    # Recursively call on the left and right subtrees
    if node.left:
        printLeafNodes(node.left)
    if node.right:
        printLeafNodes(node.right)


# Example usage:
# Constructing a binary tree
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#           /
#          7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(7)

# Print all leaf nodes
printLeafNodes(root)