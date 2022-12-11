#include "card.h"
using namespace std;
Card :: Card()
{
  rank = ' ';
  suit = ' ';
}
Card::Card( char r, char s )// constructor to create a card, setting the rank and suit 
{
  suit = r;
  rank = s;
}
void Card::setCard( char r, char s)//set existing card to new values 
{
  suit = r;
  rank = s;
} 
int Card::getValue( )// return the point value of the card. Ace = 1, 2 thru 10, Jack = 10, Queen = 10, King = 10 
{
  if (rank == 'A') 
	{
		return 1;
	}
		else if (rank == '2') 
	{
	return 2;
	}
	else if (rank == '3') 
	{
		return 3;
	}
	else if (rank == '4') 
	{
		return 4;
	}
	else if (rank == '5') 
	{
		return 5;
	}
	else if (rank == '6') 
  {
		return 6;
	}
	else if (rank == '7') 
	{
		return 7;
	}
	else if (rank == '8') 
	{
		return 8;
	}
	else if (rank == '9') 
	{
		return 9;
	}
	else 
	{
		return 10;
	}
}
void Card::display( )// display the card using 2 fields… Ace of Spade:AS, Ten of Diamond:10D, Queen of Heart:QH, Three of Club:3C. (If you want to get fancy, you can use these symbols for the suit ♠, ♣, ♥, ♦)
{
  cout << rank << suit<<".";
}

