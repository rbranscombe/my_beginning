#!/usr/bin/env python3

import argparse

import requests


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("player_tag")
    args = parser.parse_args()
    return args


def get_api_key():
    with open("/home/ruth/clash_royale/api_key.txt") as api_key_file:
        api_key_data = api_key_file.read().rstrip()
    return api_key_data


def is_winner(battle):
    return battle['team'][0]['crowns'] > battle['opponent'][0]['crowns']


def main():
    args = get_args()
    api_key = get_api_key()
    baseurl = "https://api.clashroyale.com/v1"
    url = f"{baseurl}/players/%23{args.player_tag}/battlelog"
    response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
    response.raise_for_status()
    battles_all = response.json()
    battles = [battle for battle in battles_all if battle["type"] == "PvP"]
    battles_won = [battle for battle in battles if is_winner(battle)]
    winning_percentage = round((len(battles_won) / len(battles)) * 100)
    print(f"Winning Percentage: {winning_percentage}")
    
    
if __name__ == "__main__":
    main()
