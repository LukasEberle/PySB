import json
import os
import random
import sys
import time

deck = {}
sys_name = "[T.E.A.R.S. L.L.]"


def main():
    print(f"{sys_name} Starte die Loot Lottery Routine!")
    print(f"{sys_name} Lade Deck...")
    load_deck()
    print(f"{sys_name} Initialisierung abgeschlossen!")
    while True:
        listener()


def listener():
    print(f"{sys_name} Loot Lottery Routine läuft...")
    cmd_in = input(f"{sys_name} Was willst du tun: ")
    lexer(cmd_in)


def lexer(cmd):
    arguments = cmd.split()
    if arguments[0] == "add" or arguments[0] == "putb":
        if len(arguments) > 3:
            tmp = [arguments[0]]
            card_name = ""
            for a in arguments[1:-1]:
                card_name += a
                if a != arguments[-2]:
                    card_name += " "
            tmp.append(card_name)
            tmp.append(arguments[-1])
            arguments = tmp
    if arguments[0] == "roll" and len(arguments) > 2:
        tmp = ["multi"]
        seq = []
        for a in arguments[1:]:
            seq.append(a)
        tmp.append(seq)
        arguments = tmp
    parser(arguments)


def parser(arguments):
    if arguments:
        if arguments[0] == "add":
            add_card(arguments[1], arguments[2])
            print(f"{sys_name} {arguments[1]} wurde dem Stapel mit Rarität {arguments[2]} hinzugefügt!")
        elif arguments[0] == "help":
            help_cmd()
        elif arguments[0] == "multi":
            print(f"{sys_name} Berechne Loot Lottery {len(arguments[1])} mal...")
            roll_multiple(arguments[1])
        elif arguments[0] == "putb":
            put_back(arguments[1], arguments[2])
            print(f"{sys_name} {arguments[1]} wurde in den Stapel mit Rarität {arguments[2]} zurückgelegt!")
        elif arguments[0] == "roll":
            print(f"{sys_name} Berechne Loot Lottery...")
            print(f"{sys_name} Du ziehst die Karte: {roll(arguments[1])}!")
    else:
        print(f"{sys_name} Es ist ein Fehler aufgetreten! Versuche es erneut!")


def load_deck():
    global deck
    filename = '../data/tears-deck.json'
    with open(filename, 'r', encoding='utf-8') as data:
        deck = json.load(data)


def roll(rarity):
    options = deck[str(rarity)]["content"]
    fib = [1, 1, 2, 3, 5, 8, 13, 21]
    for i in fib:
        result = random.choice(options)
        print(f"{sys_name} {result}")
        time.sleep((i/10) * random.triangular(0.8, 1.2))
    deal(result, rarity)
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


def add_card(card_name, rarity):
    deck[rarity]["dealt"].append(card_name)


def update_deck():
    global deck
    filename = '../data/tears-deck.json'
    with open(filename, 'w', encoding='utf-8') as out:
        json.dump(deck, out)


def help_cmd():
    with open("loot_lottery_commands", 'r', encoding='utf-8') as data:
        print(data.read())


if __name__ == '__main__':
    main()
