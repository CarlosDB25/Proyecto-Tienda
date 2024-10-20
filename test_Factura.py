import unittest
from MODELO.Factura import Bill

class TestBill(unittest.TestCase):
    def test_crear_bill(self):
        bill = Bill("2024-10-15", 30000)
        self.assertEqual(bill.date, "2024-10-15")
        self.assertEqual(bill.total, 30000)

    def test_setters_bill(self):
        bill = Bill("2024-10-15", 30000)
        bill.date = "2024-10-20"
        bill.total = 35000
        self.assertEqual(bill.date, "2024-10-20")
        self.assertEqual(bill.total, 35000)

if __name__ == '__main__':
    unittest.main()
