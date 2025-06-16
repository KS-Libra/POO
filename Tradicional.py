# Programación Tradicional

def ingresar_temperaturas_diarias():
    """
    Solicita al usuario las temperaturas de cada día de la semana.
    Devuelve una lista con las 7 temperaturas.
    """
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    print("--- Ingreso de Temperaturas (Tradicional) ---")
    for dia in dias:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura para el {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio_semanal(lista_temps):
    """
    Calcula el promedio de una lista de temperaturas.
    Devuelve el promedio.
    """
    if not lista_temps:
        return 0
    total = sum(lista_temps)
    promedio = total / len(lista_temps)
    return promedio

# --- Ejecución del programa tradicional ---
print("Iniciando método tradicional...")
# 1. Obtenemos los datos
temps_semana = ingresar_temperaturas_diarias()
# 2. Calculamos el promedio con los datos obtenidos
promedio_final = calcular_promedio_semanal(temps_semana)

print("\n--- Resultados (Tradicional) ---")
print(f"Las temperaturas de la semana fueron: {temps_semana}")
print(f"El promedio semanal del clima es: {promedio_final:.2f}°C 🌡️")