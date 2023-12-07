#sử dụng thuật toán đàn kiến để giải quyết bài toán Người bán hàng

import random

class MinGraph:
    def __init__(self, vertices, alpha=1, beta=1, initial_pheromone=1000, Q=100, evaporation_rate=0.5):
        self.V = vertices
        self.alpha = alpha
        self.beta = beta
        self.Q = Q
        self.evaporation_rate = evaporation_rate
        self.distance = [[0 for column in range(vertices)] 
                         for row in range(vertices)]
        self.pheromone = [[initial_pheromone for column in range(vertices)] 
                          for row in range(vertices)]
    
    def calculate_probability(self, current_vertex, visited_vertices):
        probabilities = [0 for _ in range(self.V)]
        for vertex in range(self.V):
            if vertex not in visited_vertices:
                probabilities[vertex] = (self.pheromone[current_vertex][vertex] ** self.alpha) * \
                                        ((1 / self.distance[current_vertex][vertex]) ** self.beta)
        s = sum(probabilities)
        probabilities = [prob / s for prob in probabilities]
        return probabilities
    
    def traverse_graph(self, start_vertex):
        visited_vertices = [start_vertex]
        current_vertex = start_vertex

        while len(visited_vertices) < self.V:
            probabilities = self.calculate_probability(current_vertex, visited_vertices)
            next_vertex = random.choices(range(self.V), weights=probabilities, k=1)[0]
            visited_vertices.append(next_vertex)
            current_vertex = next_vertex

        # Return to the start vertex to complete the cycle
        visited_vertices.append(start_vertex)

        return visited_vertices

    def update_pheromone(self, ant_paths):
        for ant_path in ant_paths:
            total_weight = sum(self.distance[ant_path[i-1]][ant_path[i]] for i in range(1, len(ant_path)))
            for i in range(len(ant_path) - 1):
                self.pheromone[ant_path[i]][ant_path[i+1]] += self.Q / total_weight
                self.pheromone[ant_path[i]][ant_path[i+1]] *= self.evaporation_rate

def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    num_vertices = int(lines[0].strip())
    graph = MinGraph(num_vertices)

    for i in range(1, num_vertices + 1):
        row = list(map(int, lines[i].strip().split()))
        graph.distance[i - 1] = row
    
    return graph

def simulate_ants(graph, k, iterations):
    best_path = None
    best_path_length = float('inf')

    for _ in range(iterations):
        ant_paths = []
        for _ in range(k):
            start_vertex = random.choice(range(graph.V))
            ant_path = graph.traverse_graph(start_vertex)
            ant_paths.append(ant_path)

            path_length = sum(graph.distance[ant_path[i-1]][ant_path[i]] for i in range(1, len(ant_path)))
            if path_length < best_path_length:
                best_path = ant_path
                best_path_length = path_length

        graph.update_pheromone(ant_paths)

    return best_path

# Đọc đồ thị từ tệp tin
filename = '/content/khoang_Cach.txt'
graph = read_graph_from_file(filename)

# Chạy thuật toán ACO với 2 con kiến và 100 lần lặp
best_path = simulate_ants(graph, 2, 100)

# In ra hành trình tốt nhất và độ dài của nó
print("Best path:", best_path)
best_path_length = sum(graph.distance[best_path[i-1]][best_path[i]] for i in range(1, len(best_path)))
print("Best path length:", best_path_length)
