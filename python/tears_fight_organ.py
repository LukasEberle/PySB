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
set_of_fighters = set()


def main():
    current_turn = 0
    listener(current_turn, [])


def listener(turn, participants):
    sys_name = "[T.E.A.R.S. F.O.]"
    print(f"{sys_name} Aktuelle Runde: {turn}")
    if participants:
        if len(participants) == 1:
            print(f"{sys_name} {str(participants[1])} kann handeln!")
        elif len(participants) > 1:
            p = []
            for elem in participants:
                p.add(str(elem))
            print(f"{sys_name} {participants} können handeln!")
    cmd_in = input(f"{sys_name} Was willst du tun: ")
    lexer(cmd_in, turn, participants)


def lexer(cmd, turn, participants):
    arguments = cmd.split()
    print(arguments)
    parser(arguments, turn, participants)


def parser(arguments, turn, participants):
    pass


def add_fighter(turn, name, le, ini, armor=0):
    new_fighter = Fighter(name, le, ini, armor)
    set_of_fighters.add(new_fighter)
    fighter_turn = (new_fighter, turn + new_fighter.ini_)
    turn_dict[str(new_fighter)] = fighter_turn


def delete_fighter(fighter):
    turn_dict.pop(str(fighter))


def change_ini(fighter, ini):
    fighter.ini_ = ini


def next_turn_for(participants):
    for fighter in participants:
        turn_dict[str(fighter)] += fighter.ini_


def hit_for(fighter, dmg):
    if dmg >= fighter.armor_:
        true_dmg = dmg - fighter.armor_
    elif dmg < 0:
        true_dmg = dmg
    else:
        true_dmg = 0
    fighter.le_ -= true_dmg
    if fighter.le_ <= 0:
        print(f"Die LE von {str(fighter)} ist auf 0 oder weniger gefallen und wird aus dem Kampf genommen!")
        delete_fighter(fighter)
    else:
        print(f"{str(fighter)} hat noch {fighter.le_} LE übrig.")


if __name__ == "__main__":
    main()

