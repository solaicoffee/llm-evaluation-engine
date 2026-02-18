import unittest
from evaluation.engine import EvaluationEngine


class TestEvaluationEngine(unittest.TestCase):

    def setUp(self):
        self.metrics = {
            "accuracy": 0.5,
            "clarity": 0.5
        }
        self.engine = EvaluationEngine(self.metrics)

    def test_weighted_score(self):
        scores = {
            "accuracy": 1.0,
            "clarity": 0.0
        }

        result = self.engine.evaluate(scores)
        self.assertAlmostEqual(result, 0.5)

    def test_missing_metric(self):
        scores = {
            "accuracy": 1.0
        }

        with self.assertRaises(ValueError):
            self.engine.evaluate(scores)


if __name__ == "__main__":
    unittest.main()
