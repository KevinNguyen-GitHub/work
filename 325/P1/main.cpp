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
    first = second;
    second = fiboSum; 
    fiboSum = first + second; 
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