#include "MemoryManager.h"
#include <stdlib.h>
#include <iomanip>
#include <iostream>
using namespace std;

namespace MemoryManager
{
	// IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT 
	//
	// This is the only static memory that you may use, no other global variables may be
	// created, if you need to save data make it fit in MM_pool
	//
	// IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT


	const int MM_POOL_SIZE = 65536;
	char MM_pool[MM_POOL_SIZE];

	// I have provided this tool for your use
	void memView(int start, int end)
	{

		const unsigned int SHIFT = 8;
		const unsigned int MASK = 1 << SHIFT - 1;

		unsigned int value;	// used to facilitate bit shifting and masking

		cout << endl; // start on a new line
		cout << "               Pool                     Unsignd  Unsigned " << endl;
		cout << "Mem Add        indx   bits   chr ASCII#  short      int    " << endl;
		cout << "-------------- ---- -------- --- ------ ------- ------------" << endl;

		for (int i = start; i <= end; i++)
		{
			cout << (long*)(MM_pool + i) << ':';	// the actual address in hexadecimal
			cout << '[' << setw(2) << i << ']';				// the index into MM_pool

			value = MM_pool[i];
			cout << " ";
			for (int j = 1; j <= SHIFT; j++)		// the bit sequence for this byte (8 bits)
			{
				cout << ((value & MASK) ? '1' : '0');
				value <<= 1;
			}
			cout << " ";

            if (MM_pool[i] < 32)   // non-printable character so print a blank
            	cout << '|' << ' ' << "| (";	
            else                    // characger is printable so print it
				cout << '|' << *(char*)(MM_pool + i) << "| (";		// the ASCII character of the 8 bits (1 byte)

			cout << setw(4) << ((int)(*((unsigned char*)(MM_pool + i)))) << ")";	// the ASCII number of the character

			cout << " (" << setw(5) << (*(unsigned short*)(MM_pool + i)) << ")";	// the unsigned short value of 16 bits (2 bytes)
			cout << " (" << setw(10) << (*(unsigned int*)(MM_pool + i)) << ")";	// the unsigned int value of 32 bits (4 bytes)

																				//  cout << (*(unsigned int*)(MM_pool+i)) << "|";	// the unsigned int value of 32 bits (4 bytes)

			cout << endl;
		}
	}

	// Initialize set up any data needed to manage the memory pool
	void initializeMemoryManager(void)
	{

		int freeHead = 0; // starting index of the freelist
		int inUseHead = 2; // starting index of the inUselist
		int usedHead = 4; // starting index for the used list - deallocated memory

		int nextLink = 2; // offset index of the next link
		int prevLink = 4; // offset index for the prev link

		*(unsigned short*)(MM_pool + freeHead) = 6; // freelist starts at byte 6
		*(unsigned short*)(MM_pool + inUseHead) = 0;	// nothing in the inUse list yet
		*(unsigned short*)(MM_pool + usedHead) = 0; // nothing in the used list yet

	}

	void* allocate(int aSize)
{
    // Get a pointer to the memory pool
    unsigned char* MM_pool = ...;

    // Check if the memory pool has enough space to allocate a chunk of the specified size
    if ((int)(*(unsigned short*)(MM_pool)) + aSize + 6 > 65536)
    {
        // If not, call the onOutOfMemory function
        onOutOfMemory();
    }

    // Get a pointer to the next free chunk in the memory pool
    unsigned char* freeChunk = MM_pool + 2 + *(unsigned short*)(MM_pool);

    // Set the size of the free chunk to the specified size
    *(unsigned short*)(freeChunk) = aSize;

    // Set the "allocated" flag for the chunk
    *(freeChunk + 2) = 1;

    // Update the pointer to the next free chunk in the memory pool
    *(unsigned short*)(MM_pool) += aSize + 6;

    // Return a pointer to the data area of the chunk
    return freeChunk + 6;
}


	void deallocate(void* aPointer)
	{
    // Use the std::free function to free the memory previously allocated for the pointer
    std::free(aPointer);
	}


