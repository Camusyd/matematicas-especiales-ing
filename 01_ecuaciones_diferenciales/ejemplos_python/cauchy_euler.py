# cauchy_euler.py

import sympy as sp
from sympy import Function, dsolve, Eq, Derivative, symbols

# Define la variable y la función
x = symbols('x')
y = Function('y')

def resolver_cauchy_euler(a, b, c, g_x_str):
    """
    Resuelve una Ecuación de Cauchy-Euler de segundo orden:
    a*x^2*y'' + b*x*y' + c*y = g(x)
    """
    g_x = sp.sympify(g_x_str)
    
    # 1. Define la EDO
    edo = Eq(a * x**2 * Derivative(y(x), x, 2) + 
             b * x * Derivative(y(x), x, 1) + 
             c * y(x), 
             g_x)
    
    print(f"Ecuación: {edo}")
    
    # 2. Resuelve la EDO
    try:
        solucion = dsolve(edo, y(x))
        print("\n--- Solución General (yc + yp) ---")
        print(solucion)
        
        # Opcional: Extraer la solución complementaria (homogénea)
        edo_homogenea = Eq(a * x**2 * Derivative(y(x), x, 2) + 
                           b * x * Derivative(y(x), x, 1) + 
                           c * y(x), 
                           0)
        sol_h = dsolve(edo_homogenea, y(x))
        print(f"\nSolución Complementaria (yc): {sol_h.rhs}")
        
    except Exception as e:
        print(f"\nError al resolver: {e}")

# --- Ejemplo de Uso ---
# EDO: x^2*y'' + 3*x*y' + y = 1/x
print("--- Resolver EDO de Cauchy-Euler con forzante 1/x ---")
resolver_cauchy_euler(a=1, b=3, c=1, g_x_str="1/x")

# EDO: x^2*y'' - 2*y = 3*x^2
print("\n--- Resolver EDO de Cauchy-Euler con forzante 3*x^2 ---")
resolver_cauchy_euler(a=1, b=0, c=-2, g_x_str="3*x**2")