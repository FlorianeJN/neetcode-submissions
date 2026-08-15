class Solution {
    public boolean hasDuplicate(int[] nums) {
        //Le tableau est de taille 0 ou 1, impossible d'avoir un duplicate
        if(nums.length < 2){
            return false;
        }

        boolean duplicate = false;

        for(int i = 0 ; i < nums.length && !duplicate; i++){
            for(int j = i+1 ; j < nums.length && !duplicate; j++){
                if(nums[i] == nums[j])
                duplicate = true;
            }
        }

        return duplicate;

    }
}
