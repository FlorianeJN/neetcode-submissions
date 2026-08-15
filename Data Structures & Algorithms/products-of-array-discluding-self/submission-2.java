class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        
        int maxProduct = 1;
        int zeroCount = 0;

        // Calculate the product of all non-zero numbers and count zeros
        for (int num : nums) {
            if (num == 0) {
                zeroCount++;
            } else {
                maxProduct *= num;
            }
        }

        //S'il y a plus qu'un zero, tous les elements du output sont '0'
        if (zeroCount > 1) {
            return output; 
        }

        //S'il y a exactement un zero, seulement la position du zero aura maxProduct, les autres ont '0'
        if (zeroCount == 1) {
            for (int i = 0; i < nums.length; i++) {
                if(nums[i] == 0){
                    output[i] = maxProduct;
                }
                else{
                    output[i] = 0;
                }
               // output[i] = (nums[i] == 0) ? maxProduct : 0;
            }
        } 
        //S'il n'y a aucun zero, on calcule le produit en divisant le produit max par l'element.
        else {
            for (int i = 0; i < nums.length; i++) {
                output[i] = maxProduct / nums[i];
            }
        }

        return output;
    }
}
