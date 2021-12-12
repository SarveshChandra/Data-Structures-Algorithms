// Rotating a 2D Matrix
// Given a two-dimensional square matrix (n x n), rotate the matrix 90 degrees to the right (clockwise). 

// Example 1:
// Input:
// [
//   [ 1,  2,  3, 4],
//   [ 5,  6,  7, 8],
//   [ 9, 10, 11, 12],
//   [13, 14, 15, 16]
// ],

// Output:
// [
//  [13,  9, 5, 1],
//  [14, 10, 6, 2],
//  [15, 11, 7, 3],
//  [16, 12, 8, 4]
// ]

// Example 2:
// Input:
// [
//   [10, 20],
//   [30, 40]
// ],

// Output:
// [
//  [30, 10],
//  [40, 20]
// ]

// Challenge:
// Can you do the rotation in-place?

#include<iostream>
#include<string>
#include<bits/stdc++.h>
#include"../mytemplate.h"

using namespace std;

class Solution {
  public:

    // Way 1: A layer by layer rotation.
    vector<vector<int>> rotate(vector<vector<int>>& matrix) {
        int size = matrix.size() - 1; // this is really the last index
        deb(size);

        for (int layer = 0; layer < (matrix.size() / 2); layer++) {
            deb2(layer, (matrix.size() / 2));
            for (int i = layer; i < size - layer; i++) {
                deb2(i, (size - layer));
                int topFence = matrix[layer][i];                  // starts at top left of layer
                int rightFence = matrix[i][size - layer];         // starts at top right of layer
                int bottomFence = matrix[size - layer][size - i]; // starts at bottom right of layer
                int leftFence = matrix[size - i][layer];          // starts at bottom left of layer

                // rotate 90 degrees clockwise element by element
                matrix[layer][i] = leftFence;                     // set value walking top fence
                matrix[i][size - layer] = topFence;               // set value walking right fence
                matrix[size - layer][size - i] = rightFence;      // set value walking bottom fence
                matrix[size - i][layer] = bottomFence;            // set value walking left fence
            }
        }

        return matrix;
    }


    // Way 2: Matrix Transpose
    // We flip the matrix vertically and take its transpose.
    vector<vector<int>> rotate2(vector<vector<int>>& matrix) {
      int r = matrix.size(), c = matrix[0].size();
        // Transpose Of Matrix        
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                if(i<=j){
                    swap(matrix[i][j], matrix[j][i]);
                }
            }
        }
        // Swapping Columns from left to right till half         
        for(int i=0; i<c/2; i++){
            for(int j=0; j<r; j++){
                swap(matrix[j][i], matrix[j][r-i-1]);
            }
        }

    return matrix;
    }

};

int main() {
    Solution a;

    vector<vector<int>> input = {
        { 1,  2,  3, 4},
        { 5,  6,  7, 8},
        { 9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    vector<vector<int>> output = a.rotate(input);
    for(auto r:output) {
        for(auto c:r) {
            cout<<c<<" ";
        }
        cout<<endl;
    }

    cout<<endl;

    vector<vector<int>> input2 = {
        { 1,  2,  3, 4},
        { 5,  6,  7, 8},
        { 9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    vector<vector<int>> output2 = a.rotate2(input2);
    for(vector<int> r:output2) {
        for(int c:r) {
            cout<<c<<" ";
        }
        cout<<endl;
    }
    getchar();
}