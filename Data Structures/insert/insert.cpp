#include<bits/stdc++.h>
#include "../mytemplate.h"

using namespace std;

int main() {
    vector<int> v = {5, 5};
    // for(int ele:v) {
    //     cout<<ele<<" ";
    // }
    loop(v);
    // cout<<endl;
    // v.insert(v.begin(), v.begin(), v.end());
    v.insert(v.begin()+1, 2, 100);
    printer("after v.insert()");
    loop(v);
    // for(int ele:v) {
    //     cout<<ele<<" ";
    // }
    // cout<<endl;
    getchar();
}