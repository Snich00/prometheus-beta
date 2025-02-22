import pytest
from src.hopcroft_karp import hopcroft_karp_matching

def test_empty_graph():
    """Test matching for an empty graph."""
    graph = {}
    assert hopcroft_karp_matching(graph) == {}

def test_simple_matching():
    """Test a simple bipartite graph with a clear matching."""
    graph = {
        1: [4],
        2: [5],
        3: [6]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Verify matching is valid
    assert len(matching) == 3
    assert matching[1] == 4
    assert matching[2] == 5
    assert matching[3] == 6

def test_complex_matching():
    """Test a more complex bipartite graph with multiple possible matchings."""
    graph = {
        1: [4, 5],
        2: [4, 6],
        3: [5, 6]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Verify matching properties
    assert len(matching) == 3
    # Each vertex should be matched to at most one other vertex
    assert len(set(matching.values())) == len(matching)

def test_multiple_matches_per_vertex():
    """Test graph where vertices can be matched to multiple others."""
    graph = {
        1: [4, 5, 6],
        2: [4, 5],
        3: [6]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Verify matching properties
    assert len(matching) <= 3
    # Each matched vertex should only appear once in the matching
    assert len(set(matching.values())) == len(matching)

def test_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(ValueError):
        hopcroft_karp_matching([1, 2, 3])  # Not a dictionary
    
    with pytest.raises(ValueError):
        hopcroft_karp_matching(None)  # None input

def test_unbalanced_graph():
    """Test a graph with unequal set sizes."""
    graph = {
        1: [4, 5, 6, 7],
        2: [5],
        3: [6]
    }
    matching = hopcroft_karp_matching(graph)
    
    # Verify matching is valid
    assert len(matching) <= 3
    # Verify no duplicate matches
    assert len(set(matching.values())) == len(matching)