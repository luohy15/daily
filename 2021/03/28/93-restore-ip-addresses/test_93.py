import pytest

from main_93 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().restoreIpAddresses("25525511135")  == ["255.255.11.135","255.255.111.35"]
    assert Solution().restoreIpAddresses("0000")  == ["0.0.0.0"]
    assert Solution().restoreIpAddresses("1111")  == ["1.1.1.1"]
    assert Solution().restoreIpAddresses("010010")  == ["0.10.0.10","0.100.1.0"]
    assert Solution().restoreIpAddresses("101023")  == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
