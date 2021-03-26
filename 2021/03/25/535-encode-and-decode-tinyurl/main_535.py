from typing import List

def convert10to62(num):
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    if num == 0:
        return "0"
    while num > 0:
        res = chars[num % 62] + res
        num //= 62
    return res

def convert62to10(s):
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = 0
    for c in s:
        res *= 62
        res += chars.index(c)
    return res

class Codec:

    def __init__(self):
        super().__init__()
        self.cid = 0
        self.short2long = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = "http://tinyurl.com/" + convert10to62(self.cid)
        self.cid += 1
        self.short2long[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short2long[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))