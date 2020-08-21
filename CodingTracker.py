"""
File: CodingTracker.py
----------------------
When learning a new language (either foreign or programming language) it is very important
to practice for at least 100 hours to feel proficient and comfortable with the language
and your ability to code on it. It might not get teh user to super advanced level, but it
for sure will give comfort and confidence to accomplish more.

So, this program prompts the user to start practicing, calculates how long the practice
lasted, and what was accomplished on a 100h scale.
The program also asks the user if she/he wants to keep or dismiss the record from the
practice to prevent fail positive in case the user forgot to stop the timer.
"""

import time
from humanfriendly import format_timespan

SECONDS_IN_HOUR = 3600
CODING_GOAL = 100 * SECONDS_IN_HOUR

def main():
    print_intro()
    practice_python_for_100h()
    print_congrats()

def print_intro():
    print()
    print("Practice 100 hours of coding to get familiar with Python (or other language)")

def print_congrats():
    print("You rock! You just completed 100 hours of Python coding! Keep challenging yourself.")

def practice_python_for_100h():
    """
    After 100 hour goal is established, the program promts user to start
    practicing, records the programs, and let user know how much more
    she/he needs to practice to achieve the goal.
    """
    practice_goal = CODING_GOAL
    while practice_goal > 0:
        # Start and Stop time functions to measure time practiced
        start_time = str(input('Press enter when you ready to practice '))
        if start_time == "":
            start_time = time.time()
        stop_time = str(input("Press enter to stop "))
        if stop_time == "":
            stop_time = time.time()
        time_practiced = int(stop_time - start_time)
        print("\nYou practiced " + format_timespan(time_practiced) + ".")
        record = str(input("Record this practice? (y or n): "))
        if record == 'y':
            more_to_go = int(practice_goal - time_practiced)
            practice_goal = more_to_go
            #else:
        #more_to_go = int(practice_goal - time_practiced)
        #practice_goal = more_to_go
        if practice_goal <= 0:
            break
        print("\nYou have " + format_timespan(practice_goal) + " more to go.")
    return practice_goal



if __name__ == '__main__':
    main()