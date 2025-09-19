class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = "" # Es mejor inicializarlo como string vacío
    
    # Método para leer los dos números de la potencia
    def leerNumerosParaPotencia(self):
        print("\n--- Calculando Potencia ---")
        while True:
            try:
                self.num1 = int(input("Introduce el número base: "))
                break
            except ValueError:
                print("Error: Número inválido")
        while True:
            try:
                self.num2 = int(input("Introduce el exponente: "))
                break
            except ValueError:
                print("Error: Número inválido")

    # NUEVO método para leer solo un número para la raíz
    def leerNumeroParaRaiz(self):
        print("\n--- Calculando Raíz Cuadrada ---")
        while True:
            try:
                # Usaremos num1 para guardar el valor de la raíz
                self.num1 = int(input("Introduce el número para la raíz: "))
                break
            except ValueError:
                print("Error: Número inválido")
    
    def potencia(self):
        # f-string hace el código más limpio
        self.resultado = f"La potencia de {self.num1} ^ {self.num2} es igual a {self.num1 ** self.num2}"

    def raiz_cuadrada(self):
        if self.num1 < 0:
            self.resultado = "Error: No se puede calcular la raíz de un número negativo."
        else:
            self.resultado = f"La raíz cuadrada de √{self.num1} es igual a {self.num1 ** 0.5}"
    
    def mostrarResultado(self):
        print(self.resultado)