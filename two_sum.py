from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)-1
        while low < high:
            if numbers[low] + numbers[high] == target:
                return [low+1,high+1]
            elif numbers[low] + numbers[high] > target:
                high -= 1
                while numbers[high] == numbers[high+1]:
                    high -= 1 
            else:
                low += 1
                while numbers[low] == numbers[low-1]:
                    low += 1

r = Solution().twoSum([-3,3,4,90],0)
print(r)