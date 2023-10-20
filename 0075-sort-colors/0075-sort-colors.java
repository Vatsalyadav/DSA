class Solution {
    public void sortColors(int[] nums) {

        int[] colors = new int[3];
        for(int n: nums){
            colors[n]++;
        }
        
        Arrays.fill(nums, 0, colors[0], 0); // Fill the first n elements with m
        Arrays.fill(nums, colors[0], colors[0] + colors[1], 1);
        Arrays.fill(nums, colors[0] + colors[1],colors[0] + colors[1]+ colors[2], 2);
    }
}