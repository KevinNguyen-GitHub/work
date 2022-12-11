//Create a deck of cards
#ifndef DECK_H
#define DECK_H
#include "card.h"
class Deck {
//Member variables
  private:
    Card deck[52];
    int cardsCnt;
  //Member variables
  public:
    Deck();
    void refreshDeck();//Create a fresh deck
    Card deal();//Get a card from top
    void shuffle();//Shuffle
    int cardsLeft(); //Number of cards left in deck
    void display();    //Display deck
};
#endif // !DECK_H