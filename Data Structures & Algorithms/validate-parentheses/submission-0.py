class Solution:
    def isValid(self, s: str) -> bool:
        par_map: dict = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for par in s:
            if par in par_map.keys():
                stack.append(par)
            else:
                if len(stack) == 0: return False
                last_par = stack[-1]
                if par == par_map[last_par]:
                    stack.pop()
                else:
                    stack.append(last_par)
        return len(stack) == 0