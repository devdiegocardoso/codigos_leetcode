class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        longest = 1
        list_char = []
        i = 0
        while i < len(s) - longest:
            list_char.append(s[i])
            match = False
            j = i + 1
            while j < len(s) and not match:
                if s[j] not in list_char:
                    list_char.append(s[j])
                else:
                    match = True
                j += 1
            longest = max(len(list_char), longest)
            list_char.clear()
            i += 1
                
        return max(longest,len(list_char))




print(Solution().lengthOfLongestSubstring('bbbbbbb'))
