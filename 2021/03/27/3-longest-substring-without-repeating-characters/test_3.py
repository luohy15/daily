import pytest

from main_3 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3

def test2(Solution):
    assert Solution().lengthOfLongestSubstring("") == 0

def test3(Solution):
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1

def test4(Solution):
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
