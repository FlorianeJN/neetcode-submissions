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
        //                2 [-inf,inf]
        //               / \
        //    [-inf,2]  1   3 [2,inf] 
        // When we move to the right -> update lower 
        // When we move to the left -> update higher
        // Recursive DFS -> O(n)
        return isValid(root,null,null); // node, high, low
    }

    private boolean isValid(TreeNode root, Integer low, Integer high) {
        if (root == null) return true;

        // Check root.val against low and high
        if(low != null && root.val <= low) return false;
        if(high != null && root.val >= high) return false;

        // Recursively call for each subtree and update low and high
        return isValid(root.left,low,root.val) && isValid(root.right,root.val,high);

    }

}
