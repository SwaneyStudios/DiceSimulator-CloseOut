from game import CloseOutGame
import random
import statistics

def simulate_single_game(strategy):
    """
    Simulate one complete game using a specific strategy.
    
    Args:
        strategy (str): 'one_die', 'three_dice', 'mixed', or 'hybrid'
    
    Returns:
        int: Number of turns taken to complete the game
    """
    game = CloseOutGame()
    turns = 0
    
    while not game.is_game_over():
        if strategy == 'one_die':
            num_dice = 1
        elif strategy == 'three_dice':
            num_dice = 3
        elif strategy == 'mixed':
            num_dice = random.choice([1, 3])
        else:  # hybrid strategy
            num_dice = 1 if turns < 5 else 3
            
        game.process_roll(num_dice)
        turns += 1
    
    return turns

def run_simulation(strategy, num_games=10000):
    """
    Run multiple games with a given strategy and analyze results.
    
    Args:
        strategy (str): 'one_die', 'three_dice', or 'mixed'
        num_games (int): Number of games to simulate
    
    Returns:
        dict: Statistics about the simulation
    """
    results = []
    
    for _ in range(num_games):
        turns = simulate_single_game(strategy)
        results.append(turns)
    
    return {
        'strategy': strategy,
        'games_played': num_games,
        'average_turns': statistics.mean(results),
        'median_turns': statistics.median(results),
        'min_turns': min(results),
        'max_turns': max(results),
        'std_dev': statistics.stdev(results)
    }

def compare_strategies(num_games=1000):
    """
    Compare all strategies and print results.
    
    Args:
        num_games (int): Number of games to simulate for each strategy
    """
    strategies = ['one_die', 'three_dice', 'mixed', 'hybrid']
    results = []
    
    for strategy in strategies:
        result = run_simulation(strategy, num_games)
        results.append(result)
        
        print(f"\nResults for {strategy} strategy:")
        print(f"Average turns: {result['average_turns']:.2f}")
        print(f"Median turns: {result['median_turns']:.2f}")
        print(f"Minimum turns: {result['min_turns']}")
        print(f"Maximum turns: {result['max_turns']}")
        print(f"Standard deviation: {result['std_dev']:.2f}")

def compete_strategies(strategies_to_compare, num_games=1000):
    """
    Have multiple strategies compete against each other and track wins.
    
    Args:
        strategies_to_compare (list): List of strategies to compete
        num_games (int): Number of games to simulate
    
    Returns:
        dict: Statistics about the competition including wins per strategy
    """
    wins = {strategy: 0 for strategy in strategies_to_compare}
    ties = 0
    
    for _ in range(num_games):
        # Run one game for each strategy and track turns
        game_results = {}
        for strategy in strategies_to_compare:
            turns = simulate_single_game(strategy)
            game_results[strategy] = turns
        
        # Find winner(s) of this game
        min_turns = min(game_results.values())
        winners = [s for s, t in game_results.items() if t == min_turns]
        
        if len(winners) > 1:
            ties += 1
        else:
            wins[winners[0]] += 1
    
    # Calculate win percentages
    results = {
        'total_games': num_games,
        'ties': ties,
        'win_counts': wins,
        'win_percentages': {
            strategy: (wins[strategy] / num_games) * 100 
            for strategy in strategies_to_compare
        }
    }
    
    # Print results
    print("\nCompetition Results:")
    print(f"Total games played: {num_games}")
    print(f"Ties: {ties} ({(ties/num_games)*100:.1f}%)")
    for strategy in strategies_to_compare:
        print(f"{strategy}: {wins[strategy]} wins ({results['win_percentages'][strategy]:.1f}%)")
    
    return results

if __name__ == "__main__":
    # Run simulation with 1000 games for each strategy
    print("Running simulation with 1000 games per strategy...")
    compare_strategies(10000)

    # Add this to test the competition
    print("\nRunning head-to-head competition...")
    compete_strategies(['one_die', 'three_dice', 'mixed', 'hybrid'])
