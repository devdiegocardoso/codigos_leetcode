from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color != newColor:
            self.floodRecursive(image,sr,sc,color,newColor)
        return image

    def floodRecursive(self, image: List[List[int]], sr: int, sc: int,color:int, newColor: int) -> None:
        if image[sr][sc] == color:
            image[sr][sc] = newColor
            if sr >= 1:
                self.floodRecursive(image,sr-1,sc,color,newColor)
            if sc >= 1:
                self.floodRecursive(image,sr,sc-1,color,newColor)
            if sr < len(image)-1:
                self.floodRecursive(image,sr+1,sc,color,newColor)
            if sc < len(image[0])-1:
                self.floodRecursive(image,sr,sc+1,color,newColor)

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

r = Solution().floodFill(image,sr,sc,newColor)
print(r)