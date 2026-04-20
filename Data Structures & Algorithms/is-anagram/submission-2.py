class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charlist = [0] * 26

        for char in s:
            charlist[ord(char) - ord('a')] += 1
        
        for char in t:
            charlist[ord(char) - ord('a')] -= 1

        if any(charlist) != 0:
            return False
        else:
            return True