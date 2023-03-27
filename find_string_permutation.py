import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size_search = len(s1)
        f_search = collections.Counter(s1)
        size_string = len(s2)

        for i in range(size_string-size_search+1):
            f_group = collections.Counter(s2[i:i+size_search])
            search_keys = list(f_search)
            group_keys = list(f_group)
            search_keys.sort()
            group_keys.sort()
            if search_keys == group_keys:
                match = all(f_search[key] == f_group[key] for key in f_search)
                if match:
                    return True
        return False


print(Solution().checkInclusion("adc","dcda"))
