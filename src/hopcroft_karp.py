from typing import Dict, List, Set

def hopcroft_karp_matching(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    Implement the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    Args:
        graph (Dict[int, List[int]]): A bipartite graph represented as an adjacency list.
                                      Keys are vertices from the left set, 
                                      Values are lists of adjacent vertices in the right set.
    
    Returns:
        Dict[int, int]: A maximum matching where keys are vertices from the left set 
                        and values are their matched vertices in the right set.
    
    Raises:
        ValueError: If the input graph is not a valid bipartite graph dictionary.
    """
    # Input validation
    if not isinstance(graph, dict):
        raise ValueError("Input must be a dictionary representing a bipartite graph")
    
    # Initialize data structures
    matching = {}  # Stores the current matching
    dist = {}      # Distance labels for breadth-first search
    
    def bfs() -> bool:
        """
        Breadth-first search to find augmenting paths.
        
        Returns:
            bool: True if an augmenting path exists, False otherwise.
        """
        # Initialize queue for BFS
        queue = []
        
        # Check unmatched vertices in the left set
        for u in graph:
            if u not in matching:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        # Set default distance for unmatched right vertices
        nil_vertex = 0
        dist[nil_vertex] = float('inf')
        
        # Perform BFS
        while queue:
            u = queue.pop(0)
            
            if dist[u] < dist[nil_vertex]:
                for v in graph[u]:
                    # Check if v is unmatched or can lead to an augmenting path
                    w = matching.get(v)
                    
                    if dist[w] == float('inf'):
                        dist[w] = dist[u] + 1
                        queue.append(w)
        
        # Return whether an augmenting path exists
        return dist[nil_vertex] != float('inf')
    
    def dfs(u: int) -> bool:
        """
        Depth-first search to find and update matching.
        
        Args:
            u (int): Current vertex from the left set.
        
        Returns:
            bool: True if an augmenting path is found, False otherwise.
        """
        # Check if vertex is unmatched or can lead to an augmenting path
        nil_vertex = 0
        if u != nil_vertex:
            for v in graph[u]:
                # Check next vertex in potential augmenting path
                w = matching.get(v)
                
                # Augmenting path condition
                if dist[w] == dist[u] + 1:
                    if dfs(w):
                        # Update matching
                        matching[v] = u
                        matching[u] = v
                        return True
            
            # Mark this vertex as part of a failed path
            dist[u] = float('inf')
            return False
        
        return True
    
    # Find maximum matching
    while bfs():
        for u in graph:
            if u not in matching:
                dfs(u)
    
    return {k: v for k, v in matching.items() if k in graph}