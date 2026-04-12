class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_map = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key not in main_map:
                main_map[key] = []

            main_map[key].append(word)

        return list(main_map.values())