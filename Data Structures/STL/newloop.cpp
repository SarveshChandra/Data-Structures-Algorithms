#include<bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v(5,1);
    for(int &ele:v) {
        cout<<++ele<<" ";
    }
    cout<<endl;
    for(int ele:v) {
        cout<<ele<<" ";
    }

    getchar();
}