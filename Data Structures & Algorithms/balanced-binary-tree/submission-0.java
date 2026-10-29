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
        // Brute force approach -> Compute height of left and right subtrees for each node
        // Top-down ordering
        // O(n2)

        // Base case
        if (root == null) return true;

        int left = height(root.left);
        int right = height(root.right);

        if(Math.abs(left - right) > 1) return false;

        return isBalanced(root.left) && isBalanced(root.right);
    }

    public int height(TreeNode node){
        if (node == null) return 0;
        return 1 + Math.max(height(node.left),height(node.right));
    }
}
