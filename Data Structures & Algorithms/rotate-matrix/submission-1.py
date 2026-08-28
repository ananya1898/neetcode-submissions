class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for i in range(n):
            l=0
            h=n-1
            while(l<h):
                matrix[i][l],matrix[i][h]=matrix[i][h],matrix[i][l]
                l+=1
                h-=1
                
