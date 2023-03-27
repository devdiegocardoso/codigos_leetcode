from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        TAM = len(nums)
        nums.reverse()
        p1, p2 = nums[:k], nums[k::]
        p1.reverse()
        p2.reverse()
        nums.clear()
        nums.extend(p1)
        nums.extend(p2)




lista = [1,2,3,4,5,6,7]
Solution().rotate(lista,3)
print(lista)