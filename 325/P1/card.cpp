#include "card.h"
#include <iostream>
using namespace std;

Card :: Card () // creates empty object card
{
 
 rank = '0';
 suit = 'T';
}

Card :: Card (char r, char s) // passes parameters to an empty card
{
  
  rank = r;
  suit = s;
  
}

void Card::setCard(char r, char s)  // set ranks  like ace, jack, queen, kind to numbers
// how do i set one card when i have set most of the cards to variables?

{

  char A = 1;
  char J = 'D';
  char Q = 'D';
  char K = 'D';
  
}

int Card :: getValue()  //getter function to get values from cards
{

  if (rank == 'A'){

    return 1;
    
  }

   else if ((rank == 'K') || (rank == 'Q') || (rank == 'J')) {

     return 10;
     
   }

   else {
     
    if (rank == '2') {
    return 2;
    }

    if (rank == '3') {
      return 3;
    }

    if (rank == '4') {
      return 4;
    }

    if (rank == '5') {
      return 5;
    }
    if (rank == '6') {
      return 6;
    }
    if (rank == '7') {
      return 7;
    }
    if (rank == '8') {
      return 8;
    }
    if (rank == '9') {
      return 9;
    }

    if (rank == 'D') {

      return 10;
    }

    
   }  

 }


void Card :: display() //displays one object of card for deck?
{ 

  if (rank == 'D') {

    if (suit == 'S') {
    cout << 10 << "♠";
    }

    else if (suit == 'D') {
    cout << 10 << "♦";
    }

    else if (suit == 'H') {
    cout << 10 << "♥";
    }

    else {
    cout << 10 << "♣";
    }
  }

  else if (suit == 'S') {
  cout << rank << "♠";
  }

  else if (suit == 'D') {
  cout << rank << "♦";
  }

  else if (suit == 'H') {
  cout << rank << "♥";
  }

  else{

    cout << rank << "♣";
  }

   //♠, ♣,♥, ♦
  
  // add symbols to string using a loop then print out
}