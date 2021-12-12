#include<iostream>
#include<bits/stdc++.h>
#include"../mytemplate.h"

using namespace std;

int main() {

    vector<vector<int>> grid = {{1,2,3,4, 5,6}, {7,8,9,10,11,12},{13,14,15,16,17,18},{19,20,21,22,23,24}};

    // grid[0].push_back(1);
    // for(auto x:grid) {
    //     for(auto y:x) {
    //         cout<<y<<" ";
    //     }
    //     cout<<endl;
    // }
    // cout<<endl;
    // deb(v.size());
    // deb(v[0].size());

    int rows = grid.size();
    int columns = grid[0].size();
    cout<<rows<<" "<<columns<<endl;
    int layers = (rows < columns)? rows/2 : columns/2;
    vector<int> v;

    // for(auto x:v) {
    //     for(auto y:x) {
    //         cout<<y<<" ";
    //     }
    //     cout<<endl;
    // }

    // cout<<"layers "<<layers<<endl;
    // for(int l=0; l<layers;l++) {
    //     for(int i=l;i<columns-l; i++) {
    //         v.push_back(grid[l][i]);
    //     }
    //     for(int i=l+1;i<rows-l;i++) {
    //         v.push_back(grid[i][columns-l-1]);
    //     }
    //     for(int i=columns-l-2;i>=l;i--) {
    //         v.push_back(grid[rows-l-1][i]);
    //     }
    //     for(int i=rows-l-2;i>l;i--) {
    //         v.push_back(grid[i][l]);
    //     }
    // }

    // int k=2;

    // for(int i=0;i<k;i++) {
    //     v.push_back(v[i]);
    // }

    // for(auto x:v) {
    //     cout<<x<<" ";
    // }
    // cout<<endl;
    // int index = k;

    // for(int l=0; l<layers;l++) {
    //     for(int i=l;i<columns-l; i++) {
    //         grid[l][i] = v[index];
    //         ++index;
    //     }
    //     for(int i=l+1;i<rows-l;i++) {
    //         grid[i][columns-l-1] = v[index];
    //         ++index;
    //     }
    //     for(int i=columns-l-2;i>=l;i--) {
    //         grid[rows-l-1][i] = v[index];
    //         ++index;
    //     }
    //     for(int i=rows-l-2;i>l;i--) {
    //         grid[i][l] = v[index];
    //         ++index;
    //     }
    // }

    for(auto x:grid) {
        for(auto y:x) {
            cout<<y<<" ";
        }
        cout<<endl;
    }

    getchar();
    return 0;
}