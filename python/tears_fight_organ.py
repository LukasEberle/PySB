import sys
import time


class Fighter:
    def __init__(self, name, le, ini, armor):
        self.name_ = name
        self.le_ = le
        self.ini_ = ini
        self.armor_ = armor

    def __str__(self):
        return self.name_

    def __repr__(self):
        return self.name_


turn_dict = {}
sys_name = "[T.E.A.R.S. F.O.]"


def main():
    current_turn = 0
    participants = []
    while True:
        listener(current_turn, participants)
        next_turn = sys.maxsize
        for key in turn_dict.keys():
            if turn_dict[key][1] < next_turn:
                next_turn = turn_dict[key][1]
                participants.clear()
                participants.append(turn_dict[key][0])
            elif turn_dict[key][1] == next_turn:
                participants.append(turn_dict[key][0])
        current_turn = next_turn


def listener(turn, participants):
    print(f"{sys_name} Aktuelle Runde: {turn}")
    if participants and turn > 0:
        if len(participants) == 1:
            print(f"{sys_name} {str(participants[0])} kann handeln!")
        elif len(participants) > 1:
            print(f"{sys_name} {participants} können handeln!")
    elif participants and turn == 0:
        print(f"{sys_name} {participants} nehmen aktuell an dem Kampf teil!")
    cmd_in = input(f"{sys_name} Was willst du tun: ")
    lexer(cmd_in, turn, participants)


def lexer(cmd, turn, participants):
    arguments = cmd.split()
    parser(arguments, turn, participants)


def parser(arguments, turn, participants):
    if arguments:
        if arguments[0] == "add":
            if len(arguments) == 4:
                add_fighter(turn, participants, arguments[1], int(arguments[2]), int(arguments[3]))
            elif len(arguments) == 5:
                add_fighter(turn, participants, arguments[1], int(arguments[2]), int(arguments[3]), int(arguments[4]))
            else:
                print(f"{sys_name} Ungültige Parameter! Versuche es erneut!")
        elif arguments[0] == "change-ini":
            if len(arguments) == 3:
                change_ini(turn_dict[arguments[1]][0], int(arguments[2]))
            else:
                print(f"{sys_name} Ungültige Parameter! Versuche es erneut!")
        elif arguments[0] == "end":
            end_turn(turn, participants)
            return
        elif arguments[0] == "help":
            help_cmd()
        elif arguments[0] == "hit":
            if len(arguments) == 3:
                hit_for(turn_dict[arguments[1]][0], int(arguments[2]))
            else:
                print(f"{sys_name} Ungültige Parameter! Versuche es erneut!")
        elif arguments[0] == "list":
            for key in turn_dict:
                print_info(key)
        elif arguments[0] == "quit":
            check = input(f"{sys_name} Bist du sicher, das du das Skript beenden möchtest?\n\t"
                          f"Dadurch werden alle Daten zurückgesetzt [j/n]: ")
            if check.strip().lower() == "j":
                print(f"{sys_name} Vielen Dank für das nutzen eines {sys_name}-Terminals!")
                print(f"{sys_name} Das Team wünscht viel Spaß im weiteren Abenteuers!")
                time.sleep(2)
                sys.exit(0)
            elif check.strip().lower() == "n":
                pass
            else:
                print(f"{sys_name} Ungültige Eingabe! Bitte gebe \'j\' oder \'n\' ein!\n\tZurück ins Rundenmenu!")
        elif arguments[0] == "rm":
            if arguments[1] in turn_dict.keys():
                delete_fighter(arguments[1], participants)
            else:
                print(f"{sys_name} {arguments[1]} ist kein Kampfteilnehmer! Bitte überprüfe deine Rechtschreibung.")
        else:
            print(f"\'{arguments[0]}\' ist kein gültiges Kommando. Wenn du nicht weiter weißt nutze bitte \'help\'.")
    else:
        print(f"{sys_name} Es ist ein Fehler aufgetreten! Versuche es erneut!")
    listener(turn, participants)


def add_fighter(turn, participants, name, le, ini, armor=0):
    new_fighter = Fighter(name, le, ini, armor)
    participants.append(new_fighter)
    fighter_turn = (new_fighter, turn + new_fighter.ini_)
    turn_dict[str(new_fighter)] = fighter_turn


def delete_fighter(fighter, participants):
    turn_dict.pop(fighter)
    print(f"{sys_name} {fighter} wurde erfolgreich aus dem Kampf entfernt!")


def change_ini(fighter, ini):
    fighter.ini_ = ini


def end_turn(turn, participants):
    for fighter in participants:
        if fighter in turn_dict.keys():
            turn_dict[str(fighter)] = (fighter, turn + fighter.ini_)


def hit_for(fighter, dmg):
    if dmg >= fighter.armor_:
        true_dmg = dmg - fighter.armor_
    elif dmg < 0:
        true_dmg = dmg
    else:
        true_dmg = 0
    fighter.le_ -= true_dmg
    if fighter.le_ <= 0:
        print(f"\tDie LE von {str(fighter)} ist auf 0 oder weniger gefallen!\n")
    else:
        print(f"\t{str(fighter)} hat noch {fighter.le_} LE übrig.\n")


def help_cmd():
    with open("../data/tears_commands", 'r', encoding='utf-8') as data:
        print(data.read())


def print_info(key):
    print(key)
    print(f"Nächstes mal dran: Runde {turn_dict[key][1]}")
    print(f"LE: {turn_dict[key][0].le_}\tINI: {turn_dict[key][0].ini_}\n")


if __name__ == "__main__":
    main()

