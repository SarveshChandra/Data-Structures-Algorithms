#include<iostream>

using namespace std;

/*
Approcah
If input is power of 2 than it will have only 1 set bit
(input-1) will have all other set bits except the original .
For eg 8- 1000 and 7- 0111
So their bitwise & results to 0
*/

class Solution {
  public:
    bool powerOfTwo(int input) {
      return (input && (input & (input - 1)) == 0);
    }
};

int main() {
    Solution a;
    bool output = a.powerOfTwo(110);
    cout<<output<<endl;
    getchar();
}