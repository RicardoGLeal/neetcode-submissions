class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        i, res = 0, []
        visited = set()

        top = 0
        buttom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        while i < (len(matrix) * len(matrix[0])):

            for c in range(len(matrix[0])):
                #top
                if (top,c) in visited:
                    continue
                else:
                    res.append(matrix[top][c])
                    i += 1
                    visited.add((top,c))
            print(res)

            for r in range(n):
                if (r,right) in visited:
                    continue
                else:
                    #right
                    res.append(matrix[r][right])
                    i += 1
                    visited.add((r,right))
            print(res)

            for c in range(len(matrix[0])-1, -1, -1):
                if (buttom,c) in visited:
                    continue
                else:
                    #bottom
                    res.append(matrix[buttom][c])
                    i += 1
                    visited.add((buttom,c))
            print(res)
            
            for r in range(n-1, -1, -1):
                if (r,left) in visited:
                    continue
                else:
                    #left
                    res.append(matrix[r][left])
                    i += 1
                    visited.add((r,left))
            print(res)

            top += 1
            buttom -= 1
            left += 1
            right -= 1
        
        return res
            

 
            





        

