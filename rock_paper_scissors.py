"""
Rock Paper Scissors Game
"""
import random

GAME_BANNER = """
        Hello! Welcome to ROCK PAPER SCISSORS !

        Enter your Choice from Rock[r], Paper[p], Scissors[s]  
"""


def main():
    """Main function of the program"""
    print(GAME_BANNER)
    user_input = input('You: ')
    computer_input = random.choice(['r', 'p', 's'])
    print(f'Computer: {computer_input}\n')

    # Logic
    user_cond = str(user_input) + computer_input

    win_condition = {
        'rs': 'Rock smashes Scissors!',
        'sp': 'Scissors cuts Paper!',
        'pr': 'Paper covers Rock!'}

    if user_input == computer_input:
        return 'Tie. Please try again!'

    elif user_cond in win_condition:
        return win_condition[user_cond] + ' ' + 'You Won!'
    else:
        computer_cond = user_cond[::-1]
        return win_condition[computer_cond] + ' ' + 'Computer Won!'


if __name__ == '__main__':
    print(main())
