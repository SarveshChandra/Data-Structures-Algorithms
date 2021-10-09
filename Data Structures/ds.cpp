#include<bits/stdc++.h>
using namespace std;

void to_array() {
    array<int, 3> a = {1,2,3};
    cout<<"size "<<a.size()<<endl;
    cout<<a[1]<<endl;
    cout<<a.at(1)<<endl;
    cout<<a.front()<<endl;
    cout<<a.back()<<endl;
}

void to_vector() {
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
    // to_array();
    to_vector();

    getchar();
}