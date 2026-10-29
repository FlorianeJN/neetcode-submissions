/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        // The graph is undirected so it contains cycles.
        // So we can't simply copy nodes recursively without remembering what we've already copied
        // So let's use a HashMap to keep track of original nodes and their copy.
        // This makes sure that each node is copied EXACTLY ONCE
        // Recursive DFS approach
        
        Map<Node,Node> clones = new HashMap<>();
        return dfs(node,clones);
    }

    private Node dfs(Node node, Map<Node,Node> map){
        if (node == null) return null;

        if (map.containsKey(node)) return map.get(node);

        Node copy = new Node(node.val);
        map.put(node,copy);

        for(Node n : node.neighbors){
            copy.neighbors.add(dfs(n,map));
        }

        return copy;
    }
}