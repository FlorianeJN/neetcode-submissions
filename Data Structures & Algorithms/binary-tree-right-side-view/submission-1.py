# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Use BFS to record the first right side node for each level
        Time complexity: O(n)
        """
        output = []
        if not root:
            return output

        q = deque([root])

        while q:
            size = len(q)
            is_first_node = True

            for _ in range(size):
                cur = q.popleft()
                if is_first_node:
                    output.append(cur.val)
                    is_first_node = False
                
                # adding right values first so that its the first values that we see
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        
        return output
                
        