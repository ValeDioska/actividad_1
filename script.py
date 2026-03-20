import numpy as np
import matplotlib.pyplot as plt
import csv

def resolver_sistema():
    print("Resolviendo un sistema de ecuaciones lineales...")

    #Definir una matriz de coeficentes y un vector de términos independientes
    A = np.array([[3, 1, -1], [2, 4, 1], [-1, 2, 5]])
    b = np.array([4, 1, 1])

    #Resolver el sistema Ax = b
    try:
        x = np.linalg.solve(A, b)
        print("La solución del sistema es:")
        for i, valor in enumerate(x):
            print(f"x{i} = {valor:4f}"):
        return x
    except np.linalg.LinAlgError:
        print("El sistema no tiene solución única.")
        return None

def graficar_solucion(soluciones):
    if soluciones is not None:
        etiquetas = [f"x{i}" for i in range(1, len(soluciones) + 1)]
        plt.bar(etiquetas, soluciones, color='blue', 'green', 'red')
        plt.title("Solución del Sistema de Ecuaciones")
        plt.xlabel("Variables")
        plt.ylabel("Valores")
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Guardar la gráfica como imagen
        plt.savefig("solucion_sistema.png")
        plit.close()
        print("Gráfica guardada como 'solucion_sistema.png'")
    else:
        print("No se puede graficar la solución debido a que no existe una solución única.")

def guardar_solucion_csv(soluciones):
    if soluciones is not None:
        print("Guardando la solución en un archivo CSV...")

        #Escribir la solución en un archivo CSV
        with open('solucion_sistema.csv', mode='w', newline='') as file:
            escritor = csv.writer(archivo)
            escritor.writerow(["Variable", "Valor"])
            for i, valor in enumerate(soluciones, start=1):
                escritor.writerow([f"x{i}", f"{valor:4f}"])
        print("Solución guardada en 'solucion_sistema.csv'")
    else:     
        print("No se puede guardar la solución en un archivo CSV debido a que no existe una solución única.")

def main():
    print("Bienvenido al programa de resolución de sistemas de ecuaciones lineales.")

    #Resolver el sistema
    soluciones = resolver_sistema()

    #Graficar la solución
    graficar_solucion(soluciones)

    #Guardar la solución en un archivo CSV
    guardar_solucion_csv(soluciones)

if __name__ == "__main__":
    main()
    