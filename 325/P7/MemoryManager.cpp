#include "MemoryManager.h"

#include <iomanip>
#include <iostream>
using namespace std;

typedef unsigned short sPtr;

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
		int freeListStart = 0; // starting index of the freelist
		int inUseListStart = 2; // starting index of the inUse list
		int usedListStart = 4; // starting index for the used list - deallocated memory

		// Set the head of the free list to the index following the used list
		*(unsigned short*)(MM_pool + freeListStart) = usedListStart + 2;
		// Set the head of the inUse list to null
		*(unsigned short*)(MM_pool + inUseListStart) = 0;
		// Set the head of the used list to null
		*(unsigned short*)(MM_pool + usedListStart) = 0;
	}


	// return a pointer inside the memory pool
	void *allocate(int size)
	{
		// Declare as pointers so I can dereference only as needed
		sPtr *freeListHead = (sPtr *)(MM_pool);
		sPtr *inUseListHead = (sPtr *)(MM_pool + 2);
		sPtr *usedListHead = (sPtr *)(MM_pool + 4);

		// Check if there is enough space in the memory pool
		if ((int)(*freeListHead) + size + 6 > 65536)
		{
			onOutOfMemory();
		}

		// Get the node at the head of the free list
		sPtr *node = (sPtr *)(MM_pool + *freeListHead);
		// Get the next and previous pointers of the node
		sPtr *nodeNext = (sPtr *)(MM_pool + *freeListHead + 2);
		sPtr *nodePrev = (sPtr *)(MM_pool + *freeListHead + 4);

		// Set the size of the node
		*node = size;
		// Set the previous pointer of the node to null
		*nodePrev = 0;
		// Set the next pointer of the node to the head of the inUse list
		*nodeNext = *inUseListHead;

		// If the inUse list is not empty, set the previous pointer of the head of the inUse list to the current node
		if (*nodeNext != 0)
		{
			*(sPtr *)(MM_pool + *nodeNext + 4) = *freeListHead;
		}

		// Set the head of the inUse list to the current node
		*inUseListHead = *freeListHead;
		// Update the head of the free list to the next available block of memory
		*freeListHead = *inUseListHead + size + 6;

		// Return a pointer to the data portion of the node
		return (void *)(MM_pool + *inUseListHead + 6);
	}

	// Free up a chunk previously allocated
	void deallocate(void *pointer)
	{
		// Declare as pointers so I can dereference only as needed
		char *sNode = (char *)pointer;

		sPtr *freeListHead = (sPtr *)(MM_pool);
		sPtr *inUseListHead = (sPtr *)(MM_pool + 2);
		sPtr *usedListHead = (sPtr *)(MM_pool + 4);

		// Get the node that contains the data pointed to by 'pointer'
		sPtr *node = (sPtr *)(sNode - 6);
		// Get the next and previous pointers of the node
		sPtr *nodeNext = (sPtr *)(sNode - 4);
		sPtr *nodePrev = (sPtr *)(sNode - 2);

		// If the node has a next node, set the previous pointer of the next node to the previous node of the current node
		if (*nodeNext != 0)
		{
			*(sPtr *)(MM_pool + *nodeNext + 4) = *nodePrev;
		}

		// If the node has a previous node, set the next pointer of the previous node to the next node of the current node
		if (*nodePrev != 0)
		{
			*(sPtr *)(MM_pool + *nodePrev + 2) = *nodeNext;
		}

		// Set the next pointer of the current node to the head of the used list
		*nodeNext = *usedListHead;
		// Set the previous pointer of the current node to null
		*nodePrev = 0;

		// If the used list is not empty, set the previous pointer of the head of the used list to the current node
		if (*nodeNext != 0)
		{
			*(sPtr *)(MM_pool + *nodeNext + 4) = ((char *)node - MM_pool);
		}
		// Set the head of the used list to the current node
		*usedListHead = ((char *)node - MM_pool);
	}



	int size(void *ptr)
	{
		return *(sPtr *)((char *)ptr - 6);
	}
	//---
	//--- support routines
	//--- 

	// Will scan the memory pool and return the total free space remaining
	int freeMemory(void)
	{
		return MM_POOL_SIZE - *(sPtr *)(MM_pool);
	}


	int usedMemory(void)
	{
		int total = 0;

		// Get the head of the used list
		int cur = *(unsigned short *)&MM_pool[4];
		int size = *(unsigned short *)&MM_pool[cur];
		int next = *(unsigned short *)&MM_pool[cur + 2];
		int prev = *(unsigned short *)&MM_pool[cur + 4];

		// Iterate through the used list and sum up the sizes of all the nodes
		while (cur != 0)
		{
			total += size + 6;

			// Move to the next node
			cur = next;
			size = *(unsigned short *)&MM_pool[cur];
			next = *(unsigned short *)&MM_pool[cur + 2];
			prev = *(unsigned short *)&MM_pool[cur + 4];
		}

		return total;
	}

	// Will scan the memory pool and return the total in use memory - memory being curretnly used
	int inUseMemory(void)
	{
		int total = 0;

		// Get the head of the inUse list
		int cur = *(unsigned short *)&MM_pool[2];
		int size = *(unsigned short *)&MM_pool[cur];
		int next = *(unsigned short *)&MM_pool[cur + 2];
		int prev = *(unsigned short *)&MM_pool[cur + 4];

		// Iterate through the inUse list and sum up the sizes of all the nodes
		while (cur != 0)
		{
			total += size + 6;

			// Move to the next node
			cur = next;
			size = *(unsigned short *)&MM_pool[cur];
			next = *(unsigned short *)&MM_pool[cur + 2];
			prev = *(unsigned short *)&MM_pool[cur + 4];
		}

		return total;
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
