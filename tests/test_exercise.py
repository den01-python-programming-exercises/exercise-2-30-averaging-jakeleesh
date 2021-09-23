import pytest
from src.exercise import sum,average

def test_exercise():
    assert sum(3,2,6,5) == 16
    assert average(3,2,6,5) == 4
