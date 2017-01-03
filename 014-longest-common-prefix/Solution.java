public class Solution {
    import java.util.*;
    public class Solution {
        /*
        // Alg 1: Brute force: check each of the strings. Time limit exceeded at input of lots of quite long strings.
        public String longestCommonPrefix(String[] strs) {
            if (strs.length == 0) {
                return "";
            }
            String lcp = strs[0];
            for (int i = 1; i < strs.length; i++) {
                if (strs[i].length() < lcp.length()) {
                    lcp = lcp.substring(0, strs[i].length());
                }
                if (lcp.length() == 0)
                    return lcp;
                int j;
                for (j = 0; j < lcp.length(); j++) {
                    if (strs[i].charAt(j) != lcp.charAt(j))
                        break;
                }
                lcp = lcp.substring(0, j);
            }
            return lcp;
        }
        */
        // Alg 2: Compare starting from the end of each string. Build up the longest common string in this process
        public String longestCommonPrefix(String[] strs) {
            if (strs.length == 0) {
                return "";
            }
            String lcp = "";
            int minlength = strs[0].length();
            for (int i = 0; i < strs.length; i++) {
                if (strs[i].length() < minlength)
                    minlength = strs[i].length();
            }
            for (int j = 0; j < minlength; j++) {
                char tmp = strs[0].charAt(j);
                for (int i = 0; i < strs.length; i++) {

                    if (strs[i].charAt(j) != tmp)
                        return lcp;

                }
                lcp = lcp + tmp;
            }
            return lcp;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String[] strs = new String[] {};
        System.out.println("Should be empty: " + s.longestCommonPrefix(strs));
        strs = new String[] {""};
        System.out.println("Should be empty: " + s.longestCommonPrefix(strs));
        strs = new String[] {"abc", "ab", "abcd"};
        System.out.println("Should be ab: " + s.longestCommonPrefix(strs));
    }
}
