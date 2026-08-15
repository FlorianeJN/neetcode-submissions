class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray()){
            if(c == '('){
                stack.push(')');
            }
            else if(c == '{'){
                stack.push('}');
            }
            else if (c == '['){
                stack.push(']');
            }

            //If we reach this point, then its a closing character.
            else if (stack.isEmpty() || stack.pop() != c){
                return false;
            }

        }
        return stack.isEmpty();
    }
}
