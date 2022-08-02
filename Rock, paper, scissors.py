"""
Let's play! You have to return which player won! In case of a draw return Draw!.
"""


def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    return "Player "+ ("1" if p1 == "rock" and p2 == "scissors" or p1 == "paper" and p2 == "rock"
                        or p1 == "scissors" and p2 == "paper" else "2")  + " won!"