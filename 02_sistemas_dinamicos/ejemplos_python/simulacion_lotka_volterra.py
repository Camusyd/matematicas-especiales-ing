# simulacion_lotka_volterra.py
# Script para simular el Modelo Lotka-Volterra (Presa-Depredador) y visualizar su dinámica.

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Definición del Modelo y Parámetros ---

# Parámetros del modelo Lotka-Volterra:
# x: Población de Presa (e.g., Conejos)
# y: Población de Depredador (e.g., Zorros)
alpha = 1.0   # Tasa de crecimiento de la presa (nacimientos)
beta = 0.1    # Tasa de depredación (encuentros que resultan en muerte de la presa)
gamma = 1.5   # Tasa de mortalidad del depredador (muertes naturales)
delta = 0.075 # Tasa de reproducción del depredador (reproducción por comida)

def lotka_volterra(t, X):
    """
    Define las EDOs acopladas del modelo Lotka-Volterra.
    
    dX/dt = f(t, X)
    X = [x (presa), y (depredador)]
    """
    x, y = X
    
    # EDO para la Presa (x): Crecimiento natural - Depredación
    dxdt = alpha * x - beta * x * y
    
    # EDO para el Depredador (y): Muerte natural + Crecimiento por depredación
    dydt = delta * x * y - gamma * y
    
    return [dxdt, dydt]

# --- 2. Simulación Numérica ---

# Condiciones iniciales [x0 (presas), y0 (depredadores)]
X0 = [30, 10]
t_span = (0, 100)  # Intervalo de tiempo de simulación
t_puntos = np.linspace(t_span[0], t_span[1], 500) # Puntos de tiempo para la evaluación

print("Iniciando simulación numérica del modelo Lotka-Volterra...")

# Resolver el sistema de EDOs numéricamente
# solve_ivp usa un método Runge-Kutta para aproximar la solución
sol = solve_ivp(lotka_volterra, t_span, X0, t_eval=t_puntos, method='RK45')

x_t = sol.y[0]
y_t = sol.y[1]

# --- 3. Visualización de Resultados ---

# 3.1. Gráfico de Población vs. Tiempo
plt.figure(figsize=(12, 6))
plt.plot(t_puntos, x_t, label='Presa (x)', color='blue')
plt.plot(t_puntos, y_t, label='Depredador (y)', color='red')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.title('Dinámica Poblacional del Modelo Lotka-Volterra vs. Tiempo')
plt.legend()
plt.grid(True)
plt.show()

# 3.2. Retrato de Fase (y vs. x)
# Muestra la relación cíclica entre las dos poblaciones.
plt.figure(figsize=(8, 8))
plt.plot(x_t, y_t, 'b-', linewidth=1.5) 
plt.plot(x_t[0], y_t[0], 'go', markersize=8, label='Inicio (t=0)')

# Cálculo de los puntos de equilibrio (estacionarios)
# x* = gamma / delta ; y* = alpha / beta
x_eq = gamma / delta
y_eq = alpha / beta

plt.plot(x_eq, y_eq, 'k*', markersize=10, label=f'Equilibrio ({x_eq:.1f}, {y_eq:.1f})')
plt.xlabel('Población de Presa (x)')
plt.ylabel('Población de Depredador (y)')
plt.title('Retrato de Fase de Lotka-Volterra: Ciclo Límite')
plt.axvline(x_eq, color='gray', linestyle='--')
plt.axhline(y_eq, color='gray', linestyle='--')
plt.legend()
plt.grid(True)
plt.show()
#