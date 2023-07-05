from enum import Enum
import pytest
import os


def test_score_calculator():
    assert calculate_score("A Y\nB X\nC Z") == 15


@pytest.mark.parametrize("round_str,expected", [
    ("A X", "DRAW"),
    ("A Y", "WIN"),
    ("A Z", "LOSS"),

    ("B X", "LOSS"),
    ("B Y", "DRAW"),
    ("B Z", "WIN"),

    ("C X", "WIN"),
    ("C Y", "LOSS"),
    ("C Z", "DRAW"),
])
def test_GameRound(round_str, expected):
    game_round = GameRound(round_str)
    assert game_round.game_result() == expected


def calculate_score(strategy_guide: str) -> int:
    total_score = 0
    for round_strategy in strategy_guide.split('\n'):
        game_round = GameRound(round_strategy)
        total_score += game_round.calcule_score()
    return total_score


class Choice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class GameRound():
    def __init__(self, round_strategy: str) -> None:
        choices = round_strategy.split(' ')
        self.their_choice = Choice(ord(choices[0]) - 65)
        self.your_choice = Choice(ord(choices[1]) - (65 + 23))

    def game_result(self):
        if self.your_choice == self.their_choice:
            return 'DRAW'

        your_winning_choices = [
            (Choice.ROCK, Choice.PAPER),
            (Choice.PAPER, Choice.SCISSORS),
            (Choice.SCISSORS, Choice.ROCK),
        ]
        if (self.their_choice, self.your_choice) in your_winning_choices:
            return 'WIN'
        else:
            return 'LOSS'

    def calcule_score(self):
        result = self.game_result()
        score = self.your_choice.value + 1
        if result == 'WIN':
            score += 6
        elif result == 'DRAW':
            score += 3
        return score


if __name__ == '__main__':
    path_to_file = os.path.join(os.path.dirname(__file__), '../day2_input.txt')
    with open(path_to_file, 'r') as file:
        game_strategy = file.read()
    print(calculate_score(game_strategy))
