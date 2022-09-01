class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp=1
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                temp=0
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        # print(matrix)
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if temp==0:
                matrix[i][0]=0
        
        