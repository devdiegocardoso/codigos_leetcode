"""[summary]

Returns:
    [type]: [description]
"""
from typing import List

class Solution:
    """[summary]
    """
    def search(self, nums: List[int], target: int) -> int:
        """[summary]

        Args:
            nums (List[int]): [description]
            target (int): [description]

        Returns:
            int: [description]
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = int((low + high) / 2)
            if target < nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low = mid+1
            else:
                return mid
        return -1


s = Solution()
RESULT = s.search([-1,0,3,5,9,12], 9)
print(RESULT)
