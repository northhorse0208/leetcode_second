from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hash_map = defaultdict(list)
        for str in strs:
            sorted_str = ''.join(sorted(str))
            hash_map[sorted_str].append(str)
        for value in hash_map.values():
            ans.append(value)

        return ans