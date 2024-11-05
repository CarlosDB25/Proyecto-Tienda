import unittest
from unittest.mock import patch
from datetime import datetime
from MODELO.Cliente import Client
from MODELO.Factura import Bill
from MODELO.Tienda import Store
from CRUD.crud import Crud, getDate, getPrices

class TestCrud(unittest.TestCase):
    
    def test_getDate(self):
        """Prueba que getDate devuelva la fecha en el formato correcto."""
        with patch('CRUD.crud.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2024, 10, 27, 15, 30, 45)
            self.assertEqual(getDate(), "2024-10-27 15:30:45")
    
    def test_getPrices(self):
        """Prueba que getPrices devuelva una lista de precios de productos."""
        products = [Bill("2024-10-27", 100, [{'name': 'Producto A', 'price': 100}]),
                    Bill("2024-10-28", 200, [{'name': 'Producto B', 'price': 200}])]
        prices = getPrices([{'name': product.products[0]['name'], 'price': product.products[0]['price']} for product in products])
        self.assertEqual(prices, [100, 200])

    def test_createBill(self):
        """Prueba que createBill cree correctamente una factura con fecha, total y productos."""
        crud = Crud()
        products = [{'name': 'Producto A', 'price': 100}, {'name': 'Producto B', 'price': 200}]
        
        with patch('CRUD.crud.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2024, 10, 27, 15, 30, 45)
            bill_data = crud.createBill(products)
            self.assertEqual(bill_data['date'], "2024-10-27 15:30:45")
            self.assertEqual(bill_data['total'], 300)
            self.assertEqual(bill_data['products'], products)
    
    def test_createClient(self):
        """Prueba que createClient cree correctamente un cliente con sus datos y facturas."""
        crud = Crud()
        client_data = ["Juan Pérez", "12345", Bill("2024-10-27", 300, [{'name': 'Producto A', 'price': 100}])]
        client = crud.createClient(client_data)
        
        self.assertEqual(client['name'], "Juan Pérez")
        self.assertEqual(client['id'], "12345")
        self.assertEqual(len(client['bills']), 1)
        self.assertEqual(client['bills'][0].date, "2024-10-27")
    
    def test_showBill(self):
        """Prueba que showBill imprima correctamente una factura."""
        crud = Crud()
        bill = Bill("2024-10-27", 300, [{'name': 'Producto A', 'price': 100}])
        
        with patch('builtins.print') as mock_print:
            crud.showBill(bill)
            mock_print.assert_called_with("Fecha: 2024-10-27\nProductos: ['Producto A']\nTotal: 300\n")
    
    def test_showBills(self):
        """Prueba que showBills imprima todas las facturas de un cliente o muestre un mensaje si no existen."""
        crud = Crud()
        client = Client("Juan Pérez", "12345", [
            Bill("2024-10-27", 300, [{'name': 'Producto A', 'price': 100}])
        ])
        
        StoreA = Store([client])
        
        with patch('builtins.print') as mock_print:
            crud.showBills("12345", StoreA)
            mock_print.assert_any_call("Fecha: 2024-10-27\nProductos: ['Producto A']\nTotal: 300\n")
    
    def test_searchBillById(self):
        """Prueba que searchBillById encuentre el cliente correcto o devuelva None si no existe."""
        crud = Crud()
        client1 = Client("Juan Pérez", "12345", [])
        client2 = Client("Ana García", "67890", [])
        store = Store([client1, client2])
        
        # Verifica que encuentre el cliente correcto
        client, found = crud.searchBillById("12345", store)
        self.assertTrue(found)
        self.assertEqual(client.id, "12345")
        
        # Verifica que devuelva None si el cliente no existe
        client, found = crud.searchBillById("11111", store)
        self.assertFalse(found)
        self.assertIsNone(client)

if __name__ == '__main__':
    unittest.main()
