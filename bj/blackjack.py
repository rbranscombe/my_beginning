#! usr/bin/env python3

#Blackjack game

import os

from random import shuffle
from textwrap import dedent

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six',
         'Seven','Eight', 'Nine', 'Ten', 'Jack',
         'Queen','King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5,
          'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,
          'Ten':10, 'Jack':10, 'Queen':10,
          'King':10, 'Ace':11}

def shuffled_deck():
    deck = []
    deck_str = ''
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    shuffle(deck)
    
    return deck

def deal_card(
        deck,
        person,
        number
):

    for _ in range(number):
        person.append(deck.pop())
    

def deal_hand(
        deck,
        player,
        dealer
):

    deal_card(deck, player, 2)
    deal_card(deck, dealer, 2)

def score(person):

    non_aces = [c for c in person if c != 'Ace']
    aces = [c for c in person if c == 'Ace']
    total = 0

    for card in non_aces:
        if card in ('Jack', 'Queen', 'King'):
            total += 10
        else:
            total += int(card)

    for card in aces:
        if total <= 10:
            total += 11
        else:
            total += 1
    
    return total

def display_info(
        player,
        dealer,
        player_stands
):
  
    print("Your cards:   [{}] ({})".format("][".join(player), score(player)))

    if player_stands:
        print(dedent(
            ("Dealer cards: [{}] ({})"
             .format("][".join(dealer),
             score(dealer)))))
    else:
        print(f"Dealer cards:,[{dealer[0]}][<?>]")

def hit_or_stand():
    while True:
        print("(H)it or (S)tand?")
        ask = input("> ")
        if ans[0].upper in 'HS':
            breakpoint()
            return ask

def player_play(
        deck, player, dealer,
        player_plays, dealer_plays,
        player_stands
):
    while not player_stands:
        if hit_or_stand() == 'S':
            player_plays = False
            dealer_plays = True
            player_stands = True
            display_info(
                player,
                dealer,
                player_stands=True
                )
        elif not player_stands:
            deal_card(deck, player, 1)
            display_info(
                player,
                dealer,
                player_stands=False)
            if score(player) >= 21:
                player_plays = False
                break
    return (dedent(
             player_plays,
             dealer_plays,
             player_stands
        ))

def dealer_play(
        deck, dealer, DEALER_MIN_SCORE,
        player):
    while score(dealer) <= DEALER_MIN_SCORE:
        deal_card(deck, dealer, 1)
    display_info(
        player,
        dealer,
        player_stands=True
        )
    return False

def results(player, dealer,
            player_stands,
            first_hand,
            still_playing):
    if (first_hand and score(player) == 21 and
        score(dealer) != 21):
        print("Player Blackjack!")
        still_playing = False
    elif (first_hand and score(player) != 21 and
          score(dealer) == 21):
        print("Dealer Blackjack!")
        still_playing = False
    elif score(player) > 21:
        print("Player Busted")
        still_playing = False
    if player_stands:
        if score(dealer) > 21:
            print("Dealer Busted")
        elif score(player) > score(dealer):
            print("Player High Score Win")
        elif score(player) < score(dealer):
            print("Player Low Score Win")
        else:
            print("Push. Tie")
        still_playing = False
    return still_playing


def main():
    deck = shuffled_deck()
    player = []
    dealer = []
    player_plays = True
    still_playing = True
    dealer_plays = False
    player_stands = False
    first_hand = True
    DEALER_MIN_SCORE = 17
    deal_hand(deck, player, dealer)
    display_info(player, dealer, player_stands)
    still_playing = results(
        player, dealer, player_stands=False,
        first_hand=True, still_playing=True)
    while still_playing:
        while player_plays:
            (player_plays,
             dealer_plays,
             player_stands
             ) = (player_play(
                 deck,
                 player,
                 dealer,
                 player_plays,
                 dealer_plays,
                 player_stands
                 )
             )

        while dealer_plays:
            dealer_plays = dealer_play(
                deck,
                dealer,
                DEALER_MIN_SCORE,
                player
                )
        still_playing = results(
            player, dealer, player_stands,
            False, still_playing)

if __name__ == '__main__':
    main()
              
            
        
        
