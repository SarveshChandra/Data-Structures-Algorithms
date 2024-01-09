int * removeEven( int *& Arr, int size ) {
  // Write your code here
  int i=0;
  int *temparr = new int[size];
  int counter = 0;
  while(i<size) {
    if(Arr[i]%2 != 0) {
      temparr[counter] = Arr[i];
      counter += 1;
    }
    i += 1;
  }
  delete[] Arr;
  Arr = temparr;
  return Arr;
}