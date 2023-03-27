"""[summary]

Returns:
    [type]: [description]
"""
class Solution:
    """[summary]
    """
    def __init__(self):
        self.bad = 1

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        low, high = 1, n
        while low <= high:
            if low == high:
                return low
            mid = (low + high) // 2
            call_1 = self.isBadVersion(mid)
            call_2 = self.isBadVersion(mid+1)
            if not call_1 and call_2:
                return mid+1
            elif call_1:
                high = mid
            else:
                low = mid + 1
    
    def isBadVersion(self,n):
        return n >= self.bad

s = Solution()
print(s.firstBadVersion(2))