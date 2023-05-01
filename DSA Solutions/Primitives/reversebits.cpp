#include <math.h>
#include<iostream>

using namespace std;

class Solution {
  public:
    int reverseBits(int input) {
      /*
       * Approach:
       *   1. Check the last bit of input
       *   2. Shift output left
       *   3. If it is 1, add it to output (do nothing otherwise)
       *   4. Shift input right
       *
       * Stop when input is 0
       */
      
      int output = 0;
  
      while (input != 0) {
        output = output << 1;
  
        if ((input & 1) == 1) {
          output |= 1;
        }
  
        input = input >> 1;
      }
  
      return output;
    };
};

int main() {
    Solution a;
    int output = a.reverseBits(110);
    cout<<output<<endl;
    getchar();
}