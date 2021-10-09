#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> v = {1,2,3,4,5};
    cout<<"size "<<v.size()<<endl;
    cout<<"capacity "<<v.capacity()<<endl;
    auto it = v.rend();
    cout<<*it<<endl;
    // it--;
    // cout<<*it<<endl;
    // vector<int>::iterator it2 = v.begin();
    // cout<<*it2<<endl;
    cout<<v.back()<<endl;
    getchar();
}

// use begin() and rbegin() for valid pointers.