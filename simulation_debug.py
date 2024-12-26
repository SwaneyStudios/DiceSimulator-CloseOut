from game import CloseOutGame
import random

def debug_single_game(strategy):
    """
    Run a single game with detailed output for debugging purposes.
    
    Args:
        strategy (str): 'one_die', 'three_dice', 'mixed', or 'hybrid'
    """
    game = CloseOutGame()
    turns = 0
    
    print(f"\nStarting game with {strategy} strategy")
    print("----------------------------------------")
    
    while not game.is_game_over():
        if strategy == 'one_die':
            num_dice = 1
        elif strategy == 'three_dice':
            num_dice = 3
        elif strategy == 'mixed':
            num_dice = random.choice([1, 3])
        else:  # hybrid strategy
            num_dice = 1 if turns < 2 else 3
            
        rolls = game.process_roll(num_dice)
        turns += 1
        
        state = game.get_game_state()
        print(f"\nTurn {turns}:")
        print(f"Number of dice rolled: {num_dice}")
        print(f"Rolls: {rolls}")
        print(f"Current points: {state['points']}")
        print(f"Closed numbers: {sorted(list(state['closed_numbers']))}")
    
    print("\nGame completed!")
    print(f"Total turns: {turns}")
    return turns

if __name__ == "__main__":
    # Test each strategy once
    strategies = ['one_die', 'three_dice', 'mixed', 'hybrid']
    
    for strategy in strategies:
        debug_single_game(strategy)
        input("\nPress Enter to continue to next strategy...")
