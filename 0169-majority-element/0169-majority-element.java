class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> dict = new HashMap<>();
        
        for(int n: nums){
            if(dict.containsKey(n)){
                dict.put(n, dict.get(n)+1);
                if(dict.get(n)>nums.length/2)
                return n;
            }
            else{
                dict.put(n,1);
            }
            

        }
        return nums[0];
    }
}