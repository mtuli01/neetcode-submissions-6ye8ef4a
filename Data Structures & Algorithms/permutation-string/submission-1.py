class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        freq_count = [0] * 26
        for s in s1:
            freq_count[ord(s) - ord('a')] += 1
        
        freq_count_st = [0] * 26
        l = 0
        r = len(s1) - 1
        for s in s2[l:r+1]:
            freq_count_st[ord(s) - ord('a')] += 1
        if freq_count == freq_count_st:
                return True
        print(freq_count)
        if len(s1) == len(s2): return freq_count == freq_count_st
        while r < len(s2) - 1:
            print(freq_count_st)
            if freq_count == freq_count_st:
                return True
            else:
                freq_count_st[ord(s2[l]) - ord('a')] -= 1
                l+=1
                r+=1
                freq_count_st[ord(s2[r]) - ord('a')] += 1
                if freq_count == freq_count_st:
                    return True
        return False

