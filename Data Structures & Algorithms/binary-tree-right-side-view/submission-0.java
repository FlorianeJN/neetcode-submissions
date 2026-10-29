/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        // BFS from right to left, add to list first one of each level
        // O(n)
        List<Integer> result = new ArrayList<>();

        if (root == null)
            return result;

        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);

        while (!q.isEmpty()) {
            int size = q.size();
            boolean firstIteration = true;

            for (int i = 0; i < size; i++) {
                TreeNode current = q.poll();

                if (firstIteration) {
                    result.add(current.val);
                    firstIteration = false;
                }

                if (current.right != null)
                    q.add(current.right);
                if (current.left != null)
                    q.add(current.left);
            }
        }
        return result;
    }
}
