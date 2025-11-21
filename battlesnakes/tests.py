# battlesnakes/tests.py
"""
Expanded Unit Tests using the built-in Python unittest library.
Covers all main functions in logic.py.

To run the unit tests, use:
    python battlesnakes/tests.py -v
"""

import unittest
import logic


# -------------------------
# Existing AvoidNeckTest
# -------------------------
class AvoidNeckTest(unittest.TestCase):
    def test_avoid_neck_all(self):
        test_head = {"x": 5, "y": 5}
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 5}, {"x": 5, "y": 5}]
        possible_moves = ["up", "down", "left", "right"]
        result_moves = logic._avoid_my_body(test_head, test_body, possible_moves)
        self.assertEqual(len(result_moves), 4)
        self.assertEqual(possible_moves, result_moves)

    def test_avoid_neck_left(self):
        test_head = {"x": 5, "y": 5}
        test_body = [{"x": 5, "y": 5}, {"x": 4, "y": 5}, {"x": 3, "y": 5}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "right"]
        result_moves = logic._avoid_my_body(test_head, test_body, possible_moves)
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_right(self):
        test_head = {"x": 5, "y": 5}
        test_body = [{"x": 5, "y": 5}, {"x": 6, "y": 5}, {"x": 7, "y": 5}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left"]
        result_moves = logic._avoid_my_body(test_head, test_body, possible_moves)
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_up(self):
        test_head = {"x": 5, "y": 5}
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 6}, {"x": 5, "y": 7}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left", "right"]
        result_moves = logic._avoid_my_body(test_head, test_body, possible_moves)
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_down(self):
        test_head = {"x": 5, "y": 5}
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 4}, {"x": 5, "y": 3}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left", "right"]
        result_moves = logic._avoid_my_body(test_head, test_body, possible_moves)
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)


# -------------------------
# get_info
# -------------------------
class GetInfoTest(unittest.TestCase):
    def test_get_info_returns_required_keys(self):
        info = logic.get_info()
        self.assertEqual(info["apiversion"], "1")
        self.assertIn("author", info)
        self.assertIn("color", info)
        self.assertIn("head", info)
        self.assertIn("tail", info)


# -------------------------
# get_move
# -------------------------
class GetMoveTest(unittest.TestCase):
    def test_all_directions(self):
        pos = {"x": 1, "y": 1}
        self.assertEqual(logic.get_move(pos, "left"), {"x": 0, "y": 1})
        self.assertEqual(logic.get_move(pos, "right"), {"x": 2, "y": 1})
        self.assertEqual(logic.get_move(pos, "up"), {"x": 1, "y": 2})
        self.assertEqual(logic.get_move(pos, "down"), {"x": 1, "y": 0})


# -------------------------
# _avoid_board
# -------------------------
class AvoidBoardTest(unittest.TestCase):
    def test_avoid_board_edges(self):
        head = {"x": 0, "y": 0}
        board = {"width": 5, "height": 5}
        moves = ["up", "down", "left", "right"]
        moves_left = logic._avoid_board(head, board, moves.copy())
        self.assertNotIn("left", moves_left)
        self.assertNotIn("down", moves_left)
        self.assertIn("up", moves_left)
        self.assertIn("right", moves_left)


# -------------------------
# _avoid_others
# -------------------------
class AvoidOthersTest(unittest.TestCase):
    def test_avoid_other_snakes(self):
        head = {"x": 1, "y": 1}
        others = [{"x": 2, "y": 1}, {"x": 1, "y": 2}]
        moves = ["up", "down", "left", "right"]
        moves_left = logic._avoid_others(head, others, moves.copy())
        self.assertNotIn("right", moves_left)
        self.assertNotIn("up", moves_left)
        self.assertIn("left", moves_left)
        self.assertIn("down", moves_left)


# -------------------------
# _calculate_distance
# -------------------------
class CalculateDistanceTest(unittest.TestCase):
    def test_distance_calculation(self):
        p1 = {"x": 0, "y": 0}
        p2 = {"x": 3, "y": 4}
        self.assertEqual(logic._calculate_distance(p1, p2), 7)


# -------------------------
# _select_target
# -------------------------
class SelectTargetTest(unittest.TestCase):
    def test_select_nearest_food(self):
        head = {"x": 1, "y": 1}
        food = [{"x": 2, "y": 2}, {"x": 5, "y": 5}]
        target = logic._select_target(head, food)
        self.assertEqual(target, {"x": 2, "y": 2})


# -------------------------
# _move_to_target
# -------------------------
class MoveToTargetTest(unittest.TestCase):
    def test_move_to_target_basic(self):
        head = {"x": 1, "y": 1}
        target = {"x": 3, "y": 1}
        moves = ["up", "down", "left", "right"]
        move = logic._move_to_target(head, target, moves)
        self.assertEqual(move, "right")

    def test_move_to_target_random_when_no_target(self):
        head = {"x": 1, "y": 1}
        moves = ["up", "down"]
        move = logic._move_to_target(head, {}, moves)
        self.assertIn(move, moves)


# -------------------------
# choose_move
# -------------------------
class ChooseMoveTest(unittest.TestCase):
    def test_choose_move_simple(self):
        data = {
            "you": {
                "id": "snake-123",
                "head": {"x": 1, "y": 1},
                "body": [{"x": 1, "y": 1}, {"x": 0, "y": 1}],
            },
            "board": {
                "height": 3,
                "width": 3,
                "food": [{"x": 2, "y": 2}],
                "snakes": [
                    {"id": "snake-123", "body": [{"x": 1, "y": 1}, {"x": 0, "y": 1}]}
                ],
            },
            "game": {"id": "game-1"},
            "turn": 0,
        }
        move = logic.choose_move(data)
        # "left" blocked by body
        self.assertIn(move, ["up", "down", "right"])


if __name__ == "__main__":
    unittest.main()
