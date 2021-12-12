// Given an array of time strings times, return the smallest difference between any two times in minutes.

// Example:
// Input: ["00:03", "23:59", "12:03"]
// Output: 4
// Input: The closest 2 times are "00:03" and "23:59" (by wrap-around), and they differ by 4 minutes.

// Constraints:
// All strings will be non-empty and in the format HH:mm

#include<iostream>
#include <bitset>
#include<bits/stdc++.h>
#include<string>
#include"../mytemplate.h"

using namespace std;

class Solution {
  public:
    inline int time_to_int(const string & time) {
      // Converting the time in minutes
      return stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3, 2));
    }

  int timeDifference(vector < string > & timePoints) {
    // Creating a bitset and checking if the number has already occured
    // If the number has already occured return 0
    bitset<1440> seen;
    for (const auto & time: timePoints) {
      int value = time_to_int(time);
      if (seen[value]) {
        return 0;
      }
      seen[value] = true;
    }
    // In this step we calculate the minimum difference by subtracting it with the previous
    int prev = -1, first = -1, min_diff = (24 * 60) + 1;
    for (int i = 0; i < 1440; ++i) {
      if (seen[i]) {
        if (prev != -1) {
          min_diff = min(min_diff, i - prev);
        } else {
          first = i;
        }
        prev = i;
      }
    }
    /* Wrap-around check */
    min_diff = min(min_diff, first + 1440 - prev);
    return min_diff;
  }
};

int main() {
    vector<string> times = {"00:03", "23:59", "12:03"};
    Solution a;
    int output = a.timeDifference(times);
    cout<<output<<endl;
    getchar();
}

// Parsing times