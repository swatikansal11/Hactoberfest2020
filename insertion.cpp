#include <bits/stdc++.h> 
using namespace std;
void insertionSort(int arr[],int n){
    int i,key,j;
    for(i=1;i<n;i++)
    {
        key=arr[i];
        j=i-1;
        while(j>=0 && arr[j]>key)
        {
            arr[j+1]=arr[j];
            j=j-1;
        }
        arr[j+1]=key;
    }
}
void printArray(int arr[],int n)
{
    cout<<"Sorted Array \n";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
        cout<<endl;
    }
}

int main(){
    int n, arr[10],k;
    cout<<"Enter the length of the array"<<endl;
    cin>>n;
    cout<<"Enter the array"<<endl;
    for(k=0;k<n;k++)
    {
        cin>>arr[k];
    }
    insertionSort(arr,n);
    printArray(arr,n);
    return 0;

}