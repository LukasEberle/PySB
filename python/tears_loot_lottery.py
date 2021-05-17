import json
import os
import random
import sys
import time

deck = {}
sys_name = "[T.E.A.R.S. L.L.]"


def main():
    load_deck()
    print(deck)
    print(deck["1"]["content"])


def listener():
    pass


def lexer():
    pass


def parser():
    pass


def load_deck():
    global deck
    filename = '../data/tears-deck.json'
    with open(filename, 'r', encoding='utf-8') as data:
        deck = json.load(data)


def roll(rarity):
    pass


def deal(card_name, rarity):
    pass


def put_back(card_name, rarity):
    pass


def update_deck():
    pass


if __name__ == '__main__':
    main()
