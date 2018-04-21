"""
Regular solution using BFS.
The point is just to find out the number of vertices in each connected subgraph.
Then what's left is trivial.
"""

"""
Editorial solution: disjoint sets
"""
N, I = map(int, raw_input().strip().split())
assert 1 <= N <= 10**5
assert 1 <= I <= 10**6
lis_of_sets = []

for i in range(I):
    a,b = map(int, raw_input().strip().split())
    assert 0 <= a < N and 0 <= b < N
    indices = []
    new_set = set()
    set_len = len(lis_of_sets)
    s = 0
    while s < set_len:
        if a in lis_of_sets[s] or b in lis_of_sets[s]:
            indices.append(s)
            new_set = new_set.union(lis_of_sets[s])
            del lis_of_sets[s]
            set_len -= 1
        else:
            s += 1

    new_set = new_set.union([a, b])

    lis_of_sets.append(new_set)

answer = N*(N-1)/2
for i in lis_of_sets:
    answer -= len(i)*(len(i)-1)/2

print answer


"""
Hacking solution using disjoint sets.
Instead of constructing graphs, just join the sets
"""

N, P = tuple(map(int, input().strip().split(' ')))

sets = [{i} for i in range(N)]

arr = [i for i in range(N)] #sets[arr[i]] contains i

for i in range(P):
    a, b = tuple(map(int, input().strip().split(' ')))
    if a not in sets[arr[b]]:
        #union the sets
        u = sets[arr[a]] | sets[arr[b]]
        sets[a] = u #store the union at sets[a]
        for j in u: #pointers to a
            if j!=a:
                sets[j]=set()
            arr[j]=a
total = 0
non_singles = 0
for i in range(N):
    #print(sets[arr[i]], sets[i])
    L = len(sets[i])
    if L>1: #non-single set with length L
        non_singles += L
        #add pairs with first person in the subset
        total += L*(N-L)

#singles = N - non_singles
#add pairs with first person in the set of singles
total = total + (N-non_singles)*(N-1)

#remove double counting
total = total//2
print(total)
