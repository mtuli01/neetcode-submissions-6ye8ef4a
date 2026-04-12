class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        for i in s:
            if  i not in hash_map_s:
                hash_map_s[i] = 1
            else:
                hash_map_s[i] += 1
        for j in t:
            if  j not in hash_map_t:
                hash_map_t[j] = 1
            else:
                hash_map_t[j] += 1
        print(hash_map_s, hash_map_t)
        if len(hash_map_s) != len(hash_map_t):
            return False
        else:
            for i in hash_map_s:
                if i not in hash_map_t:
                    return False
                elif hash_map_s[i] != hash_map_t[i]:
                    return False
            return True