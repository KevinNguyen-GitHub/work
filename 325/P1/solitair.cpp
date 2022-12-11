#include "deck.h"
#include <stack>

//Create object of Deck class
Deck deck;

//Function prototypes
void playGame();
bool isPrime(int val);
void printStackReverse(stack<Card> s);

int main()
{
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
            playGame();
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
void playGame() 
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
        if (isPrime(sum)) 
        {
            hand.push(c);
            //Display stack reverse order
            printStackReverse(hand);
            hand = stack<Card>();
            cout << " Prime: " << sum << endl;
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
//Check passed value is prime or not
bool isPrime(int val) 
{
    bool prime = true;
    if (val == 0 || val == 1) {
    prime = false;
    }
    else {
        for (int i = 2; i <= val / 2; ++i) 
        {
            if (val % i == 0) 
            {
                prime = false;
                break;
            }
        }
    }
    if (prime)
        return true;
    else
        return false;
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