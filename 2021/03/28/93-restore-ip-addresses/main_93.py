from typing import List

def check(s):
    if s[0] == "0":
        return len(s) == 1
    return 0 < int(s) <= 255

class Solution(object):
    """
    暴力
        枚举4段长度，判断是否合法
    time: O(1)
    space: O(1)
    """
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        for a in range(1,4):
            for b in range(1,4):
                for c in range(1,4):
                    for d in range(1,4):
                        if a + b + c + d == len(s):
                            s1 = s[0:a]
                            s2 = s[a:a+b]
                            s3 = s[a+b:a+b+c]
                            s4 = s[a+b+c:a+b+c+d]
                            if check(s1) and check(s2) and check(s3) and check(s4):
                                res.append(f"{s1}.{s2}.{s3}.{s4}")
        return res
