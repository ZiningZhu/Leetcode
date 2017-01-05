public class Solution {

    public boolean isValid(String s) {
        Stack<Character> ss = new Stack<Character>();
        HashMap<Character, Character> mmap = new HashMap<Character, Character>();
        mmap.put("(".charAt(0), ")".charAt(0));
        mmap.put("[".charAt(0), "]".charAt(0));
        mmap.put("{".charAt(0), "}".charAt(0));
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == "(".charAt(0) || s.charAt(i) == "[".charAt(0) || s.charAt(i) == "{".charAt(0)) {
                ss.push(s.charAt(i));
            } else if (!ss.empty() && s.charAt(i) == mmap.get(ss.peek())) {
                ss.pop();
            } else {
                return false;
            }

        }
        return ss.empty();
    }
}
