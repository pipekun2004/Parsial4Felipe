
stock_concepcion = 500
stock_puente_alto = 1300
stock_muelle_baron = 100
stock_muelle_vergara = 50

compradores_concepcion = set()
compradores_puente_alto = set()
compradores_baron = set()
compradores_vergara = set()

codigo_valido_concepcion = "Acceso123"

def menu():
    print("\nTOTEM AUTOSERVICIO GIRA LOS FORTIFICADOS ROCK AND CHILE IN CHILE")
    print("1.- Comprar entrada en Concepción.")
    print("2.- Comprar entrada en Puente Alto.")
    print("3.- Comprar entrada en Muelle Barón, Valparaíso.")
    print("4.- Comprar entrada en Muelle Vergara, Viña del Mar.")
    print("5.- Salir.")

while True:
    menu()
    opcion = input("Seleccione una opción: ").strip()

    if opcion == '1':
        print("-- Compra en Concepción --")
        if stock_concepcion <= 0:
            print("No hay stock disponible.")
            continue
        nombre = input("Nombre del comprador: ").strip()
        if nombre in compradores_concepcion:
            print("Error: nombre ya registrado.")
            continue
        codigo = input("Código de confirmación: ").strip()
        if codigo != codigo_valido_concepcion:
            print("Error: código de confirmación inválido.")
            continue
        compradores_concepcion.add(nombre)
        stock_concepcion -= 1
        print(f"Entrada registrada! Stock restante: {stock_concepcion}")

    elif opcion == '2':
        print("-- Compra en Puente Alto --")
        if stock_puente_alto <= 0:
            print("No hay stock disponible.")
            continue
        nombre = input("Nombre del comprador: ").strip()
        if nombre in compradores_puente_alto:
            print("Error: nombre ya registrado.")
            continue
        try:
            cantidad = int(input("Cantidad de entradas (máx 3): "))
        except ValueError:
            print("Error: debe ingresar un número.")
            continue
        if not (1 <= cantidad <= 3):
            print("Error: solo se permiten entre 1 y 3 entradas por persona.")
            continue
        if stock_puente_alto < cantidad:
            print("Error: no hay suficiente stock disponible.")
            continue
        compradores_puente_alto.add(nombre)
        stock_puente_alto -= cantidad
        print(f"Entradas registradas! Stock restante: {stock_puente_alto}")

    elif opcion == '3':
        print("-- Compra en Muelle Barón, Valparaíso --")
        if stock_muelle_baron <= 0:
            print("No hay stock disponible.")
            continue
        nombre = input("Nombre del comprador: ").strip()
        if nombre in compradores_baron:
            print("Error: nombre ya registrado.")
            continue
        compradores_baron.add(nombre)
        stock_muelle_baron -= 1
        print("Tipo de entrada asignado: G")
        print(f"Entrada registrada! Stock restante: {stock_muelle_baron}")

    elif opcion == '4':
        print("-- Compra en Muelle Vergara, Viña del Mar --")
        if stock_muelle_vergara <= 0:
            print("No hay stock disponible.")
            continue
        nombre = input("Nombre del comprador: ").strip()
        if nombre in compradores_vergara:
            print("Error: nombre ya registrado.")
            continue
        tipo = input("Tipo de entrada (Sun=Sunset, Ni=Night): ").strip().lower()
        if tipo not in ["sun", "ni"]:
            print("Error: tipo de entrada inválido.")
            continue
        compradores_vergara.add(nombre)
        stock_muelle_vergara -= 1
        print(f"Entrada registrada! Stock restante: {stock_muelle_vergara}")

    elif opcion == '5':
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opción válida!!")
