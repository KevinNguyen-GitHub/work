#include "MemoryManager.h"
#include <stdlib.h>
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

		int freeHead = 0; // starting index of the freelist
		int inUseHead = 2; // starting index of the inUselist
		int usedHead = 4; // starting index for the used list - deallocated memory

		int nextLink = 2; // offset index of the next link
		int prevLink = 4; // offset index for the prev link

		*(unsigned short*)(MM_pool + freeHead) = 6; // freelist starts at byte 6
		*(unsigned short*)(MM_pool + inUseHead) = 0;	// nothing in the inUse list yet
		*(unsigned short*)(MM_pool + usedHead) = 0; // nothing in the used list yet

	}

	void *allocate(int aSize)
	{
		// Declare as arrays for faster access
		sPtr freeHead[1] = {MM_pool[0]};
		sPtr inUseHead[1] = {MM_pool[2]};
		sPtr usedHead[1] = {MM_pool[4]};

		if (freeHead[0] + aSize + 6 > 65536)
			return nullptr;

		sPtr node[1] = {MM_pool[freeHead[0]]};
		sPtr nodeNext[1] = {MM_pool[freeHead[0] + 2]};
		sPtr nodePrev[1] = {MM_pool[freeHead[0] + 4]};

		node[0] = aSize;
		nodePrev[0] = 0;
		nodeNext[0] = inUseHead[0];

		if (nodeNext[0] != 0) {
			MM_pool[nodeNext[0] + 4] = freeHead[0];
		}

		inUseHead[0] = freeHead[0];
		freeHead[0] = inUseHead[0] + aSize + 6;

		return (void *)(MM_pool + inUseHead[0] + 6);
	}



	void deallocate(void *aPointer)
	{
		// Declare as arrays for faster access
		char *sNode = (char *)aPointer;

		sPtr freeHead[1] = {MM_pool[0]};
		sPtr inUseHead[1] = {MM_pool[2]};
		sPtr usedHead[1] = {MM_pool[4]};

		sPtr node[1] = {*(sPtr *)(sNode - 6)};
		sPtr nodeNext[1] = {*(sPtr *)(sNode - 4)};
		sPtr nodePrev[1] = {*(sPtr *)(sNode - 2)};

		if (nodeNext[0] != 0) {
			MM_pool[nodeNext[0] + 4] = nodePrev[0];
		}

		MM_pool[nodePrev[0] + 2] = nodeNext[0];
		nodeNext[0] = usedHead[0];
		nodePrev[0] = 0;
		MM_pool[nodeNext[0] + 4] = ((char *)node - MM_pool);
		usedHead[0] = ((char *)node - MM_pool);
	}

	// returns the number of bytes allocated by ptr
	int size(void *ptr)
	{
		return *(sPtr *)((char *)ptr - 6);
	}
	
	//---
	//--- support routines
	//--- 

	int freeMemory(void)
	{
		return MM_POOL_SIZE - *(sPtr *)(MM_pool);
	}

	// Will scan the memory pool and return the total used memory
	int usedMemory()
	{
		int total = 0;
		int cur = MM_pool[4];
		int size = MM_pool[cur];
		int next = MM_pool[cur + 2];
		int prev = MM_pool[cur + 4];
		while (cur != 0)
		{
			total += size + 6;
			cur = next;
			size = MM_pool[cur];
			next = MM_pool[cur + 2];
			prev = MM_pool[cur + 4];
		}

		return total;
	}	

	// Will scan the memory pool and return the total in-use memory
	int inUseMemory()
	{
		int total = 0;
		int cur = MM_pool[2];
		int size = MM_pool[cur];
		int next = MM_pool[cur + 2];
		int prev = MM_pool[cur + 4];
		while (cur != 0)
		{
			total += size + 6;
			cur = next;
			size = MM_pool[cur];
			next = MM_pool[cur + 2];
			prev = MM_pool[cur + 4];
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
