# Rock Paper Scissors

## Overview

This Python program implements the classic **Rock, Paper, Scissors** game. The player competes against the computer by choosing either rock, paper, or scissors, and the game decides the winner based on the standard rules:

- Rock beats Scissors.
- Scissors beat Paper.
- Paper beats Rock.

The game continues until the player decides to exit.

## Key Features

- **Interactive Gameplay**: Players input their choices, and the computer randomly selects its move.
- **Winner Announcement**: After each round, the program announces the winner (player or computer) or if it's a tie.
- **Multiple Rounds**: The player can continue playing multiple rounds until they decide to exit the game.
- **Randomized Computer Moves**: The program uses Python's `random` module to make the game unpredictable.

## How to Use the Program

1. **Run the Program**: After compiling and executing the Python script in a terminal or console, the game starts.
2. **Choose an Option**: The player is prompted to choose between rock, paper, or scissors.
3. **View Results**: After the player makes a choice, the computer's choice is revealed, and the winner is announced.
4. **Play Again or Exit**: The player can continue playing or choose to exit the game.

## Game Rules

- **Rock**: Beats scissors but loses to paper.
- **Paper**: Beats rock but loses to scissors.
- **Scissors**: Beat paper but lose to rock.
- If both player and computer choose the same option, it's a **tie**.

## Program Structure

- **Main Function**: Drives the flow of the game, handling user input and determining whether to continue or exit.
- **Randomization**: The computer's move is randomly selected from the options (rock, paper, scissors) using the random module.
- **Game Logic**: The game compares the player's move and the computer's move to determine the winner based on the rules of the game.

## Example of Running the Program

### Run the Program
```bash
python rock_paper_scissors.py
```

### Example Output
```bash
Choose rock, paper, or scissors: rock
Computer chose: scissors
You win! Rock beats scissors.

Would you like to play again? (yes/no): no
Thanks for playing!
```

## Future Improvements

- **Score Tracking: Implement a feature to track the player's and computer's scores across multiple rounds.
- **Extended Game Options**: Add additional moves like "Lizard" and "Spock" for a more complex game.
- **Graphical User Interface (GUI)**: Create a graphical version using a Python GUI library like Tkinter.

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

- Feel free to submit issues or pull requests for any improvements or bug fixes.

## Author

- Lavneet Hora
- Sophomore @ Texas Tech University
- Computer Science
