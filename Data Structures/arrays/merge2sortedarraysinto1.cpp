int * mergeArrays(int arr1[], int arr2[], int arr1Size,int arr2Size)
{
    int * arr3 = new int[(arr1Size + arr2Size)]; // creating new array
    // Write your code here
    int counter = 0;
    for(int index = 0, i = 0, j = 0; index < (arr1Size + arr2Size); index++) {
        if(i<arr1Size && j<arr2Size) {
            if(arr1[i]<=arr2[j]) {
                arr3[index] = arr1[i];
                i += 1;
            }
            else {
                arr3[index] = arr2[j];
                j += 1;
            }
        }
        else {
            if(i==arr1Size) {
                arr3[index] = arr2[j];
                j += 1;
            }
            else {
                arr3[index] = arr1[i];
                i += 1;
            }
        }
    }
    return arr3; // returning array
}