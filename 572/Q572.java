/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    private int t_elem;
    private boolean isIdentical(TreeNode s, TreeNode t) {
        Stack<TreeNode> s1 = new Stack<TreeNode>();
        Stack<TreeNode> s2 = new Stack<TreeNode>();
        s1.push(s);
        s2.push(t);
        int traversed = 0;
        while (s1.size() > 0) {
            TreeNode c1 = s1.pop();
            TreeNode c2 = s2.pop();
            traversed += 1;
            if (c1.val != c2.val) {
                return false;
            }
            if (c1.left != null) {
                if (c2.left == null)
                    return false;
                s1.push(c1.left);
                s2.push(c2.left);
            }
            if (c1.right != null) {
                if (c2.right == null)
                    return false;
                s1.push(c1.right);
                s2.push(c2.right);
            }
        }
        return traversed == t_elem;
    }
    public boolean isSubtree(TreeNode s, TreeNode t) {
        // Brute force: BFS each node; upon finding a node equal to t.val, start the comparison routine.
        ArrayList<TreeNode> qt = new ArrayList<TreeNode>();
        qt.add(0, t);
        while (qt.size() > 0) {
            TreeNode curr = qt.remove(qt.size()-1);
            t_elem += 1;
            if (curr.left != null) {
                qt.add(0, curr.left);
            }
            if (curr.right != null) {
                qt.add(0, curr.right);
            }
        }


        ArrayList<TreeNode> q = new ArrayList<TreeNode>();
        q.add(0, s);
        while (q.size() > 0) {
            TreeNode curr = q.remove(q.size()-1);
            if (isIdentical (curr, t)) {
                return true;
            }
            if (curr.left != null) {
                q.add(0, curr.left);
            }
            if (curr.right != null) {
                q.add(0, curr.right);
            }
        }
        return false;
    }
}
