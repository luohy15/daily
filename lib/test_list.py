from lib.list import *

def test1():
    arr_in = [1,2,3]
    arr_out = [1,2,3]
    func = lambda x: x
    assert arr_out == list2arr(func(arr2list(arr_in)))
