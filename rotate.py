from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        TAM = len(nums)
        tmp = nums[:]
        for i, _ in enumerate(nums):
            nums [(i+k)%TAM] = tmp[i]



lista = [1,2,3,4,5,6,7]
Solution().rotate(lista,3)
print(lista)