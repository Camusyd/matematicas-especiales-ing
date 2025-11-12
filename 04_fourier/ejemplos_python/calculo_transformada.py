# calculo_transformada.py
# Utilidad basada en SymPy para calcular y obtener el resultado simbólico 
# de la Transformada de Fourier (FT).

import sympy as sp
from sympy.abc import t, k, a

# Definimos las variables con suposiciones que facilitan la simplificación
# K: variable de frecuencia (dominio espectral). A: constante positiva.
t = sp.Symbol('t', real=True)
k = sp.Symbol('k', real=True)
a = sp.Symbol('a', positive=True, real=True) 

# Definición de la convención de FT a utilizar (Integral de la FT Inversa de SymPy)
# SymPy tiene múltiples convenciones; usaremos la convención donde:
# F(k) = Integral( f(t) * exp(-i*k*t) dt )

# Función para calcular la transformada usando integración directa
def calcular_ft_directa(f_t, var_t=t, var_k=k):
    """
    Calcula la Transformada de Fourier F(k) = Integral(f(t) * exp(-i*k*t) dt) 
    usando integración directa con SymPy.
    """
    # Integrando: f(t) * exp(-i * k * t)
    integrando = f_t * sp.exp(-sp.I * var_k * var_t)
    
    # Integración de -infinito a infinito
    F_k_integral = sp.integrate(integrando, (var_t, -sp.oo, sp.oo))
    
    # Simplificación y manejo de la función sinc
    F_k_simplified = sp.simplify(F_k_integral)
    
    return F_k_simplified

# ----------------------------------------------------
# --- EJEMPLO 1: FUNCIÓN EXPONENCIAL DECAYENTE ---
# ----------------------------------------------------

# f(t) = exp(-a*t) * u(t), donde u(t) es la función escalón unitario (Heaviside)
# La función debe ser causal (f(t)=0 para t<0)
f_exp = sp.exp(-a * t) * sp.Heaviside(t)

print("=== Ejemplo 1: Exponencial Causal (e^(-a*t) u(t)) ===")
print(f"f(t) = {f_exp}")

F_exp = calcular_ft_directa(f_exp)

print(f"F(k) = {F_exp}")
print("-" * 50)


# ----------------------------------------------------
# --- EJEMPLO 2: PULSO RECTANGULAR ---
# ----------------------------------------------------

# f(t) = 1 si -a <= t <= a, 0 en otro caso
f_pulso = sp.Piecewise(
    (1, (t >= -a) & (t <= a)),
    (0, True)
)

print("\n=== Ejemplo 2: Pulso Rectangular ===")
print(f"f(t) = 1 para t en [-a, a]")

F_pulso = calcular_ft_directa(f_pulso)

# La Transformada de Fourier de un pulso rectangular es la función sinc
print(f"F(k) = {F_pulso}")
print(f"F(k) en forma sinc: {2 * a * sp.sinc(a * k)}") 
# Nota: 2*a*sinc(a*k) es la forma estándar usando nuestra convención de k.
print("-" * 50)