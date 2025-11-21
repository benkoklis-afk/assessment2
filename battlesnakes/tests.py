# battlesnakes/tests.py
"""
Expanded Unit Tests using unittest.
Includes stricter tests and edge cases that may initially fail.
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
        self.assertEqual(result_moves, expected)


# -------------------------
# get_info
# -------------------------
class GetInfoTest(unittest.TestCase):
    def test_get_info_keys(self):
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
    def test_directions(self):
        pos = {"x": 1, "y": 1}
        self.assertEqual(logic.get_move(pos, "left"), {"x": 0, "y": 1})
        self.assertEqual(logic.get_move(pos, "right"), {"x": 2, "y": 1})
        self.assertEqual(logic.get_move(pos, "up"), {"x": 1, "y": 2})
        self.assertEqual(logic.get_move(pos, "down"), {"x": 1, "y": 0})


# -------------------------
# _avoid_board
# -------------------------
class AvoidBoardTest(unittest.TestCase):
    def test_avoid_edges(self):
        head = {"x": 0, "y": 0}
        board = {"width": 5, "height": 5}
        moves = ["up", "down", "left", "right"]
        moves_left = logic._avoid_board(head, board, moves.copy())
        self.assertNotIn("left", moves_left)
        self.assertNotIn("down", moves_left)


# -------------------------
# _avoid_others
# -------------------------
class AvoidOthersTest(unittest.TestCase):
    def test_avoid_snakes(self):
        head = {"x": 1, "y": 1}
        others = [{"x": 2, "y": 1}, {"x": 1, "y": 2}]
        moves = ["up", "down", "left", "right"]
        moves_left = logic._avoid_others(head, others, moves.copy())
        self.assertNotIn("right", moves_left)
        self.assertNotIn("up", moves_left)


# -------------------------
# _calculate_distance
# -------------------------
class CalculateDistanceTest(unittest.TestCase):
    def test_distance(self):
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

    def test_no_food(self):
        head = {"x": 0, "y": 0}
        target = logic._select_target(head, [])
        self.assertEqual(target, {})  # should return empty dict


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

    def test_move_to_target_no_valid_target(self):
        head = {"x": 1, "y": 1}
        moves = ["up", "down"]
        move = logic._move_to_target(head, {}, moves)
        self.assertIn(move, moves)


# -------------------------
# choose_move
# -------------------------
class ChooseMoveTest(unittest.TestCase):
    def test_choose_move_basic(self):
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
                "snakes": [{"id": "snake-123", "body": [{"x": 1, "y": 1}, {"x": 0, "y": 1}]}],
            },
            "game": {"id": "game-1"},
            "turn": 0,
        }
        move = logic.choose_move(data)
        self.assertIn(move, ["up", "down", "right"])  # left blocked by body

    def test_choose_move_trapped(self):
        """Edge case where snake has no valid moves."""
        data = {
            "you": {
                "id": "snake-123",
                "head": {"x": 0, "y": 0},
                "body": [{"x": 0, "y": 0}, {"x": 0, "y": 1}, {"x": 1, "y": 0}],
            },
            "board": {
                "height": 2,
                "width": 2,
                "food": [],
                "snakes": [{"id": "snake-123", "body": [{"x": 0, "y": 0}, {"x": 0, "y": 1}, {"x": 1, "y": 0}]}],
            },
            "game": {"id": "game-1"},
            "turn": 0,
        }
        # Expect the function to raise an IndexError or KeyError because no moves left
        with self.assertRaises(Exception):
            logic.choose_move(data)


if __name__ == "__main__":
    unittest.main()
