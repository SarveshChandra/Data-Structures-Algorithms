#User function Template for python3

class Solution:
    
    solution = []
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        solutionlen1 = len(self.solution)
        for index in range(c):
            i=0
            self.solution.append(matrix[i][index])
            j = index
        for index in range(1,r):
            self.solution.append(matrix[index][j])
            i = index
        for index in range(1,c):
            self.solution.append(matrix[i][c-index-1])
            j = c-index-1
        for index in range(1,r-1):
            self.solution.append(matrix[r-index-1][j])
            i = r-index-1
        
        solutionlen2 = len(self.solution)
        itemsadded = solutionlen2 - solutionlen1
        
        if itemsadded < r*c:
            next_matrix = []
            
            for index in range(r-2):
                next_matrix.append([])
                
            for index in range(r-2):
                for index2 in range(c-2):
                    next_matrix[index].append(matrix[index+1][index2+1])
                    
            if len(next_matrix) > 0:
                r = len(next_matrix)
                c = len(next_matrix[0])
                self.spirallyTraverse(next_matrix, r, c)
        
        return self.solution
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# user input
# 1
# 2 2
# 1 2 3 4
# 1 2 4 3 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends