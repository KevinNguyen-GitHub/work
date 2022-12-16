#include "deck.h"
#include "card.h"
#include <iostream>
using namespace std;

Deck :: Deck ()
{
  topCard = 0;
  char rank[] = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'D',   
  'J', 'Q', 'K'};
  char suit[] = {'S', 'D', 'C', 'H'};

  int suitAmount = 0;
  for (int i = 0; i < 52; i++) {

    if (i < 13) {
      suitAmount = 0;
    }

    else if (i < 26) {
      suitAmount = 1;
    }

    else if (i < 39) {
      suitAmount = 2;
    }

    else if (i >= 39) {

      suitAmount = 3;
    }
      items[i] = Card(rank[i % 13], suit[suitAmount]);
  }
}


void Deck :: refreshDeck()
{
  topCard = 0;
  char rank[] = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'D', 
  'J', 'Q', 'K'};
  char suit[] = {'S', 'D', 'C', 'H'};

  int suitAmount = 0;
  for (int i = 0; i < 52; i++) {

  if (i < 13) {
    suitAmount = 0;
  }

  else if (i < 26) {
    suitAmount = 1;
  }

  else if (i < 39) {
    suitAmount = 2;
  }

  else if (i >= 39) {
    suitAmount = 3;
  }

    items[i] = Card(rank[i % 13], suit[suitAmount]);

  }

}

Card Deck :: deal()
{
  
  Card dealing = items[topCard];
  topCard++;

  return dealing;
  
}

void Deck :: shuffle() { 

for (int i = 0; i < 100000; i++) {

  int x = rand() % 52;
  int y = rand() % 52;

  Card temp = items[x];
  items[x] = items[y];
  items[y] = temp;
  
  }
}
  
bool Deck :: isEmpty() {

  if (topCard >= 52) {

    return true;
  }
  else {
    return false;
    
  }
}
  
void Deck :: display() { 

  for (int i = 1; i < 53; i++) {

    items[i - 1].display();
    cout << " ";
    if (i % 13 == 0) {

      cout << endl;
    }
  }
  
}