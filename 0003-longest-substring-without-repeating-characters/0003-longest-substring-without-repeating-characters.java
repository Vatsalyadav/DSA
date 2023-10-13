class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> charDict = new HashMap<>();
        int startPoint = 0;
        int maxLen = 0;
        for(int i = 0; i<s.length(); i++){
            if(charDict.containsKey(s.charAt(i)) && charDict.get(s.charAt(i)) >= startPoint){
                maxLen = Math.max(maxLen, i - startPoint);
                startPoint = charDict.get(s.charAt(i)) + 1;
            }
            else{
                maxLen = Math.max(maxLen, i - startPoint + 1);
            }
            charDict.put(s.charAt(i), i);
        }
        
        return maxLen;
    }
}