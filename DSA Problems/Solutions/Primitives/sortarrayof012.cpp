// Sort array having 0,1 and 2 only
// You are given an array nums containing only 0 , 1 and 2. You need to sort the array in ascending order.


// Note: 

// Do not use any built-in sorting algorithms.
// Interviewers usually ask to solve it in O(n) time complexity and single pass.
// You should not use any extra memory.

// Example 1:
// Input: [0,1,2,1,2,2,2,1,0]
// Output: [0,0,1,1,1,2,2,2,2]


// Example 2:
// Input: [2,2,1,1,1,0,0,0,0]
// Output: [0,0,0,0,1,1,1,2,2]


// Constraints: 

// 0 <= nums[I] <=2

#include<iostream>
#include<bits/stdc++.h>

using namespace std;

class Solution{
public:
    vector<int> sortArray_0_1_2(vector<int>& nums) {
        //Counting Sort Algorithm
    
        // Make three variables
        // For counting 0,1 and 2 respectively
        int num0 = 0, num1 = 0, num2 = 0;
        int n=nums.size();
    
        //Iterate through the array and count the frequencies of each number
        for(int i = 0; i < n; i++) {
            if (nums[i] == 0) ++num0;
            else if (nums[i] == 1) ++num1;
            else if (nums[i] == 2) ++num2;
        }
    
        //Fill the original array
        //First fill all 0, then 1 and at last 2
        for(int i = 0; i < num0; ++i) nums[i] = 0;
        for(int i = 0; i < num1; ++i) nums[num0+i] = 1;
        for(int i = 0; i < num2; ++i) nums[num0+num1+i] = 2;
    
        return nums;
    }
};

int main() {
    Solution a;
    vector<int> input = {0,1,2,1,2,2,2,1,0};
    vector<int> output = a.sortArray_0_1_2(input);
    for (int element:output) {
        cout<<element<<" ";
    }
    getchar();
}

// Counting Sort Approach
// The Approach is count the number of 0,1 and 2 in separate variables. This approach requires linear time. However this approach requires 2 Pass.