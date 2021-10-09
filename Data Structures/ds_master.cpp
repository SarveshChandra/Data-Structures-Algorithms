#include<bits/stdc++.h>

using namespace std;



#include"mytemplate.h"

vector<int> ds = {5,6,2,3,7,1};
// array<int, 6> ds = {5,6,2,3,7,1};

void ulbounds() {
    cout<<endl;
    // upper lower bounds after sort
    sort(ds.begin(), ds.end());
    auto ub = upper_bound(ds.begin(), ds.end(), 6);
    cout<<"ub output"<<endl;
    for(auto it = ub;it!=ds.end();it++) {
        cout<<*it<<" ";
    }
    cout<<endl<<"lb output"<<endl;
    auto lb = lower_bound(ds.begin(), ds.end(), 6);
    for(auto it = lb;it!=ds.end();it++) {
        cout<<*it<<" ";
    }
    cout<<endl;
}


void insertvalues() {
    cout<<endl;
    // insert/pop
    ds.push_back(3000);
    cout<<"inserted push_back"<<endl;
    for(auto ele:ds) {
        cout<<ele<<" ";
    }
    cout<<endl;
    cout<<"pop_back"<<endl;
    ds.pop_back();
    for(auto ele:ds) {
        cout<<ele<<" ";
    }
    cout<<endl<<"inserted"<<endl;
    ds.insert(ds.begin()+1, 2, 100);
    for(auto ele:ds) {
        cout<<ele<<" ";
    }
    cout<<endl;
    cout<<"inserted again"<<endl;
    ds.insert(ds.end(), ds.begin(), ds.end());
    for(auto ele:ds) {
        // deb(ele);
        cout<<ele<<" ";
    }
    cout<<endl;
}


void swapds() {
    cout<<endl;
    vector<int> tmpv = {1,2,3,4,5};
    ds.swap(tmpv);
    cout<<"swapped"<<endl;
    cout<<"tmpv size "<<tmpv.size()<<endl;
    cout<<"tmpv capacity "<<tmpv.capacity()<<endl;
    cout<<"tmpv below"<<endl;
    for(int ele:tmpv) {
        cout<<ele<<" ";
    }
    cout<<endl;
    cout<<"ds size "<<ds.size()<<endl;
    cout<<"ds capacity "<<ds.capacity()<<endl;
    cout<<"ds below"<<endl;
    for(int ele:ds) {
        cout<<ele<<" ";
    }
    cout<<endl;
}


int main() {  
    // printer("starting ds", "of size", ds.size());
    // deb2(ds.size(), ds.capacity());
    ulbounds();
    insertvalues();
    swapds();
    // ds.rotate(ds.begin())
    
    getchar();
}