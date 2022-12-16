#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <thread>
#include <unistd.h>
#include <algorithm>
using namespace std;

bool verify(int arr[], int length)
{
    cout << "there are " << length << " numbers in the array" << endl;
    return is_sorted(arr, arr + length);
}

int main(int argc, char* argv[])
{
    if (argc < 2)
	{
		cout << "Please include input filename and output filename in param list.\n";
		cout << "Example:\n";
		cout << "     % verifySort mySort.txt\n";
		exit(EXIT_SUCCESS);
	}
	ifstream fin;
    string line;
    int numbers_of_lines = 0;
    int n;

    fin.open(argv[1]);
    while(fin.peek() != EOF)
    {
        getline(fin,line);
        numbers_of_lines++;
    }
	fin.close();

	int v[numbers_of_lines];
	int count = 0;

    fin.open(argv[1]);
    while (fin >> n )
	{
		v[count++] = n;	// insert a number into the arary and increase the index
	}
        
    if (verify(v,count))
    {
        cout << "Sorted" << endl;
    }
    else
    {
        cout << "Not Sorted" << endl;
    }

    fin.close();
    return 0;
}