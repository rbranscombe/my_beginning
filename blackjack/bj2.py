#! /usr/bin/env python3

#bj2.py


import os
import sys
import random
from textwrap import dedent

#Create a deck
ranks = dedent(
    """\
    ["2", "3", "4", "5", "6", "7", 
    "8", "9", "10", "A", "J", "Q", "K"]
    """
    )
suits = ["D", "H", "S", "C"]

def make_deck():
    deck = []
    for rank in ranks:
        for suit in suits:
            card = (rank, suit)
            deck.append(card)
    random.shuffle(deck)
    return deck

#Deal initial hands
deck = make_deck()
p_cards = [deck.pop(), deck.pop()]
d_cards = [deck.pop(), deck.pop()]

#Display the player cards
print(dedent(
    """\
    f"player_cards: 
    first deal: {p_cards}"
    """
    )
)
#Display one of the dealer's cards
print(dedent(
    """\
    f"dealer_cards:
    first deal: [('X', 'X')], {d_cards[1]}"
    """
    )
)



#Sum of the Player cards
p_cards_val = 0
ace = 0

p_card1_val, p_card2_val = (
    p_cards[0][0],
    p_cards[1][0]
    )

if p_card1_val in ["J","Q","K"]:
    p_cards_val += 10
elif p_card1_val == "A":
    ace += 1
    p_cards_val += 11
else:
    p_cards_val += int(p_card1_val)

if p_card2_val in ["J","Q","K"]:
    p_cards_val += 10
elif p_card2_val == "A":
    ace += 1
    p_cards_val += 11
    if p_cards_val > 21:
        p_cards_val -= 10 #use 1 for ace value
else:
    p_cards_val += int(p_card2_val)
    
#Compare Dealer and Player hands
#Player (H)it, (D)ouble down or (S)tand
#Ace ajustment
#Display dealer cards
#Sum of the Dealer cards
#Dealer (H)it or (S)tand
