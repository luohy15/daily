from lib.tree import *

def test1():
    arr_in = [1,2,3]
    arr_out = [1,2,3]
    func = lambda x: x
    assert arr_out == tree2arr(func(arr2tree(arr_in)))