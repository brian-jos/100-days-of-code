# https://replit.com/@appbrewery/rock-paper-scissors-end
import random

def main():
    rock = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """

    paper = """
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """

    scissors = """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """

    #Write your code below this line 👇
    #           0      1        2
    options = [rock, paper, scissors]
    min = 0
    max = 2
    ''' 
            0 1 2
          -------
        0 | t 1 0
        1 | 1 t 2
        2 | 0 2 t
    '''
    win_table = [["t", "1", "0"],
                 ["1", "t", "2"],
                 ["0", "2", "t"]]

    player_choice = input("Make a choice. 0 = Rock, 1 = Paper, and 2 = Scissors: ")
    
    if not (player_choice.isdigit() and (int(player_choice) >= min and int(player_choice) <= max)):
        print("Invalid input.")
        return
    player_choice = int(player_choice)
    print(options[player_choice])

    cpu_choice = random.randint(min, max)
    print(f"\nComputer chose:\n{options[cpu_choice]}\n")

    winner = win_table[cpu_choice][player_choice]
    if (winner == str(player_choice)):
        print("You win!")
    elif (winner == "t"):
        print("Tie.")
    else:
        print("You lose.")

if __name__ == "__main__":
    main()
    