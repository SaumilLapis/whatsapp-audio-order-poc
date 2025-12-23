def confidence_score(clean_text: str, order) -> float:
    score = 0.5

    if order.product != "unknown":
        score += 0.25
    if order.quantity > 0:
        score += 0.15
    if order.unit:
        score += 0.10

    return round(min(score, 1.0), 2)
