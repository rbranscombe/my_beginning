#! /usr/bin/env python3

#blackjack.py

import os
import random

Class Game:
    """\
    Game of Blackjack:

    Components

    - computer dealer
    - human player
    - 52 cards; 1 deck
    - player bankroll
    - gameplay
    - round

    Gameplay:
    1. Create a Bankroll - inial value given - $5K - used for all subsequent games
    2. Create Deck and shuffle
    3. Gameplay:
         - first round attribute is true, 
         - player active is true,
         - player double-down is false, 
         - player quit is false, 
         - player stand is false
         - player hand count is false (one)
         Player active is true.  
    4.   Player stake? Double down? Stake validity check
    5.   Player double-down is false: player hand count is false.
           Deal two cards each to player and dealer
         Player double-down is true: player hand count is true.
            and then deal one card to each hand
    7.   Show all player cards, and one of dealer cards, double-down is false, hand count is false
    8.   Show all player cards, and one of dealer cards, double-down is true, hand count is true   
    9.      Check for player blackjack - ie 21 on either hand
             if blackjack, hit is false, doubledown is false, quit is false and stand is true       
    10.     Check for player Double-down option - ie , hand count is false, both cards of same rank
             if true then offer player option to double-down - ie doubledown is true. 
            Ask player for move - hit, stand, doubledown or quit
    11.      Hit - take card
    12.       Check for player bust 
    12.       Ask player for move - hit, stand, doubledown is false, quit is false
    11.       repeat until bust or stand
    12.      Doubledown is true
      


Class Card:
    """\
    Initiate a Card object with given suit (H,D,C,S), and
    a rank. (2-10,J-K,A)
    """

    def __init__(self,suit:str,rank:str):
        self.suit = suit
        self.rank = rank

    def __str__(self)
        return self.rank + 'of' + self.suit

Class Deck:
    """\
    Create a 52 card deck.
    """

    def __init__(self):
        self.deck = list()
        self.suits = ["Diamonds", "Hearts",
                      "Spades", "Clubs"]
        self.ranks = ["Two", "Three", "Four", "Five",
                      "six", "Seven","Eight", "Nine",
                      "Ten", "Jack", "Queen", "King",
                      "Ace"]
        self.d_ranks = {"Two":2, "Three":3, "Four":4,
                        "Five":5, "Six":6, "Seven":7,
                        "Eight":8,"Nine":9, "Ten":10,
                        "Jack":10, "Queen":10,
                        "King":10, "Ace":11}
        
        #Build card objects and add them to deck list
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self)
        #Method to Initialise and populate deck string
        deck_str = ""
        for card in self.deck:
            deck_str += "\n" + card.__str__()
        return deck_str

    def shuffle(self):
        #Method to shuffle deck list
        random.shuffle(self.deck)

    def deal(self):
        #Method to deal a card from the deck list
        return self.deck.pop()
    """
        
class Hand:
    """\
    1) A hand holds the cards that have been dealt to 
    a game participant from the deck.  
    2) Maintains card value, corrects for ace strategy.
    """

    def __init__(self, round):
        self.cards = list()
        self.value = 0
        self.aces = 0 #Ace attribute, track hand aces

        self.round = round
        self.game = round.game
        self.deck = self.game.deck


    def setup(self):
        #Method to add two cards to player and dealer hands
        self.add_card(self.deck.deal())
        self.add_card(self.deck.deal())


    def add_card(self, card):
        #Method to add card to hand; calculate value
        self.cards.append(card)
        self.value += self.deck.values[card.rank]

        #Track aces
        if card.rank == "Ace":
            self.aces += 1
            
    def adjust_for_ace(self):
        #Method to adjust ace value
        while self.aces == True and self.value > 21:
            self.value -= 10
            self.aces -= 1
            #remove aces until total in play range.

    def hit(self):
        #Method to add card and adjust for ace
        self.add_card(self.deck.deal())
        self.adjust_for_ace()
        
    def strategy(self):
        #Method for hit or stand?
        ask = str(input("(H)it or (S)tand?"))
        if aks[0].upper().strip() == "H":
            self.game.active = 1:
            self.hit()
            if self.value <= 21:
                self.round.show_hoands()
    def __str__(self):
        hand_str = ""
        for card in self.cards:
            hand_str += "\n " + card.__str__()
        return "hand is:" + hand_str
            
                
Class Bankroll:
    """\
    Tracker for player stakes and bankroll tally.
    """

    def __init__(self):
        self.total = 5000
        self.stake = 0

    def win_wager(self):
        self.total += self.stake

    def lose_wager(self):
        self.total -+ self.stake

    def make_wager(self):
        while True:
            self.stake_ask = input("Enter game stake between {1} and {self.total}. QUIT to exit.")
            self.stake_ask = self.stake_ask.strip()
            if self.stake_ask[0]..upper() == "Q":
                print("Thanks for playing")
                exit()
            elif self.stake_ask.isdecimal
                if 1 < self.stake_ask <= self.total:
                    self.stake = int(self.stake_ask)
                    break
                else:
                    print(f"Hey! Try an integer between '{1}' and {self.total}")
            else:
                print("Try a valid entry again please")

    def check_tally
        tally = True
        if self.total <= 0:
            tally = False
            print("Sorry.  No money... no stakes!"
        return tally

    


    


    
Class Round:
    """/
    Each game has at least one round.  
    """

    def __init__(self, game):
        self.game = game
        #Deal first round cards
        self.player = Hand(self)
        self.dealer = Hand(self)

    def show_hands(self):
        #check if player game is active, hide dealer card
        print("\nPlayer's total is:", self.player.value, "and", self.player.__str__())
        if self.game.active:
            print("\nDealer's hand is: " <HIDDEN> ", self.dealer.cards[1]")
        else:
            print("\nDealer's total is:", self.daler.value, "and", self.dealer.__str__())


    def find_winner(self):
         



        
