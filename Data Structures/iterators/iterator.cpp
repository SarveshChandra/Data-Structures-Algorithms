#include <bits/stdc++.h>
#include "../mytemplate.h"

using namespace std;

int main() {
    vector<int> v = {1,2,3,4,5};
    loop(v);
    deb2(v.size(), v.capacity());
    // cout<<"size "<<v.size()<<endl;
    // cout<<"capacity "<<v.capacity()<<endl;
    printer("add index to begin/rebegin methods", ",decrement index from end/rend methods");
    printer("for end/rend methods, they start from -1");
    deb(*v.begin());
    deb(*(v.end()-1));
    deb(*v.rbegin());
    deb(*(v.rbegin()+1));
    deb(*(v.rend()-1));
    deb(*(v.rend()-2));
    deb(*(v.rbegin()-1));
    deb(*v.rend());
    deb(*(v.rend()+1));
    // auto it = v.rend();
    // cout<<*it<<endl;
    // auto it = v.end();
    // cout<<*it<<endl;
    // it--;
    // cout<<*it<<endl;
    // vector<int>::iterator it2 = v.begin();
    // cout<<*it2<<endl;
    deb(v.back());
    getchar();
}

// use begin() and rbegin() for valid pointers.