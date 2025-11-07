
import sys
from os import path

def test_functions():
    """Test math_tools operations functions."""
    assert gcd(48, 18) == 6
    assert lcm(4, 5) == 20
    assert is_prime(7) is True
    assert is_prime(10) is False
    assert mean([1, 2, 3, 4, 5]) == 3.0

    """Test edge cases"""
    assert gcd(0, 5) == 5
    assert lcm(0, 5) == 0

    """Test mean with empty data"""
    try:
        mean([])
    except ValueError as e:
        assert str(e) == "mean: data must not be empty" 
    else:
        assert False, "Expected ValueError for empty data in mean()"

    print("All tests passed.")

if __name__ == "__main__":
    base_dir = path.dirname(path.realpath(__file__))
    sys.path.append(base_dir[:-5])
    from math_tools import gcd, lcm, is_prime, mean
    test_functions()