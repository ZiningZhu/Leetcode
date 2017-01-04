public class Solution {

    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<String> ();
        if (n == 0) {

            res.add("");
            return res;
        }


        backtrack(res, "", 0, 0, n);
        return res;
    }

    private void backtrack(List<String> res, String s, int open, int close, int N) {
        if (open == N && close == N) {

            res.add(s);
            return;
        }
        if (open > N) {
            return;
        }
        if (open < N) {

            backtrack(res, s+"(", open+1, close, N);
        }
        if (close < open) { // Only append brackets that will balance the string out (a.k.a: NumOf(open)-NumOf(close) >= 0 at all times)

            backtrack(res, s+")", open, close+1, N);
        }
        return;
    }
}
