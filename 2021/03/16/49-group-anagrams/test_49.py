import pytest

from main_49 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]
    assert list(map(lambda arr : sorted(arr), Solution().groupAnagrams(strs))) == res
