// Samuel Lee
// Class (CECS 325-02)
// Project Name ( Prog 4 SortRace Thread
// Due Date 10/20/22
//
// I certify that this program is my own original work. I did not copy any part
// of this program from any other source. I further certify that I typed each
// and every line of code in this program.

#include <fstream> // this is file stream
#include <vector>
#include <iostream> //input output stream
#include <pthread.h> // from the library using a -lpthread for linker
#include <cstring> // includes a 
using namespace std;

struct arguments {
  int *arr;
};

void *insertionSort(void *ptr) {
  arguments *arg = (arguments *)ptr;
  arg->arr; // this is arr[]
  cout << "start" << endl;
  for (int j = 1; j < 125000; j++) {
    int key = arg->arr[j];
    int i = j - 1;
    while (i >= 0 && arg->arr[i] > key) {
      arg->arr[i + 1] = arg->arr[i];
      i = i - 1;
    }
    arg->arr[i + 1] = key;
  }
  cout << "ending" << endl;
  return NULL;
}

void merge(int arr[], int left, int right) // left is the beginning of the array right is the end of the array
{
    int i, j, k;
    //fix middle
    int mid = (left+right)/2; // middle
    int size = right - left;
    int *temp = new int[size]; //dynamic means they'll be moving around
 
    /* Merge the temp arrays back into arr[l..r]*/
    i = left; 
    j = mid; 
    k = 0; 
    while (i < mid && j < right) {
        if (arr[i] <= arr[j]) {
            temp[k] = arr[i];
            i++;
        }
        else {
            temp[k] = arr[j];
            j++;
        }
        k++;
    }
 
    //Copy the remaining if one is empty
    while (i < mid) {
        temp[k] = arr[i];
        i++;
        k++;
    }
    while (j < right) {
        temp[k] = arr[j];
        j++;
        k++;
    }
    //assumption is we have a fully sorted temporary array, now how do we return that 
    //copy temp into orignal array
    /*function from ctring */
    memcpy( arr+left, temp, sizeof(int)*size ); //need to know how big my data type -- sizeof(4*size) gets # of bytes
    delete temp;
    

}

  int main(int argc, char *argv[]) {
    if (argc < 3) {
      cout << "Please include input filename and output filename in param "
              "list.\n";
      cout << "Example:\n";
      cout << "     % mySortA numbers.txt mySorted.txt\n";
      exit(EXIT_SUCCESS);
    }

    const int MAX = 1000000;
    ofstream fout;
    ifstream fin;
    int n;

    int nums[MAX];
    int ind = 0;  //size?

    fin.open(argv[1]);
    while (fin >> n) {
      nums[ind++] = n;
    }

    int bounds = 125000; // 125000-1
    arguments argList[8];
    for (int i = 0; i < 8; i++) {
      argList[i].arr = nums + (i * bounds);
    }

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
      indices[i] = (i*bounds);
      cout << indices[i] <<endl; }

    int first = 0;
    int second;
    while (first <= 6) {
      second = first + 1;
      merge(nums, indices[first], indices[second]); // ( arr l r )
      first = second + 1;
    }


    //subsiary merges
    merge( nums, indices[0], 250000); //4
    merge( nums, 250000, 500000); //4
    merge( nums, 500000, 750000); //2
    merge( nums, 250000, MAX);  //2
    //final merge last big 1
    merge( nums, indices[0], MAX); 


    //file out
    fout.open(argv[2], ios::out | ios::trunc);
    for (int i = 0; i < ind - 1; i++)
      fout << nums[i] << endl;
    fout << nums[ind - 1] <<endl;// to get no 1mil1
    fout.close();
    fin.close();
    return 0;
  }
