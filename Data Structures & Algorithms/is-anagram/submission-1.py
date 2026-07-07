class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            def to_hashtable(w):
                ht = {}
                for c in w:
                    if c in ht:
                        ht[c] = ht[c] + 1
                    else:
                        ht[c] = 1
                return ht
            return to_hashtable(s) == to_hashtable(t)
        