# 📚 Unidad 04: Análisis de Fourier

## 🎯 Objetivos de la Unidad
Esta unidad se centra en la representación de funciones periódicas mediante **Series de Fourier** y la extensión de este concepto a funciones no periódicas a través de la **Transformada de Fourier**, fundamentales en el análisis de señales y la resolución de EDPs.

---

## I. Contenido Teórico y Conceptual

| Archivo | Descripción | Nivel |
| :--- | :--- | :--- |
| [**teoria.md**](./teoria.md) | Fundamentos de Series Trigonométricas y Complejas de Fourier. Coeficientes ($a_n, b_n, c_n$). Condición de Dirichlet y **Fenómeno de Gibbs**. Definición de la **Transformada de Fourier** ($\mathcal{F}$) y sus propiedades clave (linealidad, escalamiento, etc.). | Conceptual |

---

## II. Práctica y Ejercicios Resueltos

| Archivo | Descripción | Enfoque |
| :--- | :--- | :--- |
| [**ejercicios.ipynb**](./ejercicios.ipynb) | Notebook de Jupyter con la práctica esencial: | Procedimental |
| | 1. **Cálculo simbólico** de coeficientes de Fourier (Onda Cuadrada). | |
| | 2. **Visualización** de la convergencia de la serie de Fourier. | |
| | 3. Cálculo de la **Transformada de Fourier** (Pulso Rectangular) usando SymPy. | |

---

## III. Ejemplos Computacionales (Carpeta `ejemplos_python/`)

Esta subcarpeta contiene scripts de Python diseñados para ilustrar los conceptos de convergencia y cálculo simbólico de la Transformada.

| Archivo | Función | Librerías Principales |
| :--- | :--- | :--- |
| [**serie_fourier_convergencia.py**](./ejemplos_python/serie_fourier_convergencia.py) | Script para simular y graficar la **convergencia** de una serie de Fourier (Onda Cuadrada) a medida que se añaden más términos, ilustrando el **Fenómeno de Gibbs**. | `NumPy`, `Matplotlib` |
| [**calculo_transformada.py**](./ejemplos_python/calculo_transformada.py) | Utilidad basada en **SymPy** para calcular y obtener el resultado simbólico de la **Transformada de Fourier** de funciones básicas. | `SymPy`, `Matplotlib` |

---