#include <fstream> 
#include <vector>
#include <iostream> 
#include <thread> 
#include <cstring> 
using namespace std;

void insertionSort(int* arr, int size)
{
    for (int i = 1; i < size; i++)
    {
        int key = arr[i];
        int j = i - 1;

        // Shift elements that are greater than key to the right
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        // Insert the key in its correct position
        arr[j + 1] = key;
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
    
    int v[MAX];
    int count = 0;
    
    fin.open(argv[1]);
    while (fin >> n)
    {
        v[count++] = n; // insert a number into the array and increase the index
    }

    int v0[THREAD_MAX], v1[THREAD_MAX], v2[THREAD_MAX], v3[THREAD_MAX], v4[THREAD_MAX], v5[THREAD_MAX], v6[THREAD_MAX], v7[THREAD_MAX];

    // copy elements from v into the corresponding array
    memcpy(v0, v + (0 * THREAD_MAX), THREAD_MAX * sizeof(int));
    memcpy(v1, v + (1 * THREAD_MAX), THREAD_MAX * sizeof(int));
    memcpy(v2, v + (2 * THREAD_MAX), THREAD_MAX * sizeof(int));
    memcpy(v3, v + (3 * THREAD_MAX), THREAD_MAX * sizeof(int));
    memcpy(v4, v + (4 * THREAD_MAX), THREAD_MAX * sizeof(int));
    memcpy(v5, v + (5 * THREAD_MAX), THREAD_MAX * sizeof(int));
    memcpy(v6, v + (6 * THREAD_MAX), THREAD_MAX * sizeof(int));
    memcpy(v7, v + (7 * THREAD_MAX), THREAD_MAX * sizeof(int));

    // Create 8 threads to sort 8 different subsets of the array
    thread thread0, thread1, thread2, thread3, thread4, thread5, thread6, thread7;

    thread0 = thread(insertionSort, v0, THREAD_MAX);
    thread1 = thread(insertionSort, v1, THREAD_MAX);
    thread2 = thread(insertionSort, v2, THREAD_MAX);
    thread3 = thread(insertionSort, v3, THREAD_MAX);
    thread4 = thread(insertionSort, v4, THREAD_MAX);
    thread5 = thread(insertionSort, v5, THREAD_MAX);
    thread6 = thread(insertionSort, v6, THREAD_MAX);
    thread7 = thread(insertionSort, v7, THREAD_MAX);

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
    merge(v, 0, THREAD_MAX);
    merge(v, THREAD_MAX, 2 * THREAD_MAX);
    merge(v, 2 * THREAD_MAX, 3 * THREAD_MAX);
    merge(v, 3 * THREAD_MAX, 4 * THREAD_MAX);
    merge(v, 4 * THREAD_MAX, 5 * THREAD_MAX);
    merge(v, 5 * THREAD_MAX, 6 * THREAD_MAX);
    merge(v, 6 * THREAD_MAX, 7 * THREAD_MAX);
    merge(v, 7 * THREAD_MAX, 8 * THREAD_MAX);

    // Merge the final 8 sorted arrays into a single sorted array
    merge(v, 0, 2 * THREAD_MAX);
    merge(v, 2 * THREAD_MAX, 4 * THREAD_MAX);
    merge(v, 4 * THREAD_MAX, 6 * THREAD_MAX);
    merge(v, 6 * THREAD_MAX, 8 * THREAD_MAX);


    
    fout.open(argv[2], ios::out | ios::trunc);
    for (int i = 0; i < count - 1; i++)
        fout << v[i] <<endl;
    fout << v[count - 1] <<endl;
    fout.close();
    fin.close();
    return 0;
}