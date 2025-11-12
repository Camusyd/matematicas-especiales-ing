# plot_plano_fase.py
# Script para generar el Retrato de Fase de un sistema lineal 2x2.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp # Importación necesaria para solve_ivp

# --- CORRECCIÓN CRÍTICA: MANEJO DE DIMENSIONES (soluciona ValueError) ---
def sistema_lineal(t, X, A):
    """
    Calcula el vector de derivadas X' = A * X.
    Asegura que X (vector de estado) se redimensione para la multiplicación matricial.
    """
    
    # X viene de solve_ivp como un array 1D (ej: [x1, x2]). Lo convertimos a columna (2, 1).
    X_columna = X.reshape(-1, 1) 
    
    # Multiplicación matricial (A @ X_columna)
    derivadas = A @ X_columna
    
    # Devolver el resultado como un array 1D plano para solve_ivp.
    return derivadas.flatten() 

def plot_plano_fase(A, x_range, y_range, title="Retrato de Fase de Sistema Lineal"):
    """Dibuja el campo vectorial y algunas trayectorias."""
    
    # 1. Definición de la malla y el campo vectorial
    X, Y = np.meshgrid(np.arange(x_range[0], x_range[1], 0.3),
                       np.arange(y_range[0], y_range[1], 0.3))
    
    U = np.zeros_like(X)
    V = np.zeros_like(Y)
    
    ni, nj = X.shape
    for i in range(ni):
        for j in range(nj):
            x_val = X[i, j]
            y_val = Y[i, j]
            
            X_vector = np.array([x_val, y_val])
            
            # Llamada segura: t=0 es irrelevante para sistemas homogéneos.
            derivadas = sistema_lineal(0, X_vector, A) 
            
            U[i, j] = derivadas[0]
            V[i, j] = derivadas[1]

    # Normalización del campo vectorial para flechas uniformes
    N = np.sqrt(U**2 + V**2)
    N[N == 0] = 1 
    U = U / N
    V = V / N

    # 2. Plotting
    plt.figure(figsize=(8, 8))
    
    # Dibujar el campo vectorial (flechas)
    plt.quiver(X, Y, U, V, N, cmap='viridis', headlength=7, headwidth=4, alpha=0.8)
    
    # 3. Dibujar algunas trayectorias (soluciones numéricas)
    t_span = 10 # Tiempo máximo de integración
    t = np.linspace(-t_span, t_span, 100) 
    
    condiciones_iniciales = [
        [1, 1], [-1, 1], [1, -1], [-1, -1], [2, 0], [0, 2]
    ]
    
    for x0 in condiciones_iniciales:
        # Integra hacia adelante (t positivo)
        sol_fwd = solve_ivp(sistema_lineal, [0, t_span], x0, args=(A,), dense_output=True)
        Z_fwd = sol_fwd.sol(t[t >= 0])
        plt.plot(Z_fwd[0], Z_fwd[1], 'r-', linewidth=1.5, alpha=0.7)
        
        # Integra hacia atrás (t negativo)
        sol_bwd = solve_ivp(sistema_lineal, [0, -t_span], x0, args=(A,), dense_output=True)
        Z_bwd = sol_bwd.sol(t[t < 0])
        plt.plot(Z_bwd[0], Z_bwd[1], 'r-', linewidth=1.5, alpha=0.7)


    plt.axhline(0, color='gray', linestyle='--')
    plt.axvline(0, color='gray', linestyle='--')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title(title)
    plt.xlim(x_range)
    plt.ylim(y_range)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()

# --- Ejemplo de Uso (Foco Inestable) ---
A_ejemplo = np.array([[0.5, 1], [-1, 0.5]])
x_lim = (-3, 3)
y_lim = (-3, 3)

# --- CORRECCIÓN DE SINTAXIS: Usar raw string (r"...") ---
plot_plano_fase(A_ejemplo, x_lim, y_lim, r"Foco Inestable ($\lambda = 0.5 \pm i$)")
