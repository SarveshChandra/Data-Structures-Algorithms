// Given two strings s1 and s2 consisting of digits between 0 to 9, return a string representing the sum of s1 and s2 when they are considered as base-10 decimal numbers.

// Example #1:
// Input: s1 = "95", s2 = "7" 
// Output: "102" 
// Explanation: The sum of 95 and 7 is 102.

// Constraints:
// You may not use any built-in methods that trivialize the problem (e.g. BigInteger methods), and you may not convert the strings to integers.

#include<iostream>
#include<string>

using namespace std;

class Solution {
  public:
    string addStrings(string s1, string s2) {
        int i = s1.size() - 1, j = s2.size() - 1, carry = 0;
        string result;
        // Start from last index
        while (i >= 0 || j >= 0) {
            int sum = carry;
            // If i greater than or equal to 0 add integer value of string 1 at that i to sum
            if (i >= 0) {
                sum += (s1[i] - '0');
                i--;
            }
            // If j greater than or equal to 0 add integer value of string 2 at that j to sum
            if (j >= 0) {
                sum += (s2[j] - '0');
                j--;
            }
            // Add the unit index of sum to result
            result += to_string(sum % 10);
            // Carry is equal to sum/10
            carry = sum / 10;
        }
        
        // If carry is not zero add it to ans as the first char
        if (carry != 0) {
            result += to_string(carry);
        }
        // reverse string to get the ans
        reverse(result.begin(), result.end());
        return result;
    }
};

int main() {
    Solution a;
    string output = a.addStrings("1","2");
    cout<<output<<endl;
    getchar();
}

// Simulating Addition
// We can simulate the process typically used to carry out base-10 addition by hand. As per usual, we process our two numbers in reverse order. At each step, we compute the sum of the two decimal digits in the same column and the digitwise sum % 10 is added to the front of our answer. While performing these addition operations on the digits of our strings, we must maintain a "carry" variable representing whether or not our sum has exceeded nine at any given point. This carry variable is maintained and affects our subsequent sum digitwise sum computations. In the end, we have to reverse our string since we processed the two inputted strings in reverse order. Note how this process is identical to how one would carry out base-10 addition on paper.