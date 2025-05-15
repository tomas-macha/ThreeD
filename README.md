# Tic tac toe 3D

This is a 3D version of the tic tac toe game. It is written in Python using PyQt5.

## Run

To run the game, you need to install PyQt5:

```
pip install PyQt5
```

Then, you can run the game by running the `game/main.py` file:

```
python game/main.py
```

## Rules

The game is played on a 4x4x4 grid. The goal is to get four of your pieces in a row, column, or diagonal.
You can choose a stick and your piece will fall to the lowest available position.
This game is played by two players. They have to alternate turns.

## Controls

The game has four modes:

- 2 players
- AI level 1 (plays random moves)
- AI level 2 (three moves in depth)
- AI level 3 (four moves in depth)

You can switch between modes by pressing the `A` key.

You can rotate the camera using arrow keys (left and right).

Place pieces by clicking on the top left grid or one of the sticks.

You can change outer pieces opacity by pressing the `X` key.

## Technical details

ThreeD is written by me using transformation matrices.
The program doesn't use a canvas with z-buffer, so the correct order of object is not guaranteed,
but it should be correct most of the time.
Rendering on canvas is done using PyQt5.
Because this all runs on the CPU, it is very slow, so it generates middle frames.

## License

MIT License