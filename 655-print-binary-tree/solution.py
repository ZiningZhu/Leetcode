class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        curr = root
        nrow = self.dfs(root) + 1
        #print ("nrow={}".format(nrow))
        
        ncol = (2 ** nrow) - 1
        #console = [[""] * ncol] * nrow
        console = []
        for i in range(nrow):
            console.append([""] * ncol)
        
        # Wrap them in functions and write in recursive form instead
        self.recursive_print(console, root, 0, 0, (2 ** (nrow-1)))
        
        return console
        
    def recursive_print(self, console, node, level, pos, width):
        if (node == None):
            return
        w = int(width)
        #print ("w={}, val={}, real_pos={}".format(w, node.val, ))
        console[level][2 * pos * w + w - 1] = str(node.val)
        self.recursive_print(console, node.left, level+1, 2*pos, width/2)
        self.recursive_print(console, node.right, level+1, 2*pos+1, width/2)
    
    def dfs(self, root):
        levels = 0
        st = [Node(root, 0)]
        while (len(st) > 0) :
            curr = st.pop()
            depth = curr.d;
            if (depth > levels):
                levels = depth
            if (curr.tn.left != None):
                st.append(Node(curr.tn.left, depth+1))
            if (curr.tn.right != None):
                st.append(Node(curr.tn.right, depth+1))
        return levels
        
        
class Node:
    def __init__(self, root, depth):
        self.tn = root
        self.d = depth