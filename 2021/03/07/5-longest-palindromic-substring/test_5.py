import unittest

from main_5 import Solution

def test1():
    res = Solution().longestPalindrome("babad")
    assert res == "bab" or res == "aba"

def test2():
    checkFunc("cbbd", "bb")

def test3():
    checkFunc("a", "a")

def test3():
    res = Solution().longestPalindrome("ac")
    assert res == "a" or res == "c"

def checkFunc(sin, sout):
    assert Solution().longestPalindrome(sin) == sout
