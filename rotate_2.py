from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        TAM = len(nums)
        for _ in range(k):
            tmp = nums.pop()
            nums.insert(0,tmp)



lista = [1,2,3,4,5,6,7]
Solution().rotate(lista,3)
print(lista)