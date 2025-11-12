# 📚 Unidad 02: Fundamentos de Sistemas Dinámicos

## 🎯 Objetivos de la Unidad
Esta unidad establece los fundamentos teóricos y prácticos para el análisis de sistemas dinámicos continuos, tanto lineales como no lineales, con un enfoque en el análisis cualitativo y la estabilidad de los puntos de equilibrio.

---

## I. Contenido Teórico y Conceptual

| Archivo | Descripción | Nivel |
| :--- | :--- | :--- |
| [teoria.md](./teoria.md) | **Representación Matricial:** $\mathbf{X}' = \mathbf{A}\mathbf{X}$. Cálculo de la Ecuación Característica, Autovalores ($\lambda$) y Autovectores ($\mathbf{K}$). | Conceptual |
| | **Clasificación y Estabilidad:** Tipos de puntos críticos (Nodos, Sillas, Focos, Centros) y su estabilidad determinada por $\lambda$. | Conceptual |
| | **Sistemas No Lineales:** Introducción al análisis de estabilidad local mediante la **Matriz Jacobiana** ($J$). | Conceptual |

---

## II. Práctica y Ejercicios Resueltos

| Archivo | Descripción | Enfoque |
| :--- | :--- | :--- |
| [ejercicios.ipynb](./ejercicios.ipynb) | Notebook de Jupyter con la resolución de ejercicios clave: | Procedimental |
| | 1. Transformación de EDOs de orden superior. | |
| | 2. Resolución de los tres casos principales de autovalores (Reales Distintos, Reales Repetidos, Complejos). | |
| | 3. Cálculo de la Matriz Jacobiana de un sistema no lineal. | |

---

## III. Ejemplos Computacionales (Carpeta `ejemplos_python/`)

Esta subcarpeta contiene scripts de Python que implementan la visualización y el cálculo numérico para complementar la teoría.

| Archivo | Función | Librerías Principales |
| :--- | :--- | :--- |
| [**plot_plano_fase.py**](./ejemplos_python/plot_plano_fase.py) | Script para generar **Retratos de Fase** de sistemas lineales 2x2. Muestra el campo vectorial y las trayectorias para visualizar la estabilidad (Focos, Nodos, Sillas). | `NumPy`, `Matplotlib`, `SciPy` |
| [**simulacion_lotka_volterra.py**](./ejemplos_python/simulacion_lotka_volterra.py) | **Simulación numérica** de un sistema no lineal clásico (Presa-Depredador) para ilustrar **Centros** y órbitas cerradas. | `SciPy` (`solve_ivp`), `Matplotlib` |
| [**calc_autovalores.py**](./ejemplos_python/calc_autovalores.py) | Utilidad para el cálculo rápido y la **clasificación** de autovalores/autovectores de cualquier matriz $\mathbf{A}$. | `NumPy` |

---