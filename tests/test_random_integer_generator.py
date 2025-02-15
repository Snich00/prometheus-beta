import pytest
from src.random_integer_generator import generate_random_integer

def test_generate_random_integer_within_range():
    # Test multiple times to ensure randomness
    for _ in range(100):
        result = generate_random_integer(1, 10)
        assert 1 <= result <= 10, f"Generated value {result} is not within range [1, 10]"

def test_generate_random_integer_same_min_max():
    result = generate_random_integer(5, 5)
    assert result == 5, "Result should be exactly 5 when min and max are the same"

def test_generate_random_integer_negative_range():
    for _ in range(100):
        result = generate_random_integer(-10, -1)
        assert -10 <= result <= -1, f"Generated value {result} is not within range [-10, -1]"

def test_generate_random_integer_mixed_range():
    for _ in range(100):
        result = generate_random_integer(-5, 5)
        assert -5 <= result <= 5, f"Generated value {result} is not within range [-5, 5]"

def test_generate_random_integer_invalid_range():
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 1)

def test_generate_random_not_always_same():
    # Probabilistic test to ensure randomness
    results = {generate_random_integer(1, 10) for _ in range(100)}
    assert len(results) > 1, "Generated numbers are not random"