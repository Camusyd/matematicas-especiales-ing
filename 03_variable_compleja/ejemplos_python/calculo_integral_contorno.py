# calculo_integral_contorno.py
# Script para demostrar la integración compleja sobre contornos cerrados utilizando SymPy.
# Demuestra el Teorema de Cauchy-Goursat (integral = 0 para función analítica)
# y la Fórmula Integral de Cauchy (FIC).

import sympy as sp
from sympy.abc import z, t, i

# Definición de la unidad imaginaria para SymPy
i = sp.I

# ----------------------------------------------------
# --- UTILITY: DEFINICIÓN Y PARAMETRIZACIÓN DEL CONTORNO ---
# ----------------------------------------------------

def parametrizar_circulo(radio, centro):
    """Parametriza un círculo con orientación positiva."""
    # z(t) = centro + radio * e^(i*t), donde t varía de 0 a 2*pi
    return centro + radio * sp.exp(i * t)

def integral_contorno(f_z, z_t, t_start, t_end):
    """
    Calcula la integral de línea compleja cerrada: integral(f(z) dz)
    
    Regla: Integral(f(z) dz) = integral( f(z(t)) * z'(t) dt )
    
    Args:
        f_z (sympy.Expr): La función compleja f(z).
        z_t (sympy.Expr): La parametrización del contorno z(t).
        t_start (float): Inicio del parámetro t.
        t_end (float): Fin del parámetro t.
    """
    # 1. Calcular z'(t) = dz/dt
    dz_dt = sp.diff(z_t, t)
    
    # 2. Sustituir z por z(t) en f(z) para obtener f(z(t))
    f_z_t = f_z.subs(z, z_t)
    
    # 3. Calcular el integrando: f(z(t)) * z'(t)
    integrando = f_z_t * dz_dt
    
    # 4. Integrar el integrando respecto a t
    integral = sp.integrate(integrando, (t, t_start, t_end))
    
    return integral

# ----------------------------------------------------
# --- EJEMPLO 1: TEOREMA DE CAUCHY-GOURSAT ---
# ----------------------------------------------------

# Función analítica en todo el plano complejo (polinomio)
f_cauchy_goursat = z**2 + 2*z + 1

# Contorno C: Círculo unitario centrado en el origen (radio=1, centro=0)
z_contorno_1 = parametrizar_circulo(radio=1, centro=0)

print("=== Ejemplo 1: Teorema de Cauchy-Goursat ===")
print(f"Función analítica: f(z) = {f_cauchy_goursat}")
print(f"Contorno C: |z| = 1")

resultado_c1 = integral_contorno(f_cauchy_goursat, z_contorno_1, 0, 2*sp.pi)

print(f"Resultado (integral f(z) dz): {resultado_c1}")
print("Confirmación: Para una función analítica y contorno cerrado, la integral debe ser 0.")
print("-" * 40)

# ----------------------------------------------------
# --- EJEMPLO 2: FÓRMULA INTEGRAL DE CAUCHY (FIC) ---
# ----------------------------------------------------

# Caso simple: integral( 1 / (z - z0) dz ) = 2*pi*i (si z0 está dentro)

# z0 (singularidad) dentro del contorno
z0 = i  # z0 = i está dentro del círculo de radio 2

# Función a integrar: f(z) = 1 / (z - z0). F(z) = 1, z0 = i
f_fic = 1 / (z - z0)

# Contorno C: Círculo de radio 2 centrado en el origen
z_contorno_2 = parametrizar_circulo(radio=2, centro=0)

print("\n=== Ejemplo 2: Fórmula Integral de Cauchy (FIC) ===")
print(f"Integrando: f(z) / (z - z0) = {f_fic}")
print(f"Singularidad (z0): {z0}")
print(f"Contorno C: |z| = 2")

resultado_c2 = integral_contorno(f_fic, z_contorno_2, 0, 2*sp.pi)
resultado_c2_simplificado = sp.simplify(resultado_c2)

print(f"Resultado (integral f(z) dz): {resultado_c2_simplificado}")

# Aplicando la FIC: integral = 2*pi*i * f(z0). Como f(z) = 1, la integral debe ser 2*pi*i.
fic_teorico = 2 * sp.pi * i

print(f"Resultado Teórico (2*pi*i): {fic_teorico}")
if sp.simplify(resultado_c2_simplificado - fic_teorico) == 0:
    print("✅ El resultado concuerda con la Fórmula Integral de Cauchy.")
else:
    print("❌ El resultado NO concuerda con la Fórmula Integral de Cauchy.")