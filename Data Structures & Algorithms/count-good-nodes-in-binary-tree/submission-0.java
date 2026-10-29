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
    public int goodNodes(TreeNode root) {
        // Node is good as long as val >= maxValueSoFar
        // BFS Approach -> propagate max value so far -> O(n)
        // Use pair for node and maxValueSoFar

        if(root == null) return 0;

        Queue<Pair> q = new ArrayDeque<>();
        q.offer(new Pair(root,Integer.MIN_VALUE));
        int goodNodes = 0;

        while(!q.isEmpty()){
            Pair p = q.poll();
            TreeNode node = p.key;
            int currentMaxSoFar = p.value;

            // Compute if good node
            if(node.val >= currentMaxSoFar) goodNodes++;

            // Continue BFS and propagate maxValueSoFar
            if(node.left != null) q.offer(new Pair(node.left,Math.max(node.val,currentMaxSoFar)));
            if(node.right != null) q.offer(new Pair(node.right,Math.max(node.val,currentMaxSoFar)));
        }

        return goodNodes;
    }

    class Pair{
        TreeNode key;
        int value;

        public Pair(TreeNode key, int value){
            this.key = key;
            this.value = value;
        }
    }
}
