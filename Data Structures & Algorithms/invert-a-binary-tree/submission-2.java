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
    public TreeNode invertTree(TreeNode root) {
        // BFS -> O(n)
        // Invert the subtrees
        if (root == null) return null;

       Queue<TreeNode> q = new ArrayDeque<>();
       q.offer(root); 

       while(!q.isEmpty()){
        int size = q.size();

        for(int i = 0 ; i < size ; i++){
            TreeNode current = q.poll();

            TreeNode temp = current.left;
            current.left = current.right;
            current.right = temp;

            if (current.left != null) q.offer(current.left);
            if (current.right != null) q.offer(current.right);
        }
       }

       return root;
    }
}
