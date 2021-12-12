class Solution:
    # way 1: layer by layer rotation
    def rotate(self, matrix):
        '''
        :type matrix: list of list of int
        :rtype: list of list of int
        '''
        size = len(matrix) - 1

        for layer in range(0, len(matrix) // 2):
            for i in range(layer, size - layer):
                # starts at top left of layer
                top_fence = matrix[layer][i]
                # starts at top right of layer
                right_fence = matrix[i][size - layer]
                # starts at bottom right of layer
                bottom_fence = matrix[size - layer][size - i]
                # starts at bottom left of layer
                left_fence = matrix[size - i][layer]

                # rotate 90 degrees clockwise element by element
                # set value walking top fence
                matrix[layer][i] = left_fence
                # set value walking right fence
                matrix[i][size - layer] = top_fence
                # set value walking bottom fence
                matrix[size - layer][size - i] = right_fence
                # set value walking left fence
                matrix[size - i][layer] = bottom_fence

        return matrix

    # Way 2: Matrix Transpose
    # We flip the matrix vertically and take its transpose.
    def rotate2(self, matrix):
        '''
        :type matrix: list of list of int
        :rtype: list of list of int
        '''
        self.flipVertically(matrix)
        self.transpose(matrix)

        return matrix
    # This is the first step
    # It flips the matrix vertically
    def flipVertically(self, matrix):
        for top_row in range(0, len(matrix) // 2):
            bottom_row = len(matrix) - 1 - top_row

            temp = matrix[top_row]
            matrix[top_row] = matrix[bottom_row]
            matrix[bottom_row] = temp
    
    # This is the second step 
    # It creates transpose of the matrix
    # Interchanges rows and columns
    def transpose(self, matrix):
        for row in range(0, len(matrix)):
            for col in range(row + 1, len(matrix[0])):
                value_in_upper_triangle = matrix[row][col]
                value_in_lower_triangle = matrix[col][row]

                matrix[row][col] = value_in_lower_triangle
                matrix[col][row] = value_in_upper_triangle


a = Solution()
input = [
   [ 1,  2,  3, 4],
   [ 5,  6,  7, 8],
   [ 9, 10, 11, 12],
   [13, 14, 15, 16]
 ]
b = a.rotate(input)
print(b)
input = [
   [ 1,  2,  3, 4],
   [ 5,  6,  7, 8],
   [ 9, 10, 11, 12],
   [13, 14, 15, 16]
 ]
c = a.rotate2(input)
print(c)