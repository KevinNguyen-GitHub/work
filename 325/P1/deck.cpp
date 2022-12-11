//Implementation of deck class
#include "deck.h"
//Constructor
Deck::Deck() 
{
	char ranks[] = { 'A','1','2','3','4','5','6','7','8','9','J','Q','K' };
	char suits[] = { 'S','H','D','C' };
	int k = 0;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 13; j++)
		{
		deck[k++] = Card(ranks[j], suits[i]);
		}
	}	
	cardsCnt = 52;
}
//Create a fresh deck
void Deck::refreshDeck() 
{
	char ranks[] = { 'A','1','2','3','4','5','6','7','8','9','J','Q','K' };
	char suits[] = { 'S','H','D','C' };
	int k = 0;
	for (int i = 0; i < 4; i++) 
	{
		for (int j = 0; j < 13; j++)
		{
		deck[k++] = Card(ranks[j], suits[i]);
		}
	}
	cardsCnt = 52;
}
//Get a card from top
Card Deck::deal() 
{
	Card c=deck[cardsCnt - 1];
	cardsCnt--;
	return c;
}
//Shuffle
void Deck::shuffle() 
{
	srand(0);
	for (int i = 0; i <cardsCnt; i++)
	{
		int r = i + (rand() % (52 - i));
		Card temp = deck[i];
		deck[i] = deck[r];
		deck[r] = temp;
	}
}
//Number of cards left in deck
int Deck::cardsLeft() 
{
	return cardsCnt;
}
//Display deck
void Deck :: display() 
{
	for (int i = 0; i < 52; i++) 
	{
		if (i % 13 == 0 && i != 0) 
		{
		cout << endl;
		deck[i].display();
		cout << " ";
		}
		else 
		{
			deck[i].display();
			cout << " ";
		}
	}
}