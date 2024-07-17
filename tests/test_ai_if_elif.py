import unittest
from ai_if_elif import ai_if, ai_elif

class TestAiIfElif(unittest.TestCase):

    def test_ai_if_true_condition(self):
        result = ai_if(True, lambda: "True action", lambda: "False action")
        self.assertEqual(result, "True action")

    def test_ai_if_false_condition(self):
        result = ai_if(False, lambda: "True action", lambda: "False action")
        self.assertEqual(result, "False action")

    def test_ai_if_false_condition_no_false_action(self):
        result = ai_if(False, lambda: "True action")
        self.assertIsNone(result)

    def test_ai_elif_first_condition_true(self):
        conditions_actions = [
            (True, lambda: "First condition"),
            (True, lambda: "Second condition"),
            (True, lambda: "Third condition")
        ]
        result = ai_elif(conditions_actions)
        self.assertEqual(result, "First condition")

    def test_ai_elif_second_condition_true(self):
        conditions_actions = [
            (False, lambda: "First condition"),
            (True, lambda: "Second condition"),
            (True, lambda: "Third condition")
        ]
        result = ai_elif(conditions_actions)
        self.assertEqual(result, "Second condition")

    def test_ai_elif_no_true_conditions(self):
        conditions_actions = [
            (False, lambda: "First condition"),
            (False, lambda: "Second condition"),
            (False, lambda: "Third condition")
        ]
        result = ai_elif(conditions_actions)
        self.assertIsNone(result)

    def test_ai_elif_empty_list(self):
        result = ai_elif([])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()