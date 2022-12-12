#ifndef DECK_H
#define DECK_H
#include "card.h"

class Deck {
  private:
  Card items[52];
  int topCard; // index of deck
  public:
  Deck ();
  void refreshDeck();
  Card deal();
  void shuffle();
  bool isEmpty();
  void display();
};

#endif