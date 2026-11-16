# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Use BFS to record the nodes for each level
        Time complexity: O(n)
        """
        output = []
        if not root:
            return output

        q = deque([root])
        while q:
            size = len(q)
            cur_level_nodes = []

            # Process the nodes for this level
            for _ in range(size):
                cur_node = q.popleft()
                cur_level_nodes.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

            # Append the nodes for last level
            output.append(cur_level_nodes)
        
        return output


                




        