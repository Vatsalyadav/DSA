class Solution {
    public int[][] kClosest(int[][] points, int k) {
        TreeMap<Double, ArrayList<Integer>> sortedMap = new TreeMap<>();
        HashMap<Double, Boolean> uniqueDist = new HashMap<>();
        Double dist;
        int i = 0;
        for(int[] point: points){
            dist = (Math.pow(point[0], 2)) + (Math.pow(point[1], 2));
            if(uniqueDist.containsKey(dist)){
                sortedMap.get(dist).add(i);
            }
            else{
                sortedMap.put(dist,new ArrayList<Integer>(Arrays.asList(i)));
                uniqueDist.put(dist, true);
            }
            i++;
        }
        
        int[][] ans = new int[k][2];
        
        i = 0;
        for(Map.Entry<Double, ArrayList<Integer>> entry : sortedMap.entrySet()){
            for(int j = 0; j < entry.getValue().size() && i<k; j++, i++)
                ans[i] = points[entry.getValue().get(j)];
            if(i==k)
                break;
        }
        
        return ans;
    }
}