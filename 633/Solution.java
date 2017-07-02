public class Solution {
    public boolean judgeSquareSum(int c) {
        // For 1 to sqrt(c), store squares in a HashMap.
        // Go through again. See whether sum equals
        HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();
        int sq = (int)Math.sqrt(c);
        for (int i=0; i <= sq; i++) {
            dict.put(i*i, i);
        }
        for (int i=0; i <= sq; i++) {
            int r = c - (i*i);
            if (dict.containsKey(r)) {
                return true;
            }
        }
        return false;
    }
}