	// Will return the size of the memory block pointed to by 'ptr'
	int size(void *ptr)
	{
		// Get the size of the memory block
		int blockSize = malloc_usable_size(ptr);

		// Return the size of the memory block
		return blockSize;
	}
	
	//---
	//--- support routines
	//--- 

	int freeMemory(void)
	{
		// Start with 0 bytes of free memory
		int freeMem = 0;

		// Get the current break value, which is the end of the memory pool
		void* breakValue = sbrk(0);

		// Loop through the memory pool, starting at the beginning
		void* p = NULL;
		while (p < breakValue)
		{
			// Get the size of the current block of memory
			int blockSize = malloc_usable_size(p);

			// If the block is not in use, add its size to the total free memory
			if (!blockSize)
			{
				freeMem += blockSize;
			}

			// Move to the next block of memory
			p = (char*)p + blockSize;
		}

		// Return the total free memory
		return freeMem;
	}

	// Will scan the memory pool and return the total used memory
	int usedMemory(void)
	{
		// Start with 0 bytes of used memory
		int usedMem = 0;

		// Get the current break value, which is the end of the memory pool
		void* breakValue = sbrk(0);

		// Loop through the memory pool, starting at the beginning
		void* p = NULL;
		while (p < breakValue)
		{
			// Get the size of the current block of memory
			int blockSize = malloc_usable_size(p);

			// If the block is in use, add its size to the total used memory
			if (blockSize)
			{
				usedMem += blockSize;
			}

			// Move to the next block of memory
			p = (char*)p + blockSize;
		}

		// Return the total used memory
		return usedMem;
	}	

	// Will scan the memory pool and return the total in-use memory
	int inUseMemory(void)
	{
		// Start with 0 bytes of in-use memory
		int inUseMem = 0;

		// Get the current break value, which is the end of the memory pool
		void* breakValue = sbrk(0);

		// Loop through the memory pool, starting at the beginning
		void* p = NULL;
		while (p < breakValue)
		{
			// Get the size of the current block of memory
			int blockSize = malloc_usable_size(p);

			// If the block is in use, add its size to the total in-use memory
			if (blockSize)
			{
				inUseMem += blockSize;
			}

			// Move to the next block of memory
			p = (char*)p + blockSize;
		}

		// Return the total in-use memory
		return inUseMem;
	}

	// helper function to see teh InUse list in memory
	void traverseInUse()
	{
		int cur = *(unsigned short*)&MM_pool[2];
		int size = *(unsigned short*)&MM_pool[cur];
		int next = *(unsigned short*)&MM_pool[cur+2];
		int prev = *(unsigned short*)&MM_pool[cur+4];
		cout << "\nTraversing InUse Memory....";
		cout << "\n      InUse Head:"<<cur;
		while (cur != 0)
		{
			cout << "\n        Index:"<<cur<<" Size:"<<size<<" Next:"<<next<<" Prev:"<<prev;
			cur = next;
			size = *(unsigned short*)&MM_pool[cur];
			next = *(unsigned short*)&MM_pool[cur+2];
			prev = *(unsigned short*)&MM_pool[cur+4];
		}
	}

	//Helper function to seet eh Used list in memory
	void traverseUsed()
	{
		int cur = *(unsigned short*)&MM_pool[4];
		int size = *(unsigned short*)&MM_pool[cur];
		int next = *(unsigned short*)&MM_pool[cur+2];
		int prev = *(unsigned short*)&MM_pool[cur+4];
		cout << "\nTraversing Used Memory....";
		cout << "\n      Used Head:"<<cur;
		while (cur != 0)
		{
			cout << "\n        Index:"<<cur<<" Size:"<<size<<" Next:"<<next<<" Prev:"<<prev;
			cur = next;
			size = *(unsigned short*)&MM_pool[cur];
			next = *(unsigned short*)&MM_pool[cur+2];
			prev = *(unsigned short*)&MM_pool[cur+4];
		}
		
	}


	// this is called from Allocate if there is no more memory availalbe
	void onOutOfMemory(void)
  	{
    	std::cout << "\nMemory pool out of memory\n" << std::endl;
    	std::cout << "\n---Press \"Enter\" key to end program---:";

		cin.get();

    	exit( 1 );
  }
}
