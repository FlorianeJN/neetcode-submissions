class Solution {
    public int evalRPN(String[] tokens) {
        
        // Time complexity: O(n)
        // Space Complexity: O(n)

        Deque<Integer> stack = new ArrayDeque<>();

        for (String token : tokens) {
            if (!isAnOperator(token)) {
                stack.push(Integer.parseInt(token));
            } else {
                int b = stack.pop(); // most recently pushed
                int a = stack.pop(); // pushed before that
                int result = switch (token) {
                    case "+" -> a + b;
                    case "-" -> a - b;
                    case "*" -> a * b;
                    case "/" -> a / b;
                    default -> throw new IllegalArgumentException();
                };
                stack.push(result);
            }
        }

        return stack.pop();
    }

    public static boolean isAnOperator(String s) {
        return s.equals("-") || s.equals("+") || s.equals("*") || s.equals("/");
    }
}