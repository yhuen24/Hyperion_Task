class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, value, edges=[]):
        if value not in self.graph:
            self.graph[value] = edges

    def is_cyclic(self):
        visited = set()
        stack = list(self.graph.keys())

        while stack:
            node = stack.pop()
            if node in visited:
                return True
            visited.add(node)
            stack.extend(self.graph[node])
        return False

# driver code
my_graph = Graph()
my_graph.add_node("A", ["B", "C"])
my_graph.add_node("B")
my_graph.add_node("C", ["D"])
my_graph.add_node("D", ["E"])
my_graph.add_node("E", ["A", "C"])
for key, value in my_graph.graph.items():
    print(f"{key} : {value}")

print(my_graph.is_cyclic())
