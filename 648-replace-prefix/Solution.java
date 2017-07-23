public class Solution {
    public class Trie {
        private int count;
        private Trie[] branches;

        public Trie() {
            count = 0;
            branches = new Trie[26];
        }

        private int int_(int c) {
            return c - 'a';
        }

        public void insert(String word) {
            if (word == null || word.length() == 0) {
                this.count += 1;
                return;
            }

            int idx = int_(word.charAt(0));

            if (this.branches[idx] == null) {
                this.branches[idx] = new Trie();
                this.branches[idx].insert(word.substring(1));
            } else {
                this.branches[idx].insert(word.substring(1));
            }

        }

        public int checkPrefix(String word) {
            // Returns -1 if no prefix found. Only invoked in the root
            Trie curr = this;
            for (int i = 0; i < word.length(); i++) {
                int idx = int_(word.charAt(i));
                if (curr.count > 0) {
                    return i;
                }
                if (curr.branches[idx] == null) {
                    return -1;
                } else {
                    curr = curr.branches[idx];
                }
            }
            return -1; // No prefix anyways

        }
    }
    public String replaceWords(List<String> dict, String sentence) {
        Trie t = new Trie();
        for (String s : dict) {
            t.insert(s);
        }
        String res = "";
        String[] d2 = sentence.split(" ");
        for (int i = 0; i < d2.length; i++) {
            String s = d2[i];
            int tmp = t.checkPrefix(s);
            if (tmp > 0) {
                res += s.substring(0, tmp);
            } else {
                res += s;
            }
            if (i < d2.length-1) {
                res += " ";
            }
        }
        return res;
    }
}
