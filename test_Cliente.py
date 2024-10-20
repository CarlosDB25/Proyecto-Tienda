import unittest
from MODELO.Cliente import Client

class TestClient(unittest.TestCase):
    def test_crear_client(self):
        client = Client("Juan Pérez", "12345678")
        self.assertEqual(client.name, "Juan Pérez")
        self.assertEqual(client.id, "12345678")
        self.assertEqual(client.bills, [])

    def test_agregar_factura(self):
        client = Client("Juan Pérez", "12345678")
        client.bills = ["Factura 1", "Factura 2"]
        self.assertEqual(client.bills, ["Factura 1", "Factura 2"])

if __name__ == '__main__':
    unittest.main()
