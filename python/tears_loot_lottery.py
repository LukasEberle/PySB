import json
import os
import random
import sys
import time

deck = {}
sys_name = "[T.E.A.R.S. L.L.]"


def main():
    load_deck()


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
    options = deck[str(rarity)]["content"]
    num = len(options)
    fib = [1, 1, 2, 3, 5, 8, 13, 21]
    for i in fib:
        result = random.choice(options)
        print(f"{sys_name} {result}")
        time.sleep(i/10)
    deal(result, rarity)
    # print(f"{sys_name} Du ziehst die Karte: {result}!")
    return result


def roll_multiple(req):
    results = []
    for r in req:
        results.append(roll(r))
    print(f"{sys_name} Du erhälst die folgeneden Karten: {results}")


def deal(card_name, rarity):
    deck[rarity]["content"].remove(card_name)
    deck[rarity]["dealt"].append(card_name)


def put_back(card_name, rarity):
    deck[rarity]["dealt"].remove(card_name)
    deck[rarity]["content"].append(card_name)


def update_deck():
    global deck
    filename = '../data/tears-deck.json'
    with open(filename, 'w', encoding='utf-8') as out:
        json.dump(deck, out)


if __name__ == '__main__':
    main()
