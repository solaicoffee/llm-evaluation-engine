def accuracy_score(expected: str, actual: str) -> float:
    """
    Very simple accuracy check.
    Returns 1.0 if exact match, else 0.0.
    """
    return 1.0 if expected.strip() == actual.strip() else 0.0


def length_score(response: str, min_length: int = 20) -> float:
    """
    Rewards responses that meet minimum length.
    """
    return 1.0 if len(response) >= min_length else 0.5


def keyword_relevance(response: str, keywords: list) -> float:
    """
    Scores based on keyword presence.
    """
    matches = sum(1 for word in keywords if word.lower() in response.lower())
    return matches / len(keywords) if keywords else 0.0
