/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        
        
        int left = 1;
        int right = n;
        int mid;
        int ans = 1;
        while(left<=right){
            mid = left + (right - left)/2;
            if(isBadVersion(mid)){
                right = mid - 1;
                ans = mid;
            }
            else {
                left = mid + 1;
            }
        }
        return ans;
    }
}