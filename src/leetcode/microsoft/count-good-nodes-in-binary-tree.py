# Source: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity: O(N) where N is number of nodes in the tree
# Space complexity: O(H) where H is height of binary tree
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def traverse_tree(root, largest_value: int):
            if root is None:
                return 0

            val = root.val

            if largest_value <= val:
                is_good_node = True  # there is no node with value greater than X
            else:
                is_good_node = False  # there is a node with value greater than X

            largest_value = max(largest_value, val)

            return is_good_node + traverse_tree(root.left,
                                                largest_value) + traverse_tree(
                root.right, largest_value)

        number_of_good_nodes = traverse_tree(root, root.val)
        return number_of_good_nodes
