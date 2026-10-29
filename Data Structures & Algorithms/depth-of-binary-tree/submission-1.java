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
    public int maxDepth(TreeNode root) {
        // BFS -> Count the levels
        // O(n)
        if (root == null) return 0;

        Queue<TreeNode> q = new ArrayDeque<>();
        int max = 0;

        q.offer(root);

        while(!q.isEmpty()){
            int size = q.size();

            for (int i = 0 ; i < size ; i++){
                TreeNode current = q.poll();

                if (current.left != null) q.offer(current.left);
                if (current.right != null) q.offer(current.right);
            }
            max++;
        }
        return max;
    }
}
