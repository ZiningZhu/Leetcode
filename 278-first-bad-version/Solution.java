/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {

        /*A canonical version of binary search*/
        int start = 1;
        int end = n;
        int mid;
        while (end - start >= 2) {
            mid = start + (end - start) / 2;
            if (isBadVersion(mid)) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (isBadVersion(start))
            return start;
        else
            return end;
    }
}
