class Solution(object):

    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # For each person, just pick the most profitable task based on their ability
        # N: # workers, M: # tasks
        # The brute force implementation for above, O(NM), gets TLE
        # Idea to optimize:
        # Sort people by capacity. The current person's capacity is not lower than previous one
        # One more step - use the best_profit variable to track the best profitable task up till the current difficulty

        tasks = []
        for t in range(len(difficulty)):
            tasks.append((difficulty[t], profit[t]))
        tasks = sorted(tasks)
        ws = sorted(worker)

        np = 0
        t = 0
        best_profit = 0
        for w in range(len(ws)):
            while t < len(tasks) and tasks[t][0] <= ws[w]:
                if tasks[t][1] > best_profit:
                    best_profit = tasks[t][1]
                t += 1
            if t == 0: continue
            np += best_profit
        return np
        
