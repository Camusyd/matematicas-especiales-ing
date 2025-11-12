# plot_transformacion.py
# Script para visualizar la transformación de un dominio del plano z al plano w
# mediante una función analítica simple, como w = z^2.

import numpy as np
import matplotlib.pyplot as plt

# Definición de la función de transformación (w = f(z))
def f_z(z):
    """Ejemplo de función analítica: f(z) = z^2"""
    return z**2

# --- 1. Definición del Dominio (Malla) en el Plano Z ---

# Líneas horizontales (y=constante) y verticales (x=constante)
x_lines = np.linspace(0.5, 2.5, 5) # Valores fijos de x (verticales)
y_lines = np.linspace(0.5, 2.5, 5) # Valores fijos de y (horizontales)
num_puntos = 100 # Número de puntos para dibujar cada línea

plt.figure(figsize=(12, 6))

# --- PLOT 1: Plano Z (Dominio) ---
plt.subplot(1, 2, 1)
plt.title('Plano Z (Dominio)')
plt.xlabel('Re(z) = x')
plt.ylabel('Im(z) = y')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.6)

# Dibujar líneas verticales (x = constante) en el plano Z
for x0 in x_lines:
    y_vals = np.linspace(y_lines.min(), y_lines.max(), num_puntos)
    z_vals = x0 + 1j * y_vals
    plt.plot(z_vals.real, z_vals.imag, 'b-', alpha=0.7)
    
# Dibujar líneas horizontales (y = constante) en el plano Z
for y0 in y_lines:
    x_vals = np.linspace(x_lines.min(), x_lines.max(), num_puntos)
    z_vals = x_vals + 1j * y0
    plt.plot(z_vals.real, z_vals.imag, 'r-', alpha=0.7)

plt.axis('equal') # Para mantener la proporción cuadrada

# --- PLOT 2: Plano W (Imagen) ---
plt.subplot(1, 2, 2)
plt.title(f'Plano W (Imagen) bajo $w = f(z) = z^2$')
plt.xlabel('Re(w) = u')
plt.ylabel('Im(w) = v')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.6)

# Dibujar las líneas transformadas en el plano W

# Líneas originales verticales (x = constante) -> w(t) = (x0^2 - t^2) + i(2*x0*t)
for x0 in x_lines:
    y_vals = np.linspace(y_lines.min(), y_lines.max(), num_puntos)
    z_vals = x0 + 1j * y_vals
    w_vals = f_z(z_vals) # Aplicar la transformación
    plt.plot(w_vals.real, w_vals.imag, 'b-', alpha=0.7)

# Líneas originales horizontales (y = constante) -> w(t) = (t^2 - y0^2) + i(2*t*y0)
for y0 in y_lines:
    x_vals = np.linspace(x_lines.min(), x_lines.max(), num_puntos)
    z_vals = x_vals + 1j * y0
    w_vals = f_z(z_vals) # Aplicar la transformación
    plt.plot(w_vals.real, w_vals.imag, 'r-', alpha=0.7)

plt.axis('equal') 
plt.tight_layout()
plt.show()

#