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
    const int THREAD_MAAX = 125000;
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

    thread thread0(&quickSort,a1.data(),0,THREAD_MAX -1);
    thread thread1(&quickSort,a2.data(),THREAD_MAX,THREAD_MAX*2 -1);
    thread thread2(&quickSort,a3.data(),THREAD_MAX*2,THREAD_MAX*3 -1);
    thread thread3(&quickSort,a4.data(),THREAD_MAX*3,THREAD_MAX*4 -1);
    thread thread4(&quickSort,a5.data(),THREAD_MAX*4,THREAD_MAX*5 -1);
    thread thread5(&quickSort,a6.data(),THREAD_MAX*5,THREAD_MAX*6 -1);
    thread thread6(&quickSort,a7.data(),THREAD_MAX*6,THREAD_MAX*7 -1);
    thread thread7(&quickSort,a8.data(),THREAD_MAX*7,MAX -1);

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
