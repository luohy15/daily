from typing import List

class Proxy(object):
    def __init__(self, obj):
        object.__setattr__(self, "_obj", obj)

    def __getattribute__(self, name):
        return getattr(object.__getattribute__(self, "_obj"), name)
    def __setattr__(self, name, value):
        setattr(object.__getattribute__(self, "_obj"), name, value)

class Solution(object):
    def generateProxy(self, cls):
        return Proxy(cls)
