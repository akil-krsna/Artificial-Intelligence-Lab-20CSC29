def is_valid(graph, vertex, color, color_assignment):
    for neighbor in graph[vertex]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

def color_graph(graph, colors):
    color_assignment = {}
    for vertex in sorted(graph, key=lambda v: -len(graph[v])):
        available_colors = set(colors)
        for neighbor in graph[vertex]:
            if neighbor in color_assignment:
                available_colors.discard(color_assignment[neighbor])
        if available_colors:
            color_assignment[vertex] = min(available_colors)
    return color_assignment

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D']
    }
    colors = ['Red', 'Blue', 'Green']

    color_assignment = color_graph(graph, colors)
    for vertex, color in color_assignment.items():
        print(f"Vertex {vertex} is colored {color}")

if __name__ == "__main__":
    main()
