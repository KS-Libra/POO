# Programación Orientada a Objetos (POO)

class ClimaSemanal:
    """
    Representa el clima de una semana y las operaciones asociadas.
    """
    def __init__(self):
        """
        Constructor de la clase. Inicializa los atributos.
        El guion bajo (_) indica que es un atributo "protegido" (encapsulamiento).
        """
        self._temperaturas = []
        self._dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def ingresar_temperaturas(self):
        """
        Método para solicitar y almacenar las temperaturas de la semana.
        Modifica el estado del objeto (su atributo _temperaturas).
        """
        print("\n--- Ingreso de Temperaturas (POO) ---")
        self._temperaturas = [] # Limpiamos la lista por si se reutiliza el objeto
        for dia in self._dias:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para el {dia}: "))
                    self._temperaturas.append(temp)
                    break
                except ValueError:
                    print("Error: Por favor, ingrese un número válido.")

    def calcular_promedio(self):
        """
        Método para calcular y devolver el promedio de las temperaturas almacenadas.
        Usa los datos internos del objeto.
        """
        if not self._temperaturas:
            return 0
        total = sum(self._temperaturas)
        return total / len(self._temperaturas)

    def mostrar_resumen(self):
        """
        Muestra un resumen completo del clima semanal.
        """
        promedio = self.calcular_promedio()
        print("\n--- Resultados (POO) ---")
        print(f"Las temperaturas de la semana fueron: {self._temperaturas}")
        print(f"El promedio semanal del clima es: {promedio:.2f}°C 🌡️")


# --- Ejecución del programa POO ---
print("\nIniciando método POO...")
# 1. Creamos una instancia (un objeto) de la clase ClimaSemanal
reporte_clima = ClimaSemanal()
# 2. Usamos los métodos del objeto para realizar las acciones
reporte_clima.ingresar_temperaturas()
reporte_clima.mostrar_resumen()