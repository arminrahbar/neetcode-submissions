class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)

        return list(groups.values())

        # Another Version:
        # groups = {}

        # for word in strs:
        #     count = [0] * 26

        #     for char in word:
        #         index = ord(char) - ord('a')
        #         count[index] += 1

        #     key = tuple(count)

        #     if key not in groups:
        #         groups[key] = []

        #     groups[key].append(word)

        # return list(groups.values())
