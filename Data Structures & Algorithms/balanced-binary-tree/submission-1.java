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
    public boolean isBalanced(TreeNode root) {
        // Bottom up DFS
        // Return height of subtree and is subtree balanced
        // O(n)
        return dfs(root)[0] == 1;
    }

    /**
    Returns [isBalanced,height]
    */
    public int[] dfs(TreeNode root) {
        if (root == null)
            return new int[] {1, 0};

        int[] left = dfs(root.left);
        int[] right = dfs(root.right);

        // Its balanced if left and right are balanced and the difference in height is max 1
        boolean balanced = (left[0] == 1 && right[0] == 1) && (Math.abs(left[1] - right[1]) <= 1);

        int height = 1 + Math.max(left[1], right[1]);

        return new int[] {balanced ? 1 : 0, height};
    }
}
