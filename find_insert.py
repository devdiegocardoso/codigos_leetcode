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
        insert_index = 0
        while low <= high:
            mid = int((low + high) / 2)
            if target < nums[mid]:
                high = mid-1
                insert_index = mid
            elif target > nums[mid]:
                low = mid+1
                insert_index = low
            else:
                return mid
        return insert_index


s = Solution()
RESULT = s.search([1,3,5,6], 5)
print(RESULT)
RESULT = s.search([1,3,5,6], 2)
print(RESULT)
RESULT = s.search([1,3,5,6], 7)
print(RESULT)
RESULT = s.search([1,3,5,6], 0)
print(RESULT)
RESULT = s.search([1], 0)
print(RESULT)
RESULT = s.search([1,3], 2)
print(RESULT)