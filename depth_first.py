def depth_first_traversal(graph, start):
    visited = {}

    for k in graph:
        visited[k] = False

    node_stack = [start]
    visited[start] = True

    while len(node_stack) != 0:
      current_node = node_stack[len(node_stack) - 1]
      neighbors = graph[current_node]

graph = {
  "A" : ["B", "C", "D", "E"],
  "B" : ["A", "C", "E"],
  "C" : ["A", "B"],
  "D" : ["A", "E"],
  "E" : ["A", "B"]
}

depth_first_traversal(graph, "A")