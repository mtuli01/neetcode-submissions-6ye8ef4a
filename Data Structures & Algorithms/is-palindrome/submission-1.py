class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        ns = ""
        for char in s:
            if char.isalnum(): 
                ns += char.lower()
        print(ns)
        return ns == ns[::-1]