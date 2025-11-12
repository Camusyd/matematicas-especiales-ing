# 📚 Unidad 03: Fundamentos de Variable Compleja

## 1. El Campo de los Números Complejos

Un número complejo $z$ se define como $z = x + iy$, donde $x$ es la **parte real** ($\text{Re}(z)$) e $y$ es la **parte imaginaria** ($\text{Im}(z)$). 

### 1.1. Representaciones

* **Forma Rectangular (Cartesiana):** $z = x + iy$.
* **Forma Polar:** $z = r(\cos \theta + i \sin \theta)$.
    * **Módulo ($r$):** La distancia al origen. $r = |z| = \sqrt{x^2 + y^2}$.
    * **Argumento ($\theta$):** El ángulo respecto al eje real positivo. $\theta = \arg(z) = \arctan(y/x)$.
* **Forma Exponencial (Euler):** $z = r e^{i\theta}$. Esta es la más útil para potencias y raíces.

> **Identidad de Euler:** $e^{i\theta} = \cos \theta + i \sin \theta$.

---

## 2. Funciones de Variable Compleja

Una función compleja $f(z)$ mapea un número complejo $z$ a otro número complejo $w$.
$$w = f(z) = u(x, y) + i v(x, y)$$

Donde:
* $u(x, y) = \text{Re}(w)$ es la **parte real** de la función.
* $v(x, y) = \text{Im}(w)$ es la **parte imaginaria** de la función.

---

## 3. Condiciones de Diferenciabilidad: Ecuaciones de Cauchy-Riemann

Para que una función $f(z)$ sea **diferenciable** en un punto $z_0$, debe satisfacer condiciones mucho más estrictas que las funciones reales.

### 3.1. Ecuaciones de Cauchy-Riemann (C-R)

Las derivadas parciales de $u$ y $v$ deben cumplir:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{y} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

### 3.2. Función Analítica (Holomorfa)

Una función $f(z)$ es **analítica** (u holomorfa) en un dominio $D$ si es diferenciable en **todos** los puntos de $D$ y sus derivadas parciales son continuas en $D$.

* **Importancia:** Las funciones analíticas son la clave de la Variable Compleja. Si una función es analítica, se cumplen las propiedades más poderosas de la teoría (como el Teorema de Cauchy).

### 3.3. Funciones Armónicas y Conjugadas

* Una función $u(x, y)$ es **armónica** si cumple la **Ecuación de Laplace**:
    $$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$
* Si $f(z) = u + iv$ es analítica, entonces $u$ y $v$ son **ambas armónicas**.
* $v$ es la **conjugada armónica** de $u$.

---

## 4. Integración de Contorno y Teorema de Cauchy

La integración en el plano complejo se realiza sobre curvas o **contornos** $C$.

$$\oint_C f(z) dz$$

### 4.1. Teorema de Cauchy-Goursat
Si una función $f(z)$ es **analítica** en todos los puntos dentro y sobre un contorno simple y cerrado $C$, entonces la integral de $f(z)$ sobre ese contorno es **cero**.

$$\oint_C f(z) dz = 0$$

### 4.2. Fórmula Integral de Cauchy (FIC)
Si $f(z)$ es analítica dentro y sobre un contorno simple cerrado $C$ (orientado positivamente) y $z_0$ es un punto interior a $C$, entonces:

$$f(z_0) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z - z_0} dz$$

Esta fórmula es fundamental porque permite **calcular el valor de la función** en un punto interior $z_0$ conociendo solo los valores de la función sobre la frontera $C$.

---