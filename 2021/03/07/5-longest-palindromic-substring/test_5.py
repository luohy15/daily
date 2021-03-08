import pytest

from main_5 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    res = Solution().longestPalindrome("babad")
    assert res == "bab" or res == "aba"

def test2(Solution):
    Solution().longestPalindrome("cbbd") == "bb"

def test3(Solution):
    Solution().longestPalindrome("a") == "a"

def test4(Solution):
    res = Solution().longestPalindrome("ac")
    assert res == "a" or res == "c"
