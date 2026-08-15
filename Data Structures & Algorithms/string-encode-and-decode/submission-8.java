class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str : strs){
            sb.append(str.length()).append('#').append(str);
        }
        return new String(sb);
    }

    public List<String> decode(String str) {
       List<String> result = new ArrayList<>();
       int i = 0 ;

       while( i < str.length()){
        int sharpIndex = str.indexOf('#',i);
        int length = Integer.parseInt(str.substring(i,sharpIndex));
        i = sharpIndex + 1; //Move past the '#'
        result.add(str.substring(i , i + length));
        i += length;
       }

       return result;
    }
}
