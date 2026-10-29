class LRUCache {
    int capacity;
    Map<Integer,Node> map;
    Node head;
    Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<>();
        head = new Node(0,0);
        tail = new Node(0,0);

        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        Node node = map.get(key);
        if (node == null) return -1;

        unlink(node);
        addToFront(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        Node node = map.get(key);

        if (node != null){
            node.value = value;
            unlink(node);
            addToFront(node);
            return;
        }

        if (map.size() == capacity) {
            Node lru = tail.prev;
            unlink(lru);
            map.remove(lru.key);
        }

        Node newNode = new Node(key,value);
        map.put(key,newNode);
        addToFront(newNode);
    }

    private void unlink(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void addToFront(Node node){
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }

    class Node{
        int key, value;
        Node prev, next;

        Node(int key, int value){
            this.key = key;
            this.value = value;
        }
    }
}
