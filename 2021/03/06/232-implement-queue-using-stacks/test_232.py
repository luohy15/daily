import unittest

from main_232 import MyQueue

def test1():
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    assert obj.peek() == 1
    assert obj.pop() == 1
    assert obj.empty() == False
