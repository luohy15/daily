import pytest

from main_139 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().wordBreak("leetcode", ["leet", "code"]) == True

def test2(Solution):
    assert Solution().wordBreak("applepenapple", ["apple", "pen"]) == True

def test3(Solution):
    assert Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False

def test4(Solution):
    assert Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == False