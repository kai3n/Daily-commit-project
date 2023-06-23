# Given a stochastic process it is useful to know the hitting/stopping times associated with it. For instance if we represent the process as a graph we would like to know the time/number of steps required to reach a node, and more in general the probability distribution of such traversal times.

# The graph is represented by an adjacency map
# E.g.
adj_map = {0: [1, 3], 1: [4, 5, 3], 2: [1, 4], 3: [1], 4: [5], 5: []}
start = 0
end = 4
d = 2

def is_reachable(start, end, d, adj_map):
    queue = [[start, 1]]
    prob_of_success = 0
    for _ in range(d + 1):
        for _ in range(len(queue)):
            node, prob = queue.pop(0) # start
            if node == end:
                prob_of_success += prob
            for nei in adj_map[node]:
                queue.append([nei, prob/len(adj_map[node])])
    return prob_of_success
        
print(is_reachable(start, end, d, adj_map))

# V nodes, E edges  O(VE)
# V nodes, E dges

# We would like to know the probability of reaching end from start in d or fewer steps, assuming we perform a random walk.
