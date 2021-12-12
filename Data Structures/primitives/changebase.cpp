// Changing Base
// Given an integer (represented as a string) under base b1, convert it to base b2.

// Example 1:
// Input: ("12", 10, 2)
// Output: "1100"
// Explanation: We are converting "12" which is under base 10 (decimal) to base 2 (binary)

// Example 2:
// Input: ("123", 4, 10)
// Output: "27"
// Explanation: We are converting "123" which is under base 4 (quaternary) to base 10

// Example 3:
// Input: ("123", 4, 16)
// Output: "1B"
// Explanation: Convert "123" from base 4 to 16

// Example 4:
// Input: ("123", 10, 10)
// Output: "123"

// Constraints:
// 2 <= b1 <= 36
// 2 <= b2 <= 36
// For base-2 up to base-10 use the digits 0-9 to represent digits
// Use the English alphabet characters A-Z in base-11 and higher

#include <ctype.h>
#include <math.h>
#include<iostream>
#include<string>

using namespace std;

class Solution {
  private:
    string base10ToNewBase(int numberUnderBase10, int base) {
      if (numberUnderBase10 == 0) {
        return "";
      }

      // lsd => "least significant digit"
      char lsdAsChar;
      int lsdUnderFinalBase = numberUnderBase10 % base;
      bool needsHexConversion = lsdUnderFinalBase >= 10;
      
      if (needsHexConversion) {
        /*
        * Convert digit into a letter (theoretically 'A'-'Z') because we can't express
        * values 10 and above as single digit values.
        * 
        * If we go past base 36 this will break.
        */
        lsdAsChar = (char) ('A' + lsdUnderFinalBase - 10);
      } else {
        // 'lsdUnderFinalBase' can be expressed as a single digit
        lsdAsChar = (char) ('0' + lsdUnderFinalBase);
      }
  
      int base10NumberWithoutLsd = numberUnderBase10 / base;
      string everythingElseToOurLeft = base10ToNewBase(base10NumberWithoutLsd, base);
  
      return everythingElseToOurLeft + lsdAsChar;
    };
  
  public:
    string changeBase(string numAsString, int b1, int b2) {
      bool isNegative = numAsString.at(0) == '-';
  
      /*
      * start: If the number has a minus sign "-", then we start decomposing
      * 'numAsString' from index 1 instead of from index 0.
      * 
      * maxPower: The power applied to the base that the most significant digit will
      * be multiplied by. Ex: "324" -> maxPower will be 2 since "324" = (3 x 10^2) +
      * (2 x 10^1) + (4 x 10^0) ^ maxPower
      * 
      * numberUnderBase10: The number we are slowly going to build
      */
      int start = isNegative ? 1 : 0;
      int maxPower = numAsString.length() - 1;
      int numberUnderBase10 = 0;
  
      /*
      * Loop over every digit & add it to the base 10 integer representation we are
      * building. We will later take this base 10 integer and convert it into b2.
      */
      for (int i = start; i < numAsString.length(); i++) {
        /*
        * Get the integer value that this place "contributes", or in other words, the
        * value that will be multiplied by (base)^(digit's position).
        */
        bool isPlaceADigit = isdigit(numAsString.at(i));
        int valueContributedByPlace =
          isPlaceADigit ? numAsString.at(i) - '0' : numAsString.at(i) - 'A' + 10;
  
        /*
        * So if we have "895", it means:
        * 
        * (8 x 10^2) + (9 x 10^1) + (5 x 10^0) (800) + (90) + (5) 895
        * 
        * If we have "1AB" (under base 16, hex), it means:
        * 
        * A => 10 B => 11 (1 x 16^2) + (10 x 16^1) + (11 x 16^0) (256) + (160) + (11)
        * 427
        */
        int positionPowerWeight = maxPower - i;
        numberUnderBase10 += (int) valueContributedByPlace * pow(b1, positionPowerWeight);
      }
  
      if (numberUnderBase10 == 0) {
        return "0";
      } else {
        return (isNegative ? "-" : "") + base10ToNewBase(numberUnderBase10, b2);
      }
    };

};

int main() {
    Solution a;
    string output = a.changeBase("12", 10, 2);
    cout<<output<<endl;
    getchar();
}

// Recursive conversion