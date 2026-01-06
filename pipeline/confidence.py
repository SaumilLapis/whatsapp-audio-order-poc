CONFIDENCE_THRESHOLD = 0.75

def compute_confidence(raw_text: str, clean_text: str, order) -> dict:
    """
    Deterministic, explainable confidence calculation.

    Confidence is penalized when:
    - ASR ambiguity is detected
    - Product is unknown
    - Quantity is inferred or unclear
    """

    score = 1.0
    reasons = []

    if "free" in raw_text.lower():
        score -= 0.2
        reasons.append("ASR ambiguity detected (free vs three)")

    if order.product == "unknown":
        score -= 0.3
        reasons.append("Unknown product")

    if order.quantity <= 0:
        score -= 0.2
        reasons.append("Quantity inferred or missing")

    score = round(max(score, 0.0), 2)

    routing = (
        "auto_process"
        if score >= CONFIDENCE_THRESHOLD
        else "needs_human_review"
    )

    return {
        "confidence": score,
        "routing": routing,
        "review_reason": reasons if routing == "needs_human_review" else None,
    }
