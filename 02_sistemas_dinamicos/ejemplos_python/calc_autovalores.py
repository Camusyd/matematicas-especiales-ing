# calc_autovalores.py
# Script de utilidad para calcular autovalores, autovectores y clasificar la estabilidad 
# de un sistema lineal homogéneo X' = A * X.
# Este script utiliza NumPy para el cálculo numérico.

import numpy as np
import sympy as sp

def calcular_propiedades(A):
    """
    Calcula autovalores, autovectores de la matriz A y clasifica el punto crítico (0,0) 
    basándose en la parte real de los autovalores (lambda).
    
    Args:
        A (list of lists): Matriz de coeficientes 2x2.
    """
    
    A_np = np.array(A, dtype=float)
    
    print("### Matriz de Coeficientes A ###")
    print(A_np)
    
    print("\n--- Resultados Numéricos (NumPy) ---")
    
    try:
        # np.linalg.eig devuelve (autovalores, autovectores)
        lambdas, K = np.linalg.eig(A_np)
        print(f"Autovalores (lambda): {lambdas}")
        print(f"Autovectores (K, columnas):\n{K}")
        
        # --- Clasificación del Punto Crítico (0,0) ---
        
        # 1. Caso Real (si ambas partes imaginarias son muy cercanas a cero)
        if np.all(np.isreal(lambdas)):
            lambda1 = lambdas[0]
            lambda2 = lambdas[1]
            
            if lambda1 * lambda2 < 0:
                # Signos opuestos
                print("Clasificación: Punto de Silla (Inestable)")
            elif lambda1 > 0 and lambda2 > 0:
                # Ambos positivos
                print("Clasificación: Nodo Inestable")
            elif lambda1 < 0 and lambda2 < 0:
                # Ambos negativos
                print("Clasificación: Nodo Estable")
            elif np.isclose(lambda1, lambda2):
                # Raíces repetidas
                print("Clasificación: Nodo con Raíces Repetidas")
                
        # 2. Caso Complejo (raíces conjugadas)
        else:
            # Tomamos la parte real del primer autovalor complejo
            alpha = np.real(lambdas[0])
            
            if np.isclose(alpha, 0):
                # Parte real nula
                print("Clasificación: Centro (Marginalmente Estable)")
            elif alpha > 0:
                # Parte real positiva
                print("Clasificación: Foco Inestable")
            else:
                # Parte real negativa
                print("Clasificación: Foco Estable")
                
    except np.linalg.LinAlgError:
        print("Error: No se pudo calcular autovalores/autovectores.")


# --- PRUEBAS DE LA FUNCIÓN ---

# Ejemplo 1: Foco Estable (Autovalores: -1 +/- i)
A_ejemplo_foco = [[-1, 1], [-1, -1]]
print("\n" + "="*40)
print("--- ANALIZANDO FOCO ESTABLE (Espiral hacia adentro) ---")
calcular_propiedades(A_ejemplo_foco)
print("="*40)


# Ejemplo 2: Centro (Autovalores: +/- i)
# El caso del examen que resulta en órbitas circulares.
A_ejemplo_centro = [[0, 1], [-1, 0]]
print("\n" + "="*40)
print("--- ANALIZANDO CENTRO (Órbitas cerradas) ---")
calcular_propiedades(A_ejemplo_centro)
print("="*40)


# Ejemplo 3: Punto de Silla (Autovalores: 3, -1)
A_ejemplo_silla = [[1, 1], [4, 1]]
print("\n" + "="*40)
print("--- ANALIZANDO PUNTO DE SILLA (Inestable) ---")
calcular_propiedades(A_ejemplo_silla)
print("="*40)