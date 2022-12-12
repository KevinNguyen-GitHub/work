#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <thread>
#include <unistd.h>
using namespace std;
  
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

template<typename T, typename InputIt1, typename InputIt2, typename OutputIt>
void merge(InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, OutputIt d_first)
{
    while (first1 != last1 && first2 != last2)
    {
        if (*first2 < *first1)
        {
            *d_first++ = *first2++;
        }
        else
        {
            *d_first++ = *first1++;
        }
    }

    while (first1 != last1)
    {
        *d_first++ = *first1++;
    }

    while (first2 != last2)
    {
        *d_first++ = *first2++;
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

    
    array<int, THREAD_MAX> a1{}, a2{}, a3{}, a4{}, a5{}, a6{}, a7{}, a8{};
    copy(v.begin(), min(v.begin() + THREAD_MAX, v.end()), a1.begin());
    copy(v.begin() + THREAD_MAX, min(v.begin() + 2 * THREAD_MAX, v.end()), a2.begin());
    copy(v.begin() + 2 * THREAD_MAX, min(v.begin() + 3 * THREAD_MAX, v.end()), a3.begin());
    copy(v.begin() + 3 * THREAD_MAX, min(v.begin() + 4 * THREAD_MAX, v.end()), a4.begin());
    copy(v.begin() + 4 * THREAD_MAX, min(v.begin() + 5 * THREAD_MAX, v.end()), a5.begin());
    copy(v.begin() + 5 * THREAD_MAX, min(v.begin() + 6 * THREAD_MAX, v.end()), a6.begin());
    copy(v.begin() + 6 * THREAD_MAX, min(v.begin() + 7 * THREAD_MAX, v.end()), a7.begin());
    copy(v.begin() + 7 * THREAD_MAX, min(v.begin() + 8 * THREAD_MAX, v.end()), a8.begin());

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

    array<int, MAX> sortedArray;
    merge<int>(a1.begin(), a1.end(), a2.begin(), a2.end(), sortedArray.begin());
    merge<int>(sortedArray.begin(), sortedArray.end(), a3.begin(), a3.end(), sortedArray.begin());
    merge<int>(sortedArray.begin(), sortedArray.end(), a4.begin(), a4.end(), sortedArray.begin());
    merge<int>(sortedArray.begin(), sortedArray.end(), a5.begin(), a5.end(), sortedArray.begin());
    merge<int>(sortedArray.begin(), sortedArray.end(), a6.begin(), a6.end(), sortedArray.begin());
    merge<int>(sortedArray.begin(), sortedArray.end(), a7.begin(), a7.end(), sortedArray.begin());
    merge<int>(sortedArray.begin(), sortedArray.end(), a8.begin(), a8.end(), sortedArray.begin());

    fout.open(argv[2], ios::out | ios::trunc);
    for (int i = 0; i < MAX; i++)
    fout << sortedArray[i] <<endl;

    fout.close();
    fin.close();
    return 0;
}
