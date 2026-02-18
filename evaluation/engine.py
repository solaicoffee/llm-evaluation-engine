from typing import List, Dict


class EvaluationEngine:
    def __init__(self, metrics: Dict[str, float]):
        """
        metrics: dictionary of metric_name -> weight
        Example:
        {
            "accuracy": 0.5,
            "clarity": 0.3,
            "relevance": 0.2
        }
        """
        self.metrics = metrics

    def evaluate(self, scores: Dict[str, float]) -> float:
        """
        scores: dictionary of metric_name -> score (0-1)
        Returns weighted final score.
        """
        total_score = 0.0
        total_weight = 0.0

        for metric, weight in self.metrics.items():
            if metric not in scores:
                raise ValueError(f"Missing score for metric: {metric}")

            total_score += scores[metric] * weight
            total_weight += weight

        if total_weight == 0:
            raise ValueError("Total weight cannot be zero.")

        return total_score / total_weight
