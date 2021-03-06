# Machine Learning Lab - 1
# Monty Hall Paradox
# CHANDRESH R 01FB15ECS415
#!/usr/bin/env python3
"""Simulate the Monty Hall problem.
"""
import argparse, random
def simulate(num_doors, switch, steps):

    """(int, bool): bool
    Carry out the game for one contestant.  If 'switch' is True,
    the contestant will switch their chosen door when offered the chance.
    Returns a Boolean value telling whether the simulated contestant won.
    """

    # Doors are numbered from 0 up to num_doors-1 (inclusive).
    # Randomly choose the door hiding the prize.

    winning_door = random.randint(0, num_doors-1)
    if steps:
        print('Prize is behind door {}'.format(winning_door+1))
        # The contestant picks a random door, too.
    choice = random.randint(0, num_doors-1)
    if steps:
        print('Contestant chooses door {}'.format(choice+1))
        # The host opens all but two doors.
    closed_doors = list(range(num_doors))
    while len(closed_doors) > 2:

        # Randomly choose a door to open.
        door_to_remove = random.choice(closed_doors)

        # The host will never open the winning door, or the door
        # chosen by the contestant.

        if door_to_remove == winning_door or door_to_remove == choice:
            continue
        # Remove the door from the list of closed doors.
        closed_doors.remove(door_to_remove)

        if steps:
            print('Host opens door {}'.format(door_to_remove+1))
    # Does the contestant want to switch their choice?

    if switch:
        if steps:
            print('Contestant switches from door {} '.format(choice+1), end='')

        # There are two closed doors left.  The contestant will never
        # choose the same door, so we'll remove that door as a choice.

            available_doors = list(closed_doors) # Make a copy of the list.
            available_doors.remove(choice)
        # Change choice to the only door available.
            choice = available_doors.pop()

        if steps:
            print('to {}'.format(choice+1))
        # Did the contestant win?
    won = (choice == winning_door)

    if steps:
        if won:
            print('Contestant WON', end='\n\n')
        else:
            print('Contestant LOST', end='\n\n')
    return won

def main():
    # Get command-line arguments
    parser = argparse.ArgumentParser(description='simulate the Monty Hall problem')
    parser.add_argument('--doors', default=1, type=int, metavar='int', help='number of doors offered to the contestant')
    parser.add_argument('--trials', default=4, type=int, metavar='int', help='number of trials to perform')
    parser.add_argument('--steps', default=True, action='store_true', help='display the results of each trial')
    args = parser.parse_args()
    print('Simulating {} trials...'.format(args.trials))

    # Carry out the trials
    winning_non_switchers = 0
    winning_switchers = 0
    for i in range(args.trials):
        # First, do a trial where the contestant never switches.
        won = simulate(args.doors, switch=False, steps=args.steps)
        if won:
            winning_non_switchers += 1

        # Next, try one where the contestant switches.
        won = simulate(args.doors, switch=True, steps=args.steps)
        if won:
            winning_switchers += 1
        print('Switching won {0:5} times out of {1} ({2}% of the time)'.format(winning_switchers, args.trials,(winning_switchers / args.trials * 100 ) ))
        print('Not switching won {0:5} times out of {1} ({2}% of the time)'.format( winning_non_switchers, args.trials,(winning_non_switchers / args.trials * 100 ) ))

if __name__ == '__main__':
    main()

