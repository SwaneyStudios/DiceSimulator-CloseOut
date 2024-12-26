from game import CloseOutGame

# Example usage
game = CloseOutGame()

# Roll a single die (worth 3 points)
rolls = game.process_roll(1)
print(f"Rolled: {rolls}")
print(f"Game state: {game.get_game_state()}")

# Roll three dice (worth 1 point each)
rolls = game.process_roll(3)
print(f"Rolled: {rolls}")
print(f"Game state: {game.get_game_state()}")

# Check if game is over
print(f"Game over: {game.is_game_over()}")