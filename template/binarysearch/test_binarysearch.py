from main_binarysearch import *

def test_lower_bound():
    assert lower_bound([-1, 0, 0, 3, 3, 3, 7, 8, 9], 3) == 3

def test_upper_bound():
    assert upper_bound([-1, 0, 0, 3, 3, 3, 7, 8, 9], 3) == 6