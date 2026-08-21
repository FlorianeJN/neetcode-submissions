class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        // Monotonic stack approach (+ sorting)
        // Time Complexity: O(n log n)

        int[][] pairs = new int[position.length][2];
        Stack<Double> stack = new Stack<>();

        for(int i = 0 ; i < position.length ; i++){
            pairs[i][0] = position[i];
            pairs[i][1] = speed[i];
        }

        Arrays.sort(pairs, (a, b) -> b[0] - a[0]);

        for(int[] pair : pairs){
            double time = (double) (target - pair[0]) / pair[1];
            if(stack.isEmpty() || time > stack.peek()) stack.push(time);
        }

        return stack.size();
    }
}
