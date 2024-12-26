import random

def roll_dice(sides=6):
    """
    Roll a dice with the specified number of sides.
    Args:
        sides (int): Number of sides on the dice (default is 6)
    Returns:
        int: Random number between 1 and the number of sides
    """
    return random.randint(1, sides)

class CloseOutGame:
    def __init__(self):
        """Initialize the game with a dictionary tracking points for numbers 1-6"""
        self.number_points = {i: 0 for i in range(1, 7)}
        self.closed_numbers = set()

    def roll_multiple_dice(self, num_dice):
        """Roll specified number of dice and return results"""
        return [roll_dice() for _ in range(num_dice)]

    def process_roll(self, num_dice):
        """
        Process a roll of dice and update points.
        Args:
            num_dice (int): Number of dice to roll (1 or 3)
        Returns:
            list: Numbers rolled
            dict: Updated points for each number
        """
        if num_dice not in [1, 3]:
            raise ValueError("Must roll either 1 or 3 dice")

        # Points per die based on number of dice rolled
        points_per_die = 3 if num_dice == 1 else 1
        
        # Roll the dice
        rolls = self.roll_multiple_dice(num_dice)
        
        # Update points for each rolled number
        for roll in rolls:
            if roll not in self.closed_numbers:
                self.number_points[roll] += points_per_die
                if self.number_points[roll] >= 3:
                    self.closed_numbers.add(roll)
                    self.number_points[roll] = 3

        return rolls

    def is_game_over(self):
        """Check if all numbers are closed out"""
        return len(self.closed_numbers) == 6

    def get_game_state(self):
        """Return current game state"""
        return {
            'points': self.number_points,
            'closed_numbers': self.closed_numbers
        }
