class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> stack = new Stack<>(); // Stores [temp,index]
        int[] result = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            int t = temperatures[i];

            while (!stack.isEmpty() && t > stack.peek()[0]) {
                // remove from the stack and treat
                int[] val = stack.pop();
                result[val[1]] = i - val[1];
            }

            stack.push(new int[] {t, i});
        }

        return result;
    }
}
