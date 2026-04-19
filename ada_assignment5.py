# Delivery Route Optimization Mini Project
# Author: Adarsh Rai

import heapq
from itertools import permutations

# -------------------- DATA --------------------

dist_matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 8, 12, 18],
    [15, 8, 0, 9, 14],
    [20, 12, 9, 0, 7],
    [25, 18, 14, 7, 0]
]

# -------------------- TASK 3 --------------------
# Recursive Route Cost

def route_cost(current, visited, n):
    if len(visited) == n:
        return dist_matrix[current][0]

    min_cost = float('inf')
    for next_node in range(n):
        if next_node not in visited:
            visited.add(next_node)
            cost = dist_matrix[current][next_node] + route_cost(next_node, visited, n)
            min_cost = min(min_cost, cost)
            visited.remove(next_node)
    return min_cost


# -------------------- TASK 4 --------------------
# Greedy Parcel Selection

parcels = [
    {'id':'P1','value':500,'weight':2,'location':1},
    {'id':'P2','value':300,'weight':5,'location':2},
    {'id':'P3','value':700,'weight':3,'location':3},
    {'id':'P4','value':200,'weight':4,'location':4},
]

def greedy_selection(capacity):
    items = sorted(parcels, key=lambda x: x['value']/x['weight'], reverse=True)
    total_w, total_v = 0, 0
    selected = []

    for p in items:
        if total_w + p['weight'] <= capacity:
            selected.append(p['id'])
            total_w += p['weight']
            total_v += p['value']

    return selected, total_w, total_v


# -------------------- TASK 5 --------------------
# Dijkstra

def dijkstra(graph, src):
    n = len(graph)
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        for v in range(n):
            if graph[u][v] > 0:
                nd = dist[u] + graph[u][v]
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
    return dist


# -------------------- TASK 6 --------------------
# TSP Brute Force

def tsp_brute(dist, n):
    nodes = list(range(1, n))
    best_cost = float('inf')

    for perm in permutations(nodes):
        path = [0] + list(perm) + [0]
        cost = sum(dist[path[i]][path[i+1]] for i in range(len(path)-1))
        best_cost = min(best_cost, cost)

    return best_cost


# -------------------- MAIN --------------------

if __name__ == "__main__":
    n = 5

    print("Recursive Route Cost:", route_cost(0, {0}, n))

    selected, w, v = greedy_selection(10)
    print("Selected Parcels:", selected)
    print("Total Value:", v)

    print("Shortest Paths:", dijkstra(dist_matrix, 0))

    print("TSP Cost:", tsp_brute(dist_matrix, n))
