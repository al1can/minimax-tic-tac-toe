## Basic Terminal Tic Tac Toe written in Python

## Rules:
First person to get all the cells in a horizontal, vertical or diagonal line wins.
The input needs to be an integer values in the range of 1-3 and the order x and y separated with a single space.

## Basic Gameplay

                Pick the side you want to play as. X or O
                X
                 - | - | -
                ---+---+---
                 - | - | -
                ---+---+---
                 - | - | -
                Now it is X's turn.
                1 1
                 X | - | -
                ---+---+---
                 - | O | -
                ---+---+---
                 - | - | -
                Now it is X's turn.
                2 1
                 X | X | O
                ---+---+---
                 - | O | -
                ---+---+---
                 - | - | -
                Now it is X's turn.
                1 3
                 X | X | O
                ---+---+---
                 O | O | -
                ---+---+---
                 X | - | -
                Now it is X's turn.
                3 2
                 X | X | O
                ---+---+---
                 O | O | X
                ---+---+---
                 X | O | -
                Now it is X's turn.
                3 3
                 X | X | O
                ---+---+---
                 O | O | X
                ---+---+---
                 X | O | X
                It is a draw!

## Handling of inputs

                 - | - | -
                ---+---+---
                 - | - | -
                ---+---+---
                 - | - | -
                Now it is O's turn.
                0
                Wrong type of input!
                You need to enter integer values in the order x and y separated with a single space.
                1 4
                The input needs to be between 1 and 3
                a
                Wrong type of input!
                You need to enter integer values in the order x and y separated with a single space.
                1 1
                 O | - | -
                ---+---+---
                 - | - | -
                ---+---+---
                 - | - | -
                Now it is X's turn.
                1 1
                This place is not available. Try again different spot!
