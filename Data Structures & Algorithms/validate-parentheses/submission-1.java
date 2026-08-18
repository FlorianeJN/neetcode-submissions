class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        char[] array = s.toCharArray();

        for (char c : array) {
            if (c == '{' || c == '(' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false; 

                if (c == '}') {
                    if (stack.peek() == '{') stack.pop();
                    else return false;
                } else if (c == ')') {
                    if (stack.peek() == '(') stack.pop();
                    else return false;
                } else {
                    if (stack.peek() == '[') stack.pop();
                    else return false;
                }
            }
        }

        return stack.isEmpty();
    }
}