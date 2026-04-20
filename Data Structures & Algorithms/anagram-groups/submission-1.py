class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for word in strs:
            visited = [0] * 26
            for char in word:
                visited[ord(char) - ord('a')] += 1
            visited = tuple(visited)
            if visited in strs_dict:
                strs_dict[visited].append(word)
            
            else:
                strs_dict[visited] = []
                strs_dict[visited].append(word)
        
        return list(strs_dict.values())
                