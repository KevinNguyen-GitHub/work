
#include <fstream> 
#include <vector>
#include <iostream> 
#include <thread> 
#include <cstring> 
using namespace std;

struct arguments
{
    int *arr;
};

void insertionSort(int* arr, int n)
{
    for (int i = 1; i < n; i++)
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

    arguments argList[8];
    for (int i = 0; i < 8; i++) {
      argList[i].arr = v + (i * THREAD_MAX);
    }
    
    // Create 8 threads to sort 8 different subsets of the array
    pthread_t thread0, thread1, thread2, thread3, thread4, thread5, thread6, thread7;
    int iret0, iret1, iret2, iret3, iret4, iret5, iret6, iret7;
    iret0 = pthread_create(&thread0, NULL, insertionSort, (void *)&argList[0]);
    iret1 = pthread_create(&thread1, NULL, insertionSort, (void *)&argList[1]);
    iret2 = pthread_create(&thread2, NULL, insertionSort, (void *)&argList[2]);
    iret3 = pthread_create(&thread3, NULL, insertionSort, (void *)&argList[3]);
    iret4 = pthread_create(&thread4, NULL, insertionSort, (void *)&argList[4]);
    iret5 = pthread_create(&thread5, NULL, insertionSort, (void *)&argList[5]);
    iret6 = pthread_create(&thread6, NULL, insertionSort, (void *)&argList[6]);
    iret7 = pthread_create(&thread7, NULL, insertionSort, (void *)&argList[7]);

    pthread_join(thread0, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    pthread_join(thread3, NULL);
    pthread_join(thread4, NULL);
    pthread_join(thread5, NULL);
    pthread_join(thread6, NULL);
    pthread_join(thread7, NULL);

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
    merge(v, indices[0], 250000); 
    merge(v, 250000, 500000); 
    merge(v, 500000, 750000); 
    merge(v, 250000, MAX);  
    merge(v, indices[0], MAX); 

    
    fout.open(argv[2], ios::out | ios::trunc);
    for (int i = 0; i < count - 1; i++)
        fout << v[i] <<endl;
    fout << v[count - 1] <<endl;
    fout.close();
    fin.close();
    return 0;
}