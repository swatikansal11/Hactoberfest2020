#include <bits/stdc++.h>
using namespace std;
void swap(int *xp,int*yp){
    int temp=*xp;
    *xp=*yp;
    *yp=temp;
}

void bubbleSort(int arr[],int n){
   int i,j;
   for(i=0;i<n-1;i++){
       for(j=0;j<n-i-1;j++){
           if(arr[j]>arr[j+1]){
               swap(&arr[j],&arr[j+1]);
           }
       }
   }

}
void printArray(int arr[],int n){
    cout<<"Sorted Array"<<endl;
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
        cout<<endl;
    }
}

int main(){
    int k,n,arr[30];
    cout<<"Enter the length of the array"<<endl;
    cin>>n;
    cout<<"Enter the array"<<endl;
    for(k=0;k<n;k++)
    {
      cin>>arr[k];

    }
 bubbleSort(arr,n);
 printArray(arr,n);
 return 0;
}