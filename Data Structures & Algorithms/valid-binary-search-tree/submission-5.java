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
    public boolean isValidBST(TreeNode root) {
        // BFS Approach
        // Pass low and high so that node can compare

        if (root == null) return true;

        Queue<Pair> q = new ArrayDeque<>();
        q.offer(new Pair(root,new Integer[]{null,null})); // [0] -> low , [1] -> high

        while(!q.isEmpty()){
            Pair p = q.poll();
            TreeNode current = p.node;
            Integer low = p.values[0];
            Integer high = p.values[1];

            // Check current against high and low
            if (low != null && current.val <= low) return false;
            if (high != null && current.val >= high) return false;

            // Add subtrees + update high and low
            if (current.left != null)
                q.offer(new Pair(current.left,new Integer[]{low,current.val}));
            
            if (current.right != null)
                q.offer(new Pair(current.right,new Integer[]{current.val,high}));

        }

        return true;
    }

    class Pair {
        TreeNode node;
        Integer[] values;

        public Pair(TreeNode node, Integer[] values){
            this.node = node;
            this.values = values;
        }
    }
}
