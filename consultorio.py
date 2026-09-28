# 1 Datos constantes - Tabla precios
VALOR_CITA = {
    "Particular":80000,
    "EPS": 5000,
    "Prepagada":30000
}

VALOR_ATENCION = {
    "Particular":{"Limpieza":60000, "Calzas":80000, "Extraccion":100000, "Diagnostico":50000},
    "EPS":{"Limpieza":0, "Calzas":40000, "Extraccion":40000, "Diagnostico":0},
    "Prepagada":{"Limpieza":0, "Calzas":10000, "Extraccion":10000, "Diagnostico":0}
}

#Arreglo donde se guardaran todos los clientes registrados
clientes = []

# 2 Funciones para leer los datos de un cliente
def pedir_tipo_cliente():
    """Muestra un menú y obliga a elegir una opción válida"""
    print("\nTipo de cliente:")
    print("1. Particular")
    print("2. EPS")
    print("3. Prepagada")
    opcion = input("Elija una opción (1-3): ")

    if opcion == "1":
        return "Particular"
    elif opcion =="2":
        return "EPS"
    elif opcion == "3":
        return "Prepagada"
    else:
        print ("Opción inválida, se asignará 'Particular' por defecto.")
        return "Particular"

def pedir_tipo_atencion():
    """Muestra un menú y obliga a elegir una opción válida"""
    print("\nTipo de Atención:")
    print("1. Limpieza")
    print("2. Calzas")
    print("3. Extracción")
    print ("4. Diagnostico")
    opcion = input ("Elija una opción (1-4): ")

    if opcion == "1":
        return "Limpieza"
    elif opcion == "2":
        return "Calzas"
    elif opcion == "3":
        return "Extracción"
    elif opcion == "4":
        return "Diagnóstico"
    else: 
        print ("Opción inválida, se asignará 'Limpieza' por defecto.")
        return "Limpieza"

def pedir_cantidad(tipo_atencion):
    if tipo_atencion in ("Limpieza", "Diagnostico"):
        print(f"La cantidad para {tipo_atencion} es siempre 1.")
        return 1
    else:
        cantidad = int(input(f"Ingrese la cantidad de {pedir_tipo_cliente} (mayor que 0): "))
        while cantidad <= 0:
            cantidad = int (input("La cantidad debe ser mayor que 0. Ingrese de nuevo: "))
    return cantidad

def pedir_prioridad():
    print("\nPrioridad de la atención: ")
    print("Normal")
    print("Urgente")
    opcion = input("Elija una prioridad: ")

    if opcion == "1":
        return "Normal"
    else:
        return "Urgente"

def calcular_valor_total(tipo_cliente, tipo_atencion, cantidad):
    valor_cita = VALOR_CITA [tipo_cliente]
    valor_atencion_unit = VALOR_ATENCION [tipo_cliente][tipo_atencion]
    valor_total = valor_cita + (valor_atencion_unit * cantidad)
    return valor_cita, valor_atencion_unit, valor_total

def registrar_cliente():
    """Lee todos los datos de UN cliente y los guarda en un diccionario."""
    print("\n----- REGISTRO DE CLIENTE -----")
    cedula = input("Cédula: ")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    tipo_cliente = pedir_tipo_cliente()
    tipo_atencion = pedir_tipo_atencion()
    cantidad = pedir_cantidad(tipo_atencion)
    prioridad = pedir_prioridad()
    fecha_cita = input("Fecha de la cita (dd/mm/aaaa): ")
 
    valor_cita, valor_atencion_unit, valor_total = calcular_valor_total(
        tipo_cliente, tipo_atencion, cantidad
    )
 
    # Un diccionario representa "un registro" de la tabla de clientes.
    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_cliente": tipo_cliente,
        "tipo_atencion": tipo_atencion,
        "cantidad": cantidad,
        "prioridad": prioridad,
        "fecha_cita": fecha_cita,
        "valor_cita": valor_cita,
        "valor_atencion_unit": valor_atencion_unit,
        "valor_total": valor_total
    }
 
    print(f"\n>> Valor total a pagar por {nombre}: ${valor_total:,}")
    return cliente

#3 Arreglo para calculos sobre todos los clientes

def calcular_totales(lista_clientes):
    total_clientes = len(lista_clientes)

    ingresos_totales = 0
    for c in lista_clientes:
        ingresos_totales += c["valor_total"]

    clientes_extraccion = 0 
    for c in lista_clientes:
        if c["tipo_atencion"] == "Extraccion":
            clientes_extraccion += 1

    return total_clientes, ingresos_totales, clientes_extraccion
    
#4 ordenar la lista

def ordenar_por_valor_atencion(lista_clientes):
    n = len(lista_clientes)
    for i in range(n - 1):
        for j in range (n - 1 - i):
            if lista_clientes[j]["valor_atencion_unit"] < lista_clientes[j + 1]["valor_atencion_unit"]:
                lista_clientes[j], lista_clientes[j + 1] = lista_clientes[j + 1], lista_clientes[j]
    return lista_clientes

#5 Buscar cliente por cédula

def buscar_por_cedula(lista_clientes, cedula_buscada):
    for c in lista_clientes:
        if c["cedula"] == cedula_buscada:
            return c
    return None

#6 Mostrar resultados en pantalla

def mostrar_lista(lista_clientes, titulo="LISTA DE CLIENTES"):
    print(f"\n===== {titulo} =====")
    for c in lista_clientes:
        print(f"Cédula: {c['cedula']} | Nombre: {c['nombre']} | "
              f"Atención: {c['tipo_atencion']} | Valor Atención: ${c['valor_atencion_unit']:,} | "
              f"Total a pagar: ${c['valor_total']:,}")
 
#7 Programa principal

def main():
    print("=== SISTEMA DE CITAS - CONSULTORIO ODONTOLÓGICO ===")
    cantidad_clientes = int(input("¿Cuántos clientes desea registrar?: "))
 
    for i in range(cantidad_clientes):
        nuevo_cliente = registrar_cliente()
        clientes.append(nuevo_cliente)  # Guardamos en el arreglo
 
    mostrar_lista(clientes, "CLIENTES REGISTRADOS (orden de ingreso)")
 
    total, ingresos, extracciones = calcular_totales(clientes)
    print("\n===== RESUMEN GENERAL =====")
    print(f"1. Total de clientes atendidos: {total}")
    print(f"2. Ingresos totales recibidos: ${ingresos:,}")
    print(f"3. Clientes que van para extracción: {extracciones}")
 
    ordenar_por_valor_atencion(clientes)
    mostrar_lista(clientes, "CLIENTES ORDENADOS POR VALOR DE ATENCIÓN (MAYOR A MENOR)")
 
    cedula_buscar = input("\nIngrese la cédula que desea buscar: ")
    resultado = buscar_por_cedula(clientes, cedula_buscar)
 
    if resultado:
        print("\n¡Cliente encontrado!")
        print(resultado)
    else:
        print("\nNo se encontró ningún cliente con esa cédula.")
 
 
# Este bloque asegura que main() solo se ejecute si corremos
# este archivo directamente (buena práctica en Python).
if __name__ == "__main__":
    main()