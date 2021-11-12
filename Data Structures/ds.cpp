
#include<bits/stdc++.h>
#include "mytemplate.h"
using namespace std;

void to_array() {
    cout<<endl;
    array<int, 3> a = {1,2,3};
    loop(a);
    printer("starting array", "of size", a.size());
    // deb(a.size());
    // cout<<"size "<<a.size()<<endl;
    deb(a[1]);
    // cout<<a[1]<<endl;
    deb(a.at(1));
    // cout<<a.at(1)<<endl;
    deb(a.front());
    // cout<<a.front()<<endl;
    deb(a.back());
    // cout<<a.back()<<endl;
}

void to_vector() {
    cout<<endl;
    vector<int> v(5,100);
    for(int ele:v) {
        cout<<ele<<" ";
    }
    cout<<endl;
    cout<<"size "<<v.size()<<endl;
    cout<<"capacity "<<v.capacity()<<endl;
    v.push_back(101);
    cout<<"size "<<v.size()<<endl;
    cout<<"capacity "<<v.capacity()<<endl;
    // v.insert(v.begin(), 300);
    // v.insert(v.begin(), v.begin(), v.end());
    v.insert(v.begin()+1, 2, 5);
    // cout<<v[0]<<endl;
    for(int ele:v) {
        cout<<ele<<" ";
    }
    cout<<endl;
    cout<<"size "<<v.size()<<endl;
    cout<<"capacity "<<v.capacity()<<endl;
    v.erase(v.begin(), v.end()-1);
    for(int ele:v) {
        cout<<ele<<" ";
    }
    cout<<endl;
    cout<<"size "<<v.size()<<endl;
    cout<<"capacity "<<v.capacity()<<endl;
}

int main() {
    to_array();
    to_vector();

    getchar();
}