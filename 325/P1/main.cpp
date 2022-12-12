#include "deck.h"
#include "card.h"
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
    while (true) 
    {
        if (deck.cardsLeft() == 0) 
        {
            // If the last sum is a fibonacci number, exit the game
            if (isFibonacci(sum)) 
            {
                break;
            }
            // Otherwise, continue playing
            else 
            {
                deck.refreshDeck();
                deck.shuffle();
            }
        }
        // Take a card and check the sum
        Card c = deck.deal();
        sum += c.getValue();
        // If the sum is a fibonacci number, print the stack and increment the piles count
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
        //Otherwise add the card to the stack
        else 
        {
            hand.push(c);
        }
    }

    // Check if the piles count is greater than 0, and if it is, print the "Winner" message
    if (piles > 0) 
    {
        cout << "\nWinner in " << piles << " piles!\n";
    }

    // If the last sum is not a fibonacci number, print the "Loser" message
    if (sum!=0) 
    {
        printStackReverse(hand);
        hand = stack<Card>();
        cout << " Loser\n";
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
