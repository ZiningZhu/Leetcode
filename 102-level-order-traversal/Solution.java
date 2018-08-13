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
    private class MTreeNode {
        int depth;
        TreeNode tn;
        MTreeNode (TreeNode t, int d) {tn = t; this.depth=d;}
        int getDepth() {return this.depth;}
    }

    public List<List<Integer>> levelOrder(TreeNode root) {
        ArrayList<MTreeNode> q = new ArrayList<MTreeNode>();
        List<Integer> levelans = new ArrayList<Integer>();
        List<List<Integer>> ans = new ArrayList<List<Integer>>();

        if (root == null) {
            System.out.println("Root is null!");
            return ans;
        }

        int prev_d = 0;
        q.add(new MTreeNode(root, 0));
        while ( q.size() != 0) {
            MTreeNode mt = q.remove(0);

            int dc = mt.getDepth();

            if (dc > prev_d) {
                ans.add(levelans);
                levelans = new ArrayList<Integer>();
                prev_d = dc;
                levelans.add(mt.tn.val);
                //levelans.clear();
            } else {
                levelans.add(mt.tn.val);
            }


            if (mt.tn.left != null) {
                MTreeNode l = new MTreeNode(mt.tn.left, dc+1);
                q.add(l);
            }
            if (mt.tn.right != null) {
                MTreeNode r = new MTreeNode(mt.tn.right, dc+1);
                q.add(r);
            }
        }
        ans.add(levelans);
        return ans;
    }
}

/*
1. Use private class instead of parallel existing classes.
2. List<Integer> sth = new ArrayList<Integer>, but when it comes to List of List, instantiate them as ArrayList<List<T>>, because Java generics are not covariant.
*/
