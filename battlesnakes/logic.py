import random
from typing import List, Dict
{
"""
This file can be a nice home for your Battlesnake's logic and helper functions.

We have started this for you, and included some logic to remove your Battlesnake's 'neck'
from the list of possible moves!
"""


def get_info() -> dict:
    """
    This controls your Battlesnake appearance and author permissions.
    For customization options, see https://docs.battlesnake.com/references/personalization

    TIP: If you open your Battlesnake URL in browser you should see this data.
    """
    return {
        "apiversion": "1",
        "author": "YourName",  # TODO: Your Battlesnake Username
        "color": "#E8B937",
        "head": "smart-caterpillar",
        "tail": "tiger-tail",
    }


def choose_move(data: dict) -> str:
    """
    data: Dictionary of all Game Board data as received from the Battlesnake Engine.
    For a full example of 'data', see https://docs.battlesnake.com/references/api/sample-move-request

    return: A String, the single move to make. One of "up", "down", "left" or "right".

    Use the information in 'data' to decide your next move. The 'data' variable can be interacted
    with as a Python Dictionary, and contains all of the information about the Battlesnake board
    for each move of the game.

    """
    my_snake = data["you"]  # A dictionary describing your snake's position on the board
    my_head = my_snake["head"]  # A dictionary of coordinates like {"x": 0, "y": 0}
    my_body = my_snake[
        "body"
    ]  # A list of coordinate dictionaries like [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}]
    board = data["board"]
    snakes = board["snakes"]

    others = []
    for snake in snakes:
        if snake["id"] != my_snake["id"]:
            body_coords = snake["body"]
            for body in body_coords:
                others.append(body)

    food = []
    for foodPos in board["food"]:
        food.append(foodPos)

    print(f"OtherPositions: {others}")

    # Uncomment the lines below to see what this data looks like in your output!
    # print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    # print(f"All board data this turn: {data}")
    # print(f"My Battlesnake this turn is: {my_snake}")
    # print(f"My Battlesnakes head this turn is: {my_head}")
    # print(f"My Battlesnakes body this turn is: {my_body}")

    possible_moves = ["up", "down", "left", "right"]

    board = data["board"]
    possible_moves = _avoid_board(my_head, board, possible_moves)

    possible_moves = _avoid_my_body(my_head, my_body, possible_moves)

    possible_moves = _avoid_others(my_head, others, possible_moves)

    target = _select_target(my_head, food)
    move = _move_to_target(my_head, target, possible_moves)

    print(
        f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}"
    )

    return move


def get_move(pos: Dict[str, int], direction: str) -> Dict[str, int]:
    """
    Helper function to get a potential next move given a position and the
    direction name (string).
    """
    moves = {
        "left": {"x": pos["x"] - 1, "y": pos["y"]},
        "right": {"x": pos["x"] + 1, "y": pos["y"]},
        "down": {"x": pos["x"], "y": pos["y"] - 1},
        "up": {"x": pos["x"], "y": pos["y"] + 1},
    }

    return moves[direction]


def _avoid_board(
    my_head: Dict[str, int], board: Dict[str, int], possible_moves: List[str]
) -> List[str]:
    """
    Removes any possible moves that are out of bounds.
    """
    if my_head["x"] == 0:
        possible_moves.remove("left")
    if my_head["x"] == board["width"] - 1:
        possible_moves.remove("right")
    if my_head["y"] == 0:
        possible_moves.remove("down")
    if my_head["y"] == board["height"] - 1:
        possible_moves.remove("up")

    print(f"avoid_board: MyHead:{my_head} MovesLeft:{possible_moves}")

    return possible_moves


def _avoid_my_body(
    my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]
) -> List[str]:
    """
    Removes any moves that would run into own body.
    """
    if get_move(my_head, "left") in my_body:
        possible_moves.remove("left")

    if get_move(my_head, "right") in my_body:
        possible_moves.remove("right")

    if get_move(my_head, "down") in my_body:
        possible_moves.remove("down")

    if get_move(my_head, "up") in my_body:
        possible_moves.remove("up")

    print(f"avoid_my_body: MyHead:{my_head} MovesLeft:{possible_moves}")

    return possible_moves


def _avoid_others(
    my_head: Dict[str, int], others: List[dict], possible_moves: List[str]
) -> List[str]:
    """
    Removes any moves that would run into others.
    """
    if get_move(my_head, "left") in others:
        possible_moves.remove("left")

    if get_move(my_head, "right") in others:
        possible_moves.remove("right")

    if get_move(my_head, "up") in others:
        possible_moves.remove("up")

    if get_move(my_head, "down") in others:
        possible_moves.remove("down")

    print(f"avoid_others: MyHead:{my_head} MovesLeft:{possible_moves}")

    return possible_moves


def _calculate_distance(my_head: Dict[str, int], target: Dict[str, int]) -> int:
    dx = abs(my_head["x"] - target["x"])
    dy = abs(my_head["y"] - target["y"])
    return dx + dy


def _select_target(my_head: Dict[str, int], food: List[dict]) -> Dict[str, int]:
    minDis = 1000
    target = {}
    for foodItem in food:
        dis = _calculate_distance(my_head, foodItem)
        if dis < minDis:
            minDis = dis
            target = foodItem
    print(f"target: {target}")
    return target


def _move_to_target(
    my_head: Dict[str, int], target: Dict[str, int], possible_moves: List[str]
) -> str:
    if bool(target):
        if target["x"] > my_head["x"]:
            if "right" in possible_moves:
                return "right"
        if target["x"] < my_head["x"]:
            if "left" in possible_moves:
                return "left"
        if target["y"] < my_head["y"]:
            if "down" in possible_moves:
                return "down"
        if target["y"] > my_head["y"]:
            if "up" in possible_moves:
                return "up"
    return random.choice(possible_moves)
