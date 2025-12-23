from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    product: str
    quantity: int
    unit: Optional[str]

def extract_order(text: str) -> Order:
    """
    Very simple rule-based extractor for PoC
    Example input:
    'i need 3 pallets of cement'
    """
    words = text.split()

    quantity = next((int(w) for w in words if w.isdigit()), 1)
    product = "cement" if "cement" in words else "unknown"
    unit = "pallets" if "pallet" in words else None

    return Order(
        product=product,
        quantity=quantity,
        unit=unit,
    )
