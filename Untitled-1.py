while True:
    import re
    Concepción = 500
    PuenteAlto = 1300
    MuelleBarónenValparaíso = 100
    enMuelleVergaraenViñadelMar = 50
    nombres_ingresados = set()

    def agregar_nombre(nombre):
        if nombre not in nombres_ingresados:
            nombres_ingresados.add(nombre)
        print("TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
        print("1.- Comprar entrada a “los Fortificados” en Concepción.")
        print("2.- Comprar entrada a “los Fortificados” en Puente Alto.")
        print("3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.")
        print("4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.")
        print("5.- Salir.")
        try:
            opcion = int(input("seleccione una opcion: "))

            if opcion == 1:
                nombre = input("ingrese su nombre: ")
                input("ingrese su codigo de confirmacion:")
                print("se a confirmado la compra: ")
            
            elif opcion == 2:
                nombre = input("ingrese su nombre:")
                int(input("Cantidad de entradas (máx 3):"))

            elif opcion == 3:
                nombre =input("ingrese su nombre:")
                input("seleceione el tipo de entrada")

            elif opcion == 4:
                nombre =input("ingrese su nombre:")
                input("Tipo de entrada (Sun=Sunset, Ni=Night):")

            elif opcion == 5:
                print("progrma terminado...")
                break
            else:
                print("seleccione una opcion valida")
        except:
            print("ingrese un valor numerico")