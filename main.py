from MODELO.Cliente import Client
from MODELO.Factura import Bill

def main():
    # Crear un cliente
    cliente = Client("Juan Pérez", "123456")

    # Crear facturas
    factura1 = Bill("2024-10-01", 150.00)
    factura2 = Bill("2024-10-15", 200.00)

    # Agregar facturas al cliente
    cliente.bills.append(factura1)
    cliente.bills.append(factura2)

    # Aquí establece un punto de interrupción
    # para inspeccionar el objeto cliente y sus facturas
    print("Cliente creado:", cliente.name)
    print("Facturas del cliente:")
    for bill in cliente.bills:
        print(f"Fecha: {bill.date}, Total: {bill.total}")

if __name__ == "__main__":
    main()