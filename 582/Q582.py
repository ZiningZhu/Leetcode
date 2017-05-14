class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        # Just look for all children of an element in a tree. Prestore all stuffs into a dictionary to save time from O(n^2) to O(n).
        q = [kill]
        ans = []

        child = {}
        for i in range(len(pid)):
            kid = pid[i]
            parent = ppid[i]
            if parent not in child:
                child[parent] = [kid]
            else:
                child[parent].append(kid)


        while (len(q) > 0):
            curr = q.pop(0)
            ans.append(curr)
            if curr in child:
                q.extend(child[curr])


        return ans
