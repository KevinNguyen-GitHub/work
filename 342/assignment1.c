#include <stdio.h>
#include <stdlib.h>

// function to swap elements
void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

// function to find the partition position
int partition(int *a, int low, int high) {
  // select the rightmost element as pivot
  int pivot = a[high];

  // pointer for greater element
  int i = low - 1;

  // traverse each element of the array
  // compare them with the pivot
  for (int j = low; j < high; j++) {
    if (a[j] <= pivot) {
      // if element smaller than pivot is found
      // swap it with the greater element pointed by i
      i++;

      // swap element at i with element at j
      if (i != j) {
        swap(&a[i], &a[j]);
      }
    }
  }

  // swap the pivot element with the greater element at i
  swap(&a[i + 1], &a[high]);

  // return the partition point
  return (i + 1);
}

// function to perform quicksort
void quick_sort(int *a, int n) {
  if (n < 2) {
    // base case: array with 0 or 1 element is already sorted
    return;
  }

  // select the first element as pivot
  int pivot = a[0];

  // partition the array around pivot
  int i = partition(a, 0, n - 1);

  // recursively sort the left and right subarrays
  quick_sort(a, i);
  quick_sort(a + i + 1, n - i - 1);
}

void merge(int a[], int l, int m, int r) {
  int i, j, k;
  int n1 = m - l + 1;
  int n2 = r - m;

  /* create temp arrays */
  int *L = malloc(n1 * sizeof(int)); // allocate memory for left subarray
  int *R = malloc(n2 * sizeof(int)); // allocate memory for right subarray

  /* Copy data to temp arrays L[] and R[] */
  for (i = 0; i < n1; i++)
    L[i] = a[l + i];
  for (j = 0; j < n2; j++)
    R[j] = a[m + 1 + j];

  /* Merge the temp arrays back into a[l..r]*/
  i = 0; // Initial index of first subarray
  j = 0; // Initial index of second subarray
  k = l; // Initial index of merged subarray
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      a[k] = L[i];
      i++;
    } else {
      a[k] = R[j];
      j++;
    }
    k++;
  }

  /* Copy the remaining elements of L[], if there
  are any */
  while (i < n1) {
    a[k] = L[i];
    i++;
    k++;
  }

  /* Copy the remaining elements of R[], if there
  are any */
  while (j < n2) {
    a[k] = R[j];
    j++;
    k++;
  }

  /* Free the memory allocated for temporary arrays */
  free(L);
  free(R);
}

void merge_sort(int *a, int n) {
  if (n > 1) {
    int m = n / 2;
    merge_sort(a, m);          // sort left subarray
    merge_sort(a + m, n - m);  // sort right subarray
    merge(a, 0, m - 1, n - 1); // merge sorted subarrays
  }
}

// function to check if an array is sorted
int is_sorted(int *a, int n) {
  for (int i = 0; i < n - 1; i++) {
    if (a[i] > a[i + 1]) {
      return 0;
    }
  }
  return 1;
}

// function to print array elements
void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    printf("%d  ", array[i]);
  }
  printf("\n");
}

int main() {
  // seed the random number generator
  srand(time(NULL));

  // test with an empty array
  int n = 0;
  int *a = malloc(sizeof(int) * n); // dynamically allocate memory for array
  merge_sort(a, n);
  quick_sort(a, n);
  printf("Empty array: %d\n", is_sorted(a, n));

  // test with an array of size 1
  n = 1;
  a[0] = rand() % 100;
  merge_sort(a, n);
  quick_sort(a, n);
  printf("Array of size 1: %d\n", is_sorted(a, n));

  // test with a sorted array
  n = 10;
  for (int i = 0; i < n; i++) {
    a[i] = i;
  }
  merge_sort(a, n);
  quick_sort(a, n);
  printf("Sorted array: %d\n", is_sorted(a, n));

  // test with a reverse-sorted array
  n = 10;
  for (int i = 0; i < n; i++) {
    a[i] = n - i - 1;
  }
  merge_sort(a, n);
  quick_sort(a, n);
  printf("Reverse-sorted array: %d\n", is_sorted(a, n));

  // test with an array of random integers
  n = 1000;
  for (int i = 0; i < n; i++) {
    a[i] = rand() % 10000;
  }
  merge_sort(a, n);
  quick_sort(a, n);
  printf("Random array: %d\n", is_sorted(a, n));

  return 0;
}