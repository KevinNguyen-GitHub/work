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

#include "deck.h"
#include "card.h"
#include <iostream>
using namespace std;

Deck :: Deck () //calling deck from header
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


void Deck :: refreshDeck() //refresh deck makes a new deck, calls the original constructor
//♠, ♣,♥, ♦
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

Card Deck :: deal() //get top of the card, index of 0?
{
  
  Card dealing = items[topCard];
  topCard++;

  return dealing;
  
  //create counter and need to reset counter everytime after every use and also track index
  //for loop might work better
}

void Deck :: shuffle() { //shuffle deck using random libraries

for (int i = 0; i < 100000; i++) {

  int x = rand() % 52;
  int y = rand() % 52;

  Card temp = items[x];
  items[x] = items[y];
  items[y] = temp;
  
  }
}
  
bool Deck :: isEmpty() {// check using length or something else

  
  if (topCard >= 52) {

    return true;
  }

  else {
    
    return false;
    
  }
}
  
void Deck :: display() { // display deck in 13 columns and 4 rows

  for (int i = 1; i < 53; i++) {

    items[i - 1].display();
    cout << " ";
    if (i % 13 == 0) {

      cout << endl;
    }
  }
  
}

#include <iostream>
#include "card.h"
#include "deck.h"
using namespace std;

bool isFibo(int partSum) {

  int first = 0;
  int second = 1;
  int fiboSum;

  fiboSum = first + second;

  while (fiboSum < partSum){
  //fibonacci until cardSum
    first = second; // 0, 1, 1 , 2
    second = fiboSum; // 1, 1, 2, 3
    fiboSum = first + second; // 0 + 1 = 1 , 1+ 1 = 2, 1+ 2 =3

    //0,1,1,2,3,5,8,13,21,34,55

  } 
  if (fiboSum == partSum) {
    return true;
  }
  
  else {
    return false;
  }
}

int main() {
  srand(time(NULL));
  int userInput = 0;
  Deck items;

  while (userInput < 5){

    cout << "Welcome to Fibonacci Solitaire!\n1. New Deck\n2. Display Deck\n3. Shuffle Deck\n4. Play Solitaire\n5. Exit\nPlease input a number between 1 and 5." << endl;
    cin >> userInput;
    cout << endl;
  

  if (userInput == 1){
    items.refreshDeck();
  }

  else if (userInput == 2){
    items.display();
  }

  else if (userInput == 3){
    items.shuffle();
  }

  else if (userInput == 4){
    Card dealedCard;
    int gameCounter = 0;
    int pileCounter = 0;
    int partSum = 0;
    cout << "Fibonacci Solitaire!!" << endl;
  
    // false until topCard is 52
    while (items.isEmpty() == false) {
      
      dealedCard = items.deal(); //deal one card
      partSum += dealedCard.getValue(); //getValue of dealedcard
      dealedCard.display();
      gameCounter ++;
      cout << ", ";

      // value does not equal the Fibonacci number

      // value equal the Fibonacci number
      if ((isFibo(partSum) == true) && (items.isEmpty() == false)) {
        //refresh partSum to 0
        cout << "Fibo: " << partSum << endl;
        // keeps track of piles
        pileCounter ++;
        partSum = 0;

      }

        //else if (item.isEMpty())&& isFibo(partSum) == false

      if ((isFibo(partSum) == false) && (items.isEmpty()== true)) {
        cout << endl;
        cout << "Last hand value: " << partSum << endl;
        pileCounter ++;
        cout << "Loser in " << pileCounter << " piles!" << endl;
        gameCounter ++;

      }

      else if ((isFibo(partSum) == true) && (items.isEmpty() == true)) {

        pileCounter ++;
        cout << "Fibo:" << partSum << "\nWinner in " << pileCounter << " piles!" << endl;
        gameCounter ++;
        cout << "Games played: " << gameCounter;
      }

      }
    
  }
  
  else if (userInput == 5){

    cout << "The Game has been exited" << endl;
    break;

  }
  else {
    cout << "Please enter a valid integer!" << endl;
    cin >> userInput;
  }
    
  cout << "" << endl;
   }
}