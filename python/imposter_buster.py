beans = ()
suspects = ()


def death_of(bean):
    beans.remove(bean)
    for murder in suspects:
        murder.remove(bean)


def add_murder():
    suspects.append(())


def add_suspect(murder_number, suspect):
    suspects[murder_number].append(suspect)


def start_game(players):
    beans.clear()
    for elem in players:
        beans.append(elem)


def check_for_killer():
    for case in suspects:
        if len(case) == 1:
            killer = case
            suspects.remove(case)
            return killer
    return "No Confirmed Killer"
