from collections import deque

def breadth_first(graph, start):
    visited = {}

    for k in graph:
        visited[k] = False

    node_queue = deque(start)

    while len(node_queue) != 0:
        current_node = node_queue.popleft()
        print current_node
        visited[n] = True
        neighbors = graph[current_node]

        for n in neighbors:
            if not visited[n]:
                node_queue.append(n)

graph = {
  "A" : ["B", "C", "D", "E"],
  "B" : ["A", "C", "E"],
  "C" : ["A", "B"],
  "D" : ["A", "E"],
  "E" : ["A", "B"]
}

breadth_first_traversal(graph, "A")