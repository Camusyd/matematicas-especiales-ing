# serie_fourier_convergencia.py
# Simulación de la convergencia de la Serie de Fourier para una Onda Cuadrada
# Muestra el Fenómeno de Gibbs en las discontinuidades.

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de la Onda Cuadrada
# f(t) = 1 si 0 < t < pi, -1 si -pi < t < 0. Periodo T=2*pi, L=pi.
def onda_cuadrada_original(t_vals):
    """Función real de la Onda Cuadrada con periodo 2*pi."""
    # Usamos la función signo, ajustada para el periodo 2*pi
    # La función np.sign maneja los valores en las discontinuidades.
    periodo = 2 * np.pi
    t_mod = np.mod(t_vals + np.pi, periodo) - np.pi # Mapea t al intervalo [-pi, pi]
    
    f_t = np.sign(t_mod)
    
    # En las discontinuidades (t_mod = -pi, 0, pi), el valor es 0, que es el punto medio.
    return f_t

# Definición de la suma parcial de la Serie de Fourier para la Onda Cuadrada
def suma_parcial_fourier(t_vals, N_terms):
    """
    Calcula la suma parcial de la Serie de Fourier para la Onda Cuadrada:
    f(t) ~ SUM[n=1, n impar]^N (4/(n*pi) * sin(n*t))
    """
    total_sum = np.zeros_like(t_vals, dtype=float)
    
    # Iteramos solo sobre n impar
    for n_val in range(1, N_terms * 2, 2):  # n = 1, 3, 5, ...
        # Calculamos el coeficiente bn = 4 / (n*pi)
        bn = 4 / (n_val * np.pi)
        
        # Sumamos el término: bn * sin(n*t)
        total_sum += bn * np.sin(n_val * t_vals)
        
    return total_sum

# --- 1. Configuración de la Simulación ---
T_periodo = 2 * np.pi
t_array = np.linspace(-3 * T_periodo / 2, 3 * T_periodo / 2, 800) # Rango de -3pi a 3pi

# Número de términos para las aproximaciones
N_1 = 5     # Pocos términos
N_2 = 20    # Términos intermedios
N_3 = 100   # Muchos términos (para ver el Fenómeno de Gibbs claramente)

# --- 2. Cálculo de las Sumas Parciales ---
f_original = onda_cuadrada_original(t_array)
f_approx_1 = suma_parcial_fourier(t_array, N_1)
f_approx_2 = suma_parcial_fourier(t_array, N_2)
f_approx_3 = suma_parcial_fourier(t_array, N_3)

# --- 3. Visualización de la Convergencia y Gibbs ---

plt.figure(figsize=(10, 7))

# Trazar la función original
plt.plot(t_array, f_original, 'k--', linewidth=1, label='Onda Cuadrada Original', alpha=0.7)

# Trazar las aproximaciones
plt.plot(t_array, f_approx_1, label=f'Suma parcial (N={N_1} términos)', alpha=0.8)
plt.plot(t_array, f_approx_2, label=f'Suma parcial (N={N_2} términos)', alpha=0.8)
plt.plot(t_array, f_approx_3, label=f'Suma parcial (N={N_3} términos)', alpha=0.9, linewidth=1.5)

plt.title('Convergencia de la Serie de Fourier y Fenómeno de Gibbs')
plt.xlabel('Tiempo $t$ (rad)')
plt.ylabel('$f_N(t)$')
plt.ylim(-1.5, 1.5)
plt.legend(loc='lower right')
plt.axhline(1.089, color='r', linestyle=':', linewidth=0.8, label='Overshoot de Gibbs (aprox. 1.089)')
plt.axhline(-1.089, color='r', linestyle=':', linewidth=0.8)

plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

#