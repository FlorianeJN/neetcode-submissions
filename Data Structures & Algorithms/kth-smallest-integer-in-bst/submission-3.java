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
    private int count = 0;
    private int result = 0;

    public int kthSmallest(TreeNode root, int k) {
        // Inorder traversal (left,node,right) on binary tree gives sorted order
        // O(h + k) -> Optimal version
        // Stop as soon as we have the result
        dfs(root,k);
        return result;
    }

    private void dfs(TreeNode root, int k){
        if (root == null || count >= k) return;

        dfs(root.left,k); // Go as far left as possible

        if (count >= k) return;

        count++;
        if(count == k) {
            result = root.val;
            return;
        }

        dfs(root.right,k);
    }
}
