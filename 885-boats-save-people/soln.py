class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # Greedy solution. Pick the heaviest remaining that can fit on boat. n^2. TLE
        """
        people.sort(key=lambda x: -x)

        taken = [0] * len(people)
        boats = 0

        for i in range(len(people)):
            if taken[i]:
                continue
            taken[i] = 1
            for j in range(i+1, len(people)):
                if taken[j]:
                    continue
                if people[i] + people[j] <= limit:
                    taken[j] = 1
                    break
            boats += 1
        return boats

        # Optimized solution. Passed
        people.sort(key=lambda x: -x)
        boats = 0

        if len(people) == 1:
            return 1
        j = 1
        while j < len(people) and people[0] + people[j] > limit:
            j += 1

        while len(people) > 0:
            # j is the position of sentinel (largest passenger summing to below limit, w.r.t previous i)
            #print j, boats, people

            # First search left
            can_go_left = False
            while j > 0 and j < len(people) and people[0] + people[j] <= limit:
                j -= 1
                can_go_left = True
            if j <= 0:  # Anyone is fine
                if len(people) == 1:
                    return boats+1
                else:
                    people.pop(1)
                    people.pop(0)
                    boats += 1
                    j = min(1, len(people)-1)
            else:
                if can_go_left:
                    j += 1
                    people.pop(j)
                    people.pop(0)
                    boats += 1
                    j -= 2
                else:
                    j += 1
                    if j >= len(people):
                        people.pop(0)
                        boats += 1
                        j = len(people)-1
                    else:
                        people.pop(j)
                        people.pop(0)
                        boats += 1
                        j -= 2
        return boats
        """
        # Solution 3: Pick the lightest available.
        # This passed...? LMFAO
        people.sort(key=lambda x: -x)
        boats = 0
        while len(people) > 0:
            if len(people) == 1:
                return boats+1

            if people[0] + people[-1] > limit:
                boats += 1
                people.pop(0)
            else:
                people.pop(0)
                people.pop()
                boats += 1
        return boats


        
