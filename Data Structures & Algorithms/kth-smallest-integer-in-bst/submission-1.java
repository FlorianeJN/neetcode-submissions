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
    public int kthSmallest(TreeNode root, int k) {
       // O(n log n) solution -> Use a minHeap
       // Inserting in a heap is log n and we do it n times
       // Go through the tree to fill the minHeap
       // Pop the heap k times
       PriorityQueue<Integer> minHeap = new PriorityQueue<>();
       int res = 0;
       dfs(root,minHeap);

       for(int i = 0 ; i < k ; i++){
        res = minHeap.poll();
       }

       return res;
    }

    private void dfs(TreeNode root, PriorityQueue<Integer> heap){
        if (root == null) return;

        heap.add(root.val);
        dfs(root.left,heap);
        dfs(root.right,heap);
    }
}
