from random import randint

def roll_dice(self):
    doubles = False
    die_1 = randint(1, 6)
    die_2 = randint(1, 6)

    print "You rolled a %d and a %d." % (die_1, die_2)

    if die_1 == die_2:
        print "You've won! Congrats!"
        doubles = True
        return doubles