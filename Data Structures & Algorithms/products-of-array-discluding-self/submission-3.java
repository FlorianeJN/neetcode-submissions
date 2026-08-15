class Solution {
    public int[] productExceptSelf(int[] nums) {
        int countZero = 0;
        int maxProduct = 1;
        int[] output = new int[nums.length];

        //Obtenir le produit maximal et le nombre de '0'
        for(int n : nums){
            if(n == 0){
                countZero++;
            }
            else{
                maxProduct *= n;
            }
        }

        //Cas 1 - Aucun zero
        if(countZero == 0){
            for(int i = 0 ; i < nums.length; i++){
                output[i] = maxProduct / nums[i];
            }
            return output;
        }

        //Cas 2 - Exactement 1 zero
        else if(countZero == 1){
            for(int i = 0 ; i < nums.length ; i++){
                if(nums[i] == 0){
                    output[i] = maxProduct; //Les autres cases sont automatiquement initialisee a '0'
                }
            }
            return output;
        }

        //Cas 3 - plus qu'un zero
        else{
            return output; //Toutes les cases sont initialisees a '0'
        }

    }
}  
