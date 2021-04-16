import pytest

from main_535 import Codec as Codec0
from main_535 import convert10to62, convert62to10

@pytest.fixture(params=[Codec0])
def Codec(request):
    return request.param

def test1(Codec):
    codec = Codec()
    url = "https://leetcode-cn.com/problems/encode-and-decode-tinyurl/"
    assert codec.decode(codec.encode(url)) == url

def test10to62():
    assert convert10to62(0) == "0"
    assert convert10to62(10) == "a"
    assert convert10to62(61) == "Z"
    assert convert10to62(62) == "10"

def test62to10():
    assert convert62to10("0") == 0
    assert convert62to10("a") == 10
    assert convert62to10("Z") == 61
    assert convert62to10("10") == 62
