#include<bits/stdc++.h>

using namespace std;

void misc() {
    vector<int> v = {4,6,2,3,7};
    // sort(v.begin(), v.end());
    sort(v.begin(), v.end(), greater<int>());
    for(int ele:v) {
        cout<<ele<<" ";
    }
    cout<<endl;
    
    array<int, 5> arr = {4,6,2,3,7};
    sort(arr.begin(), arr.end());
    for(int ele:arr) {
        cout<<ele<<" ";
    }
    cout<<endl;

    //normal array
    int arr2[] = {4,6,2,3,1};
    sort(arr2, arr2 + 5); // [first, last]
    sort(arr2, arr2 + 4); // [first, last)
    for(int ele:arr2) {
        cout<<ele<<" ";
    }
    cout<<endl;
}

// sort according to second element.
// if second element is same, then sort according to first element but in descending order.
bool comp(pair<int, int> p1, pair<int, int> p2) {
    if(p1.second<p2.second) {return true;}
    else if(p1.second == p2.second) {
        if(p1.first > p2.first) {
            return true;
        }
    }
    return false;
}


void custom_sort() {
    pair<int, int> p[] = {{1,2}, {5,4}, {6,7}, {9,3}, {8,3}};
    for(pair<int, int> ele:p) {
        cout<<ele.first<<" "<<ele.second<<", ";
    }
    cout<<endl;
    sort(p, p + 5, comp);
    for(pair<int, int> ele:p) {
        cout<<ele.first<<" "<<ele.second<<", ";
    }
}

int main() {
    // misc();
    custom_sort();

    getchar();
}