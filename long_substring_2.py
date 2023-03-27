class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        longest = 0
        count = 0
        size = len(s)
        i = 0
        for i in range(size):
            if i > size - longest:
                break
            for j in range(i,size):
                if s[j] not in s[i:j]:
                    count += 1
                else:
                    break
            longest = max(longest,count)
            count = 0
             
        return max(longest,count)




print(Solution().lengthOfLongestSubstring('dvdf'))
