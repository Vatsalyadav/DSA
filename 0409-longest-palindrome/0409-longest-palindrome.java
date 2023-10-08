class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> chars = new HashMap<>();
        int longest = 0;
        for(char ch: s.toCharArray()){
            if(chars.containsKey(ch))
                chars.put(ch, chars.get(ch)+1);
            else
                chars.put(ch, 1);
        }
        boolean hasOdd = false;
        for(int count: chars.values()){
            if(count%2 == 1) {
                hasOdd = true;
                longest+= count-1;
            }
            else {
                longest+= count;
            }
        }
        
        return longest + (hasOdd ? 1 : 0); 
    }
}