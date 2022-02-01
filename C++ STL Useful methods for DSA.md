Include header file for STL,

#include<bits/stdc++.h>
vector<int> v(5,100); // 5 times 100
vector<int> ds = {5,6,2,3,7,1};
//size and capacity
ds.size() //6
ds.capacity() //6
iterators


ds.begin() //points to first element
ds.end() // points to address after last element (null)
ds.rbegin() //points to last element
ds.rend() //points to memory address before first element (null)


vector<int>::iterator it = v.begin();


sort
sort(ds.begin(), ds.end(), greater<int>()); //sort in descending order

int arr2[] = {4,6,2,3,1}; //normal array
loop(arr2);
sort(arr2, arr2 + 3); // [first, last)

sort(ds.begin(), ds.end()); //returns nothing
//now the vector is sorted. 1 2 3 5 6 7

pair<int, int> p[] = {{1,2}, {5,4}, {6,7}, {9,3}, {8,3}};
for(pair<int, int> ele:p) {
    cout<<ele.first<<" "<<ele.second<<", ";
}

sort(p, p + 5, comp);
loop2(p);
output: | 1,2 | 9,3 | 8,3 | 5,4 | 6,7 |
bool comp(pair<int, int> p1, pair<int, int> p2) {
    if(p1.second<p2.second) {return true;}
    else if(p1.second == p2.second) {
        if(p1.first > p2.first) {
            return true;
        }
    }
    return false;
}


upper and lower bounds
auto ub = upper_bound(ds.begin(), ds.end(), 3); //returns iterator to upper bound
auto lb = lower_bound(ds.begin(), ds.end(), 2); //returns iterator to lower bound
//loop from upper bound to vector end
for(auto it = ub;it!=ds.end();it++) {
        cout<<*it<<" ";
    }
output: 5 6 7
//loop from lower bound to vector end
for(auto it = lb;it!=ds.end();it++) {
        cout<<*it<<" ";
    }

output: 2 3 5 6 7


push_back to vector
ds.push_back(3000);
output: 1 2 3 5 6 7 3000
now size 7, capacity 12


pop back element
ds.pop_back();
output: 1 2 3 5 6 7
now size 6, capacity 12


insert()
//using insert method of number of copies
ds.insert(ds.begin()+1, 2, 100); //(position by iterator, number of elements,data)
//returns: iterator that points to the inserted data.

output: 1 100 100 2 3 5 6 7
//using insert method of range


ds.insert(ds.end(), ds.begin(), ds.end()); //(position, first, last)
output: 1 100 100 2 3 5 6 7 1 100 100 2 3 5 6 7
//loop ds elements modern way,
for(auto ele:ds) {   
    cout<<ele<<" ";
}


swap
vector<int> tmpv = {1,2,3,4,5};
ds.swap(tmpv);
tmpv.size() //16
tmpv.capacity() //16
ds.size() //5
ds.capacity() //5


erase()
remove a range of elements
ds.erase(v.begin(), v.end()); //all values
ds.erase(v.begin(), v.end()-1); //all values except last one


minmax_element()
auto m = minmax_element(v.begin(), v.end()); //Return a pair of iterators pointing to the minimum and maximum elements in a range.
deb(*m.first);
deb(*m.second);


arrays
array<int, 3> a = {1,2,3};
loop(a);
printer("starting array", "of size", a.size());
a.front() //1
a.back() //3




grid/matrix

vector<vector<int>> grid = {{1,2,3,4, 5,6}, {7,8,9,10,11,12},{13,14,15,16,17,18},{19,20,21,22,23,24}};
printer("input grid");
    for(auto x:grid) {
        for(auto y:x) {
            cout<<y<<" ";
        }
        cout<<endl;
  }
int rows = grid.size();
int columns = grid[0].size();
int layers = (rows < columns)? rows/2 : columns/2; //output 2