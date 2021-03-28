import pytest

from main_1805 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]) == "bobistwoyearsold"
    assert Solution().evaluate("hi(name)", [["a","b"]]) == "hi?"
    assert Solution().evaluate("(a)(a)(a)aaa", [["a","yes"]]) == "yesyesyesaaa"
    assert Solution().evaluate("(a)(b)", [["a","b"],["b","a"]]) == "ba"