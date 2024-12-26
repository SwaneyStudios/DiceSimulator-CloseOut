# Close Out Dice Game Simulator

This project simulates and analyzes different strategies for playing the "Close Out" dice game, a game where players aim to accumulate points for numbers 1-6 until they are all "closed out."

## Game Rules

- Players can choose to roll either 1 die or 3 dice on their turn
- When rolling 1 die, each roll is worth 3 points
- When rolling 3 dice, each roll is worth 1 point
- A number is "closed out" when it accumulates 3 points
- The game ends when all numbers (1-6) are closed out
- The goal is to complete the game in the fewest possible turns

## Strategies Analyzed

The simulator compares four different strategies:

1. **One Die Strategy** (`one_die`)
   - Always rolls a single die for 3 points per roll

2. **Three Dice Strategy** (`three_dice`)
   - Always rolls three dice for 1 point per roll

3. **Mixed Strategy** (`mixed`)
   - Randomly chooses between rolling one die or three dice each turn

4. **Hybrid Strategy** (`hybrid`)
   - Starts with one die for the first few turns
   - Switches to three dice for the remainder of the game

## Features

- Single game simulation with detailed turn-by-turn analysis
- Bulk simulation of thousands of games to generate statistics
- Strategy comparison metrics including:
  - Average turns to completion
  - Median turns
  - Minimum and maximum turns
  - Standard deviation
  - Head-to-head competition results

## Usage

To run the basic simulation:
```bash
python simulation.py
```

To debug a single game with detailed output:
```bash
python simulation_debug.py
```


## Project Structure

- `game.py` - Core game logic and mechanics
- `simulation.py` - Main simulation and analysis code
- `simulation_debug.py` - Detailed single-game debugging tool

## Analysis Results

The simulation provides detailed statistics for each strategy, including:
- Win rates in head-to-head competition
- Average number of turns to completion
- Variability in game length
- Optimal strategy identification

This tool is useful for:
- Understanding game dynamics
- Testing and comparing different strategies
- Identifying optimal play patterns
- Analyzing game balance and mechanics
