//Create a class Card
#ifndef CARD_H
#define CARD_H
#include<iostream>
using namespace std;
class Card {
  private:
    char rank;
    char suit;
  public:
    Card();
    Card(char r, char s);//Create the card
  void setCard(char r, char s);//Set card attributes
  int getValue();//Getter
  void display();// Show the card 
};
#endif // !CARD_H