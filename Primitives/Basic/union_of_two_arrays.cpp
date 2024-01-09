//Function to return the count of number of elements in union of two arrays.
int doUnion(int a[], int n, int b[], int m)  {
    //code here
    int output = 0;
    set<int> outputset;
    
    for(int i=0; i<n; i++) {
        outputset.insert(a[i]);
    }
    
    for(int i=0; i<m; i++) {
        outputset.insert(b[i]);
    }
    
    return outputset.size();
}