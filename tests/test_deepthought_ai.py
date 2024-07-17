import unittest
from unittest.mock import patch
import deepthought_ai

@patch('deepthought_ai.main.eval_condition_with_ai')
class TestAiIfElif(unittest.TestCase):

    def test_ai_if_true_condition(self, mock_eval):
        mock_eval.return_value = True
        result = deepthought_ai.ai_if("True condition", lambda: "True action", lambda: "False action")
        self.assertEqual(result, "True action")
        mock_eval.assert_called_once_with("True condition")

    def test_ai_if_false_condition(self, mock_eval):
        mock_eval.return_value = False
        result = deepthought_ai.ai_if("False condition", lambda: "True action", lambda: "False action")
        self.assertEqual(result, "False action")
        mock_eval.assert_called_once_with("False condition")

    def test_ai_if_false_condition_no_false_action(self, mock_eval):
        mock_eval.return_value = False
        result = deepthought_ai.ai_if("False condition", lambda: "True action")
        self.assertIsNone(result)
        mock_eval.assert_called_once_with("False condition")

    def test_ai_elif_first_condition_true(self, mock_eval):
        mock_eval.side_effect = [True, False, False]
        conditions_actions = [
            ("First condition", lambda: "First action"),
            ("Second condition", lambda: "Second action"),
            ("Third condition", lambda: "Third action")
        ]
        result = deepthought_ai.ai_elif(conditions_actions)
        self.assertEqual(result, "First action")
        mock_eval.assert_called_with("First condition")

    def test_ai_elif_second_condition_true(self, mock_eval):
        mock_eval.side_effect = [False, True, False]
        conditions_actions = [
            ("First condition", lambda: "First action"),
            ("Second condition", lambda: "Second action"),
            ("Third condition", lambda: "Third action")
        ]
        result = deepthought_ai.ai_elif(conditions_actions)
        self.assertEqual(result, "Second action")
        self.assertEqual(mock_eval.call_count, 2)

    def test_ai_elif_no_true_conditions(self, mock_eval):
        mock_eval.return_value = False
        conditions_actions = [
            ("First condition", lambda: "First action"),
            ("Second condition", lambda: "Second action"),
            ("Third condition", lambda: "Third action")
        ]
        result = deepthought_ai.ai_elif(conditions_actions)
        self.assertIsNone(result)
        self.assertEqual(mock_eval.call_count, 3)

    def test_ai_elif_empty_list(self, mock_eval):
        result = deepthought_ai.ai_elif([])
        self.assertIsNone(result)
        mock_eval.assert_not_called()

    def test_ai_if_with_natural_language_condition(self, mock_eval):
        mock_eval.return_value = True
        result = deepthought_ai.ai_if("Is the sky blue?", lambda: "Yes", lambda: "No")
        self.assertEqual(result, "Yes")
        mock_eval.assert_called_once_with("Is the sky blue?")

if __name__ == '__main__':
    unittest.main()