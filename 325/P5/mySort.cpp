#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <thread>
#include <unistd.h>
using namespace std;

struct arguments
{
    int *arr;
};

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high]; 
    int i = (low-1); 
  
    for (int j = low; j <= high-1; j++) {
        if (arr[j] <= pivot) {
            i++; 
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[high]);
    return (i+1);
}

void quickSort(int arr[], int low, int high)
{
    if (low < high) {
        int p = partition(arr, low, high);
        quickSort(arr, low, p-1);
        quickSort(arr, p+1, high);
    }
}

void merge(int arr[], int left, int right) {
    int mid = (left+right)/2; // middle
    int size = right - left;
    int *temp = new int[size]; // dynamic array

    /* Merge the temp arrays back into arr[left..right] */
    int i = left; 
    int j = mid; 
    int k = 0; 
    while (i < mid && j < right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
    }

    // Copy the remaining elements if one of the subarrays is empty
    while (i < mid) temp[k++] = arr[i++];
    while (j < right) temp[k++] = arr[j++];

    // Copy the sorted temp array into the original array
    for (int i = 0; i < size; i++) {
        arr[left+i] = temp[i];
    }

    delete[] temp; // Use array delete to avoid memory leak
}

int main(int argc, char* argv[])
{
    if (argc < 3)
	{
		cout << "Please include input filename and output filename in param list.\n";
		cout << "Example:\n";
		cout << "     % mySort numbers.txt mySorted.txt\n";
		exit(EXIT_SUCCESS);
	}
    
    const int MAX = 1000000;
    const int THREAD_MAX = 125000;
  	ofstream fout;
	ifstream fin;
	int n;
	
	array<int, MAX> v;
	int count = 0;


    fin.open(argv[1]);
    while (fin >> n )
	{
		v[count++] = n;	// insert a number into the arary and increase the index
	}

    
    arguments argList[8];
    for (int i = 0; i < 8; i++) {
      argList[i].arr = v + (i * THREAD_MAX);
    }

    thread thread0(quickSort,argList[0],0,THREAD_MAX);
    thread thread1(quickSort,argList[1],0,THREAD_MAX);
    thread thread2(quickSort,argList[2],0,THREAD_MAX);
    thread thread3(quickSort,argList[3],0,THREAD_MAX);
    thread thread4(quickSort,argList[4],0,THREAD_MAX);
    thread thread5(quickSort,argList[5],0,THREAD_MAX);
    thread thread6(quickSort,argList[6],0,THREAD_MAX);
    thread thread7(quickSort,argList[7],0,THREAD_MAX);

    // Start all threads
    thread0.join();
    thread1.join();
    thread2.join();
    thread3.join();
    thread4.join();
    thread5.join();
    thread6.join();
    thread7.join();

    // merging
    int indices[8];
    for( int i = 0; i < 8; i++){
      indices[i] = (i*THREAD_MAX);
    }
    int first = 0;
    int second;
    while (first <= 6) {
      second = first + 1;
      merge(v, indices[first], indices[second]); // ( arr l r )
      first = second + 1;
    }

    // merge
    merge(v, indices[0], 250000); //4
    merge(v, 250000, 500000); //4
    merge(v, 500000, 750000); //2
    merge(v, 250000, MAX);  //2
    merge(v, indices[0], MAX); 

    
    fout.open(argv[2], ios::out | ios::trunc);
    for (int i = 0; i < count - 1; i++)
        fout << v[i] <<endl;
    fout << v[count - 1] <<endl;
    fout.close();
    fin.close();
    return 0;
}
