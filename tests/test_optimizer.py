
from cash_optimizer.optimizer import find_minimal_exchange
import unittest

class TestCashOptimizer(unittest.TestCase):
    def test_us_cash(self):

        payment_amount = 19.96
        denominations = [0.01, 0.05, 0.10, 0.25, 1, 5, 10, 20, 50, 100]
        payment_made, change = find_minimal_exchange(denominations, payment_amount)
        self.assertEqual(sum(payment_made) - sum(change), round(payment_amount, 2))
        self.assertEqual(len(payment_made) + len(change), 3) 

if __name__ == '__main__':
    unittest.main()