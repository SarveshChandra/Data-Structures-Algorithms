#include<bits/stdc++.h>
#include "mytemplate.h"
using namespace std;

int main() {
    vector<int>v = {1,3,4,7,8,9};
    loop(v);
    // cout<<*v.rbegin()<<endl;
    // auto maxi = max_element(v.begin(), v.end());
    // cout<<*maxi<<endl;
    auto m = minmax_element(v.begin(), v.end()); //Return a pair of iterators pointing to the minimum and maximum elements in a range.
    deb(*m.first);
    deb(*m.second);
    // cout<<*m.first<<endl;
    // cout<<*m.second<<endl;
    getchar();
}