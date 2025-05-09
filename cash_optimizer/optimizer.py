from .utils import breakdown_amount
from typing import List, Tuple

def find_minimal_exchange(denominations: List[float], total_value: float, max_overpay: float = 1.00) -> Tuple[List[float], List[float]]:

    denominations = sorted(set(round(d, 2) for d in denominations), reverse=True)
    min_total_items = float('inf')
    best_payment, best_change = [], []

    for overpay_cents in range(0, int(max_overpay * 100) + 1):
        
        payment_amount = round(total_value + overpay_cents / 100, 2)
        payment = breakdown_amount(payment_amount, denominations)

        if not payment:
            continue

        change_amount = round(payment_amount - total_value, 2)
        change = breakdown_amount(change_amount, denominations) if change_amount > 0 else []
        total_items = len(payment) + len(change)
        
        if total_items < min_total_items:
            min_total_items = total_items
            best_payment, best_change = payment, change

    return best_payment, best_change