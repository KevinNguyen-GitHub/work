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
  srand(time(0)); // Use the current time as the seed for the random number generator
  for (int i = 0; i < cardsCnt; i++)
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

#include "deck.h"
#include <stack>

//Function prototypes
void playGame(Deck& deck);
bool isFibonacci(int val);
void printStackReverse(stack<Card> s);

int main()
{
    // Create a deck object
    Deck deck;

    int ch;
    //Loop until exit
    while (true) 
    {
        //User choices
        cout << "Welcome to Solitaire Prime!\n1) New Deck\n2) Display Deck\n3) Shuffle Deck\n4) Play Solitaire\n5) Exit\n\nEnter choice: ";
        cin >> ch;
        //Switch according to choice
        switch (ch) 
        {
            //Create a new deck
            case 1:
            deck.refreshDeck();
            cout << "\nNew deck created\n";
            break;
            //Display deck
            case 2:
            cout << "\nDeck:\n";
            deck.display();
            cout << endl;
            break;
            //Shuffle deck of cards
            case 3:
            deck.shuffle();
            cout << "\nShuffled deck created\n";
            break;
            //Play game
            case 4:
            playGame(deck);
            break;
            //End
            case 5:
            cout << "\nThank you!!!\n";
            exit(0);
            break;
            default:
            cout << "\nIncorrect choice\n";
            break;
        }
        cout << endl;
    }
}

//Function simulate a play
void playGame(Deck& deck) 
{
    cout << deck.cardsLeft() << endl;
    int piles = 0,sum=0;
    stack<Card> hand;
    cout << "\nPlaying Solitaire game!!\n\n";
    //Play game until deck cards count reach 0
    while (deck.cardsLeft() != 0) 
    {
        //Otherwise take a card check sum
        Card c = deck.deal();
        sum += c.getValue();
        //If print then clear and increment piles count
        if (isFibonacci(sum)) 
        {
            hand.push(c);
            //Display stack reverse order
            printStackReverse(hand);
            hand = stack<Card>();
            cout << " Fibonacci: " << sum << endl;
            piles++;
            sum = 0;
        }
        //Otherwise add into stack
        else 
        {
            hand.push(c);
        }
    }
    if (sum!=0) 
    {
        printStackReverse(hand);
        hand = stack<Card>();
        cout << " Loser\n";
    }
    else 
    {
        cout << "\nWinner in " << piles << " piles!\n";
    }
}

//Check passed value is fibo or not
bool isFibonacci(int n)
{
  if (n == 0 || n == 1)
  {
    return true;
  }

  int a = 0;
  int b = 1;

  while (b < n)
  {
    int c = a + b;
    a = b;
    b = c;
  }

  return (b == n);
}


//Display stack in reverse order
void printStackReverse(stack<Card> s)
{
    if (s.empty())
        return;
    Card x = s.top();
    s.pop();
    printStackReverse(s);
    x.display();
    cout << " ";
    s.push(x);
}
