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
    1.  Bankroll initialised to 5k, for all subsequent games
    2.  Start first round
    3.  Ask player for stake
    4.  Make sure stake within bankroll
    5.  Create 52 card shuffled deck
    6.  Deal four cards: two each to dealer and player
    7.  Show one of dealer's cards and both of players
    8.  Player Hit, take another card
    9.  Check for bust, Check for Hit, 
    10. If player stands, play dealer's hand
    11. Dealer hits until Dealer hand is >= 17.
    12. Determine winner
    13. Adjust bankroll
    14. Ask player to continue playing
    15. if play again, repeat from step 3.

    Ways for game to end:
    1.  Player busts (prior to dealer turn)
    2.  Dealer wins, score is higher than player stand, but not a Dealer bust
    3.  Dealer bust

    Rules:
    1.  Card rank 2 - 10; integer rank. 
    2.  Face Card rank J - K; integer 10.
    3.  Aces rank; integer 1 or 11.
    
    """

    def __init__(self):
        #Create and shuffle deck
        self.deck = Deck()
        self.deck.shuffle()

        self.bankroll = Bankroll()

        self.game_round = 1

        self.playing = True

    def play_game(self):
        self.bankroll.ask_stake()

        while True:
            #Initiate a new round and play it
            new_round = Round(self)
            new_round.play_round()

            #Ask to play again
            self.playing = input(
                "Do you want to play again? 
                Yes (any key), No (Enter)"
            )
    
            tally = self.bankroll.check_tally()

            if self.playing and tally:
                #wants to play again and has money
                self.game_round += 1
                continue

            else:
                #exit
                print("Thanks for playing.")
                break

if __name__"__main__":
    print("Let's play Black Jack!")
    #Create game and play
    game = Game()
    Game.play_game(game)

            
Class Card:
    """\

    Initiate a Card object with given suit (H,D,C,S), 
    and a rank. (2-10,J-K,A)
    
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
        return self.deck.,pop()
        
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
         



        
