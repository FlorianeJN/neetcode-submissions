class Solution {

    public String encode(List<String> strs) {
        // Encoding to the format length#string
        // Ex: "love","you" -> 4#love3#you

        StringBuilder sb = new StringBuilder();

        for(String str : strs){
            sb.append(str.length()+"#"+str);
        }

        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int index = 0;

        while (index < str.length()) {
            int hashIndex = index;
            while (str.charAt(hashIndex) != '#') {
                hashIndex++;
            }
            int length = Integer.parseInt(str.substring(index, hashIndex));
            int start = hashIndex + 1;
            String word = str.substring(start, start + length);
            result.add(word);
            index = start + length;
        }

        return result;
    }
}
