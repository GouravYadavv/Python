from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dictionary = defaultdict(list)
        result = []

        for i in strs:
            s = tuple(sorted(i))
            Dictionary[s].append(i)
        for i in Dictionary.values():
            result.append(i)
        return result


a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
