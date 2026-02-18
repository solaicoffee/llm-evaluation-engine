from evaluation.engine import EvaluationEngine


def run_benchmark():
    # Define metric weights
    metrics = {
        "accuracy": 0.5,
        "length": 0.3,
        "relevance": 0.2,
    }

    engine = EvaluationEngine(metrics)

    # Example scored output (normally calculated via metrics.py)
    sample_scores = {
        "accuracy": 1.0,
        "length": 0.8,
        "relevance": 0.6,
    }

    final_score = engine.evaluate(sample_scores)

    print(f"Final Evaluation Score: {final_score:.3f}")


if __name__ == "__main__":
    run_benchmark()
