class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> magDict = new HashMap<>();
        for(char ch: magazine.toCharArray()){
            if(magDict.containsKey(ch))
                magDict.put(ch, magDict.get(ch)+1);
            else
                magDict.put(ch, 1);
        }
        for(char ch: ransomNote.toCharArray()){
            if(magDict.containsKey(ch) && magDict.get(ch)>0)
                magDict.put(ch, magDict.get(ch)-1);
            else
                return false;
        }
        return true;
    }
}