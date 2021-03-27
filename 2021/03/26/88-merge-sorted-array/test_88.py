import pytest

from main_88 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]

def test2(Solution):
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1]