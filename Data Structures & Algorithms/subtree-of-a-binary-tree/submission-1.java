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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // Serialization approach
        // O(m+n)

        String r = serialize(root);
        String s = serialize(subRoot);
        return r.contains(s);
    }

    private String serialize(TreeNode root){
        StringBuilder sb = new StringBuilder();
        build(root,sb);
        return sb.toString();
    }

    private void build(TreeNode root, StringBuilder sb){
        if(root == null) {
            sb.append("#,");
            return;
        }
        sb.append("@").append(root.val).append(",");
        build(root.left,sb);
        build(root.right,sb);
    }
}
