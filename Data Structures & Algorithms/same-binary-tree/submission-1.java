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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // BFS
        // For each level, compare left and right
        if (p == null && q == null)
            return true;
        if (p == null || q == null)
            return false;

        Queue<TreeNode> queueP = new ArrayDeque<>();
        Queue<TreeNode> queueQ = new ArrayDeque<>();
        queueP.add(p);
        queueQ.add(q);

        while (!queueP.isEmpty()) {
            TreeNode a = queueP.poll();
            TreeNode b = queueQ.poll();

            if (a.val != b.val)
                return false;

            if ((a.left == null) != (b.left == null))
                return false;
            if ((a.right == null) != (b.right == null))
                return false;

            if (a.left != null) {
                queueP.add(a.left);
                queueQ.add(b.left);
            }

            if (a.right != null) {
                queueP.add(a.right);
                queueQ.add(b.right);
            }
        }

        return true;
    }
}
