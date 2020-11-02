class Fighter:
    def __init__(self, name, le, ini, entry, armor):
        self.name_ = name
        self.le_ = le
        self.ini_ = ini
        self.next_turn_ = entry
        self.armor_ = armor

    def __str__(self):
        return self.name_

    def update_next_turn(self):
        self.next_turn_ = self.next_turn_ + self.ini_
        return self.next_turn_


turn_dict = {}
fighter_set = set()


def main():
    current_turn = 0


def lexer():
    pass


def parser():
    pass


def add_fighter(name, le, ini, armor=0):
    fighter_set.add(Fighter(name, le, ini, current_turn, armor))


def delete_fighter(fighter):
    fighter_set.remove(fighter)


def change_ini(fighter, ini):
    fighter.ini_ = ini


def end_turn(turn, participants):
    for fighter in participants:
        fighter.update_next_turn()
    turn += 1

