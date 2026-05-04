class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq_s1 = [0] * 26
        freq_win = [0] * 26

        # build frequency for s1 and first window
        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            freq_win[ord(s2[i]) - ord('a')] += 1

        if freq_s1 == freq_win:
            return True

        # slide the window
        l = 0
        for r in range(len(s1), len(s2)):
            freq_win[ord(s2[r]) - ord('a')] += 1      # add right
            freq_win[ord(s2[l]) - ord('a')] -= 1      # remove left
            l += 1
            if freq_s1 == freq_win:
                return True

        return False