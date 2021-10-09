#include<bits/stdc++.h>
using namespace std;

int main() {
    vector<int>v = {1,3,4,7,8,9};
    // cout<<*v.rbegin()<<endl;
    // auto maxi = max_element(v.begin(), v.end());
    // cout<<*maxi<<endl;
    auto m = minmax_element(v.begin(), v.end());
    cout<<*m.first<<endl;
    cout<<*m.second<<endl;
    getchar();
}