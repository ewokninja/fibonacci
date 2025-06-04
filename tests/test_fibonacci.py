import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from fibonacci_app import compute_fibonacci

def test_first_five():
    assert compute_fibonacci(5) == [0, 1, 1, 2, 3]

def test_single_value():
    assert compute_fibonacci(1) == [0]

def test_invalid():
    with pytest.raises(ValueError):
        compute_fibonacci(0)

