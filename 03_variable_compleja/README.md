# 📚 Unidad 03: Fundamentos de Variable Compleja

## 🎯 Objetivos de la Unidad
Esta unidad introduce el análisis de funciones de variable compleja $f(z)$, centrándose en la **analiticidad** (holomorfía) y el poderoso concepto de **integración de contorno** en el plano complejo.

---

## I. Contenido Teórico y Conceptual

| Archivo | Descripción | Nivel |
| :--- | :--- | :--- |
| [**teoria.md**](./teoria.md) | Fundamentos: Representación rectangular y polar. Funciones $f(z) = u + iv$. **Ecuaciones de Cauchy-Riemann (C-R)**. Analiticidad. Teorema de Cauchy-Goursat y Fórmula Integral de Cauchy (FIC). | Conceptual |

---

## II. Práctica y Ejercicios Resueltos

| Archivo | Descripción | Enfoque |
| :--- | :--- | :--- |
| [**ejercicios.ipynb**](./ejercicios.ipynb) | Notebook de Jupyter con la práctica esencial de la unidad: | Procedimental |
| | 1. Conversión entre formas rectangulares y exponenciales. | |
| | 2. **Verificación simbólica** de las Ecuaciones de Cauchy-Riemann. | |
| | 3. Determinación de funciones armónicas conjugadas $v(x, y)$. | |

---

## III. Ejemplos Computacionales (Carpeta `ejemplos_python/`)

Esta subcarpeta contiene scripts de Python que utilizan librerías como SymPy y Matplotlib para visualizar transformaciones y demostrar los teoremas clave de la integración compleja.

| Archivo | Función | Librerías Principales |
| :--- | :--- | :--- |
| [**plot_transformacion.py**](./ejemplos_python/plot_transformacion.py) | Visualización de la transformación del plano $z$ al plano $w$ mediante funciones analíticas (e.g., $w = z^2$). | `NumPy`, `Matplotlib` |
| [**verificar_cauchy_riemann.py**](./ejemplos_python/verificar_cauchy_riemann.py) | Utilidad para el cálculo simbólico de derivadas parciales y **verificación automática** de las condiciones de C-R. | `SymPy` |
| [**calculo_integral_contorno.py**](./ejemplos_python/calculo_integral_contorno.py) | Demostración del **Teorema de Cauchy-Goursat** ($\oint f(z) dz = 0$) y la **Fórmula Integral de Cauchy** usando integración simbólica sobre contornos. | `SymPy` |

---