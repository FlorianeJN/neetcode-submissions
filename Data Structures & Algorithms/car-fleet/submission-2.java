class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] pairs = new int[position.length][2]; // position,speed
        Stack<Double> stack = new Stack<>();

        for (int i = 0; i < position.length; i++) {
            pairs[i][0] = position[i];
            pairs[i][1] = speed[i];
        }

        // Sort in decreasing order of position
        Arrays.sort(pairs, (a, b) -> b[0] - a[0]);

        for (int[] p : pairs) {
            double time = (double) (target - p[0]) / p[1];

            if (stack.isEmpty() || time > stack.peek())
                stack.add(time);
        }

        return stack.size();
    }
}
