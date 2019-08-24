"""
Magic 8 Ball:
    - Simulate a magic 8-ball.
    - Allow the user to enter their question.
    - Display an in progress message(i.e. "thinking").
    - Create 20 responses, and show a random response.
    - Allow the user to ask another question or quit.
Bonus:
Add a gui.
It must have box for users to enter the question.
It must have at least 4 buttons:
ask
clear (the text box)
play again
quit (this must close the window)
"""
import time
import random

answers = ['Absolutely!', 'No problem.', 'No way!', 'Not sure.', 'You are right!', 'He would love it!',
           'She would love it!', 'Go for it!']


def answer():
    question = input('Type in your question: ')
    print('------Thinking!!!------')
    time.sleep(5)
    print(answers[random.randint(0, len(answers))])


def menu():
    choice = input("""Enter:
    - 'a' to ask question
    - 'q' to quit:
    """)

    while choice != 'q':
        if choice == 'a':
            answer()
        else:
            print('Enter right choice!')

        choice = input("""Enter:
        - 'a' to ask question
        - 'q' to quit:
        """)


menu()