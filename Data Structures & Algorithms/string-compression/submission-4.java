class Solution {
    public int compress(char[] chars) {
        int start = 0;
        int write = 0;

        while(start < chars.length){
            int end = start + 1;

            while(end < chars.length && chars[end] == chars[start]) end++;

            int length = end - start;
            chars[write++] = chars[start];

            if (length > 1) {
                String str = String.valueOf(length);

                for(int i = 0 ; i < str.length() ; i++){
                    chars[write++] = str.charAt(i);
                }
            }

            start = end;
        }

        return write;
    }
}