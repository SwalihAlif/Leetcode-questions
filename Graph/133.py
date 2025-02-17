#133 clone Graph
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        visited = {}
        def dfs(current_node):
            if current_node in visited:
                return visited[current_node]
            cloned_node = Node(current_node.val)
            visited[current_node] = cloned_node

            for nei in current_node.neighbors:
                cloned_node.neighbors.append(dfs(nei))
            return cloned_node
        return dfs(node)
    
