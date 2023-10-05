#include <iostream>
using namespace std;

int binarySearch(int arr[], int leftindex, int rightindex, int x)
{
	if (rightindex >= leftindex) {
		int mid = (leftindex + rightindex) / 2;
		if (arr[mid] == x)
			return mid;
		if (arr[mid] > x)
			return binarySearch(arr, leftindex, mid - 1, x);
        return binarySearch(arr, mid + 1, rightindex, x);
	}
	return -1;
}

int main(void)
{
    int a,i,x;
    cin>>a;
    int arr[a];
    for(i=0; i<a; i++){
        cin>>arr[i];
    }
    cin>>x;
	int result = binarySearch(arr, 0, a, x);
	result == -1 ? cout << "Element is not present in array" : cout << "Element is present at index " << result;
	return 0;
}


