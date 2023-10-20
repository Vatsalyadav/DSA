class Solution {
    public void sortColors(int[] nums) {
        HashMap<Integer, Integer> colors = new HashMap<>();
        
        colors.put(0,0);
        colors.put(1,0);
        colors.put(2,0);
        
        for(int n:nums){
            colors.put(n, colors.get(n)+1);
        }
        int i = 0;
        int l = 0;
        while(i<3){
            for(int j = 0; j<colors.get(i); j++)
                nums[l++] = i;
            i++;
        }
    }
}