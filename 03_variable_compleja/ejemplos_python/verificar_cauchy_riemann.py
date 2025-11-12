# verificar_cauchy_riemann.py
# Script de utilidad que usa SymPy para verificar las Ecuaciones de Cauchy-Riemann (C-R)
# de una función f(z) = u(x, y) + i*v(x, y).

import sympy as sp
from sympy.abc import x, y

def verificar_cr(u_expr, v_expr):
    """
    Verifica si las funciones u(x, y) y v(x, y) cumplen las Ecuaciones de Cauchy-Riemann.
    
    Args:
        u_expr (sympy.Expr): Expresión simbólica para la parte real u(x, y).
        v_expr (sympy.Expr): Expresión simbólica para la parte imaginaria v(x, y).
    """
    
    print(f"Función Real (u): {u_expr}")
    print(f"Función Imaginaria (v): {v_expr}")
    print("\n" + "="*40)
    
    # 1. Cálculo de las Derivadas Parciales
    du_dx = sp.diff(u_expr, x)
    dv_dy = sp.diff(v_expr, y)
    
    du_dy = sp.diff(u_expr, y)
    dv_dx = sp.diff(v_expr, x)

    print("--- Derivadas Parciales ---")
    print(f"du/dx = {du_dx}")
    print(f"dv/dy = {dv_dy}")
    print(f"du/dy = {du_dy}")
    print(f"dv/dx = {dv_dx}")
    print("="*40)

    # 2. Verificación de las Ecuaciones de C-R
    
    # Ecuación 1: du/dx = dv/dy
    check1_diff = sp.simplify(du_dx - dv_dy)
    c1_ok = (check1_diff == 0)
    
    # Ecuación 2: du/dy = -dv/dx
    check2_diff = sp.simplify(du_dy + dv_dx) # Usamos suma para verificar si la diferencia es cero
    c2_ok = (check2_diff == 0)

    print("--- Verificación C-R ---")
    print(f"Ecuación 1 (du/dx = dv/dy): Diferencia = {check1_diff}. Cumple: {c1_ok}")
    print(f"Ecuación 2 (du/dy = -dv/dx): Suma (du/dy + dv/dx) = {check2_diff}. Cumple: {c2_ok}")
    print("-" * 40)
    
    if c1_ok and c2_ok:
        print("✅ La función f(z) = u + iv CUMPLE las Ecuaciones de Cauchy-Riemann. Es una función ANALÍTICA.")
    else:
        print("❌ La función f(z) NO cumple las Ecuaciones de Cauchy-Riemann. NO es analítica.")

# ----------------------------------------------------
# --- EJEMPLOS DE USO ---
# ----------------------------------------------------

# Ejemplo A: Función Analítica (f(z) = z^3)
# f(z) = (x+iy)^3 = (x^3 - 3xy^2) + i(3x^2y - y^3)
print("\n=== Ejemplo A: f(z) = z^3 (Analítica) ===")
u_a = x**3 - 3*x*y**2
v_a = 3*x**2*y - y**3
verificar_cr(u_a, v_a)

# Ejemplo B: Función NO Analítica (f(z) = z_barra = x - iy)
# u(x,y) = x, v(x,y) = -y
print("\n=== Ejemplo B: f(z) = z_barra (No Analítica) ===")
u_b = x
v_b = -y
verificar_cr(u_b, v_b)