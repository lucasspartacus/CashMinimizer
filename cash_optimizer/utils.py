from typing import List

def breakdown_amount(amount: float, denominations: List[float]) -> List[float]:
    result = []
    remaining = round(amount, 2)
    for d in denominations:
        while remaining >= d - 1e-6:  
            result.append(d)
            remaining = round(remaining - d, 2)
    if abs(remaining) > 1e-6:
        return []  
    return result
