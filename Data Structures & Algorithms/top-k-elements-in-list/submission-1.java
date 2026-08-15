class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> mapCount = new HashMap<>();
        int size = nums.length + 1;

        //Un array contenant des listes. l'indice de l'array correspond au compte.
        List<Integer>[] listeArray = new List[size];
        for(int i = 0 ; i < size ; i++){
            listeArray[i] = new ArrayList<>();
        }

        //On remplit la map pour le compte
        for(int n : nums){
            mapCount.put(n,mapCount.getOrDefault(n,0)+1);
        }

        //On remplit l'array du compte.
        for(Map.Entry<Integer,Integer> entry : mapCount.entrySet()){
            listeArray[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int indexRes = 0;

        //On parcourt l'array du compte k fois et on obtient alors les k plus frequentes valeurs.
        for(int j = size - 1 ; j > 0 && k > 0 ; j--){
            if(!listeArray[j].isEmpty()){
                for(int n : listeArray[j]){
                    res[indexRes] = n;
                    k--;
                    indexRes++;
                }
            }
        }
        return res;
    }
}
