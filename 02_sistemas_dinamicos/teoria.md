# 📚 Unidad 02: Fundamentos de Sistemas Dinámicos

## 1. Representación Matricial: Sistemas Lineales Homogéneos

Un sistema de Ecuaciones Diferenciales Ordinarias (EDOs) de primer orden lineales y homogéneas se expresa de manera compacta como:

$$\mathbf{X}'(t) = \mathbf{A}\mathbf{X}(t)$$

Donde:
* $\mathbf{X}(t) = \begin{pmatrix} x_1(t) \\ x_2(t) \end{pmatrix}$ es el **Vector de Estado** (las variables dependientes).
* $\mathbf{X}'(t)$ es el vector de las derivadas.
* $\mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ es la **Matriz de Coeficientes** (constantes).

## 2. Solución Analítica: Autovalores y Autovectores

La solución general se construye a partir de los autovalores ($\lambda$) y autovectores ($\mathbf{K}$) de la matriz $\mathbf{A}$.

### Ecuación Característica
Los **autovalores ($\lambda$)** se encuentran resolviendo:

$$\det(\mathbf{A} - \lambda\mathbf{I}) = 0$$

### Autovectores
Para cada $\lambda$, el **autovector ($\mathbf{K}$) ** se encuentra resolviendo:

$$(\mathbf{A} - \lambda\mathbf{I})\mathbf{K} = \mathbf{0}$$

### Solución General
La solución es la combinación lineal de las soluciones fundamentales:
$$\mathbf{X}(t) = c_1 \mathbf{K}_1 e^{\lambda_1 t} + c_2 \mathbf{K}_2 e^{\lambda_2 t}$$

## 3. Clasificación de Estabilidad y Retratos de Fase

La naturaleza y la **estabilidad** del **Punto Crítico** (el origen $\mathbf{X} = \mathbf{0}$) están determinadas exclusivamente por los autovalores $\lambda_1$ y $\lambda_2$.

| Tipo de Raíces $\lambda$ | Tipo de Punto Crítico | Estabilidad | Retrato de Fase |
| :--- | :--- | :--- | :--- |
| $\lambda_1, \lambda_2$ Reales; Signos Opuestos | **Punto de Silla** | Inestable | Trayectorias se acercan y luego divergen (líneas rectas). |
| $\lambda_1, \lambda_2$ Reales; Mismo Signo | **Nodo** | Estable (si $\lambda < 0$) o Inestable (si $\lambda > 0$). | Trayectorias rectas que convergen o divergen. |
| $\lambda = \alpha \pm i\beta$ (Complejas) | **Foco** (si $\alpha \ne 0$) | Estable (si $\alpha < 0$) o Inestable (si $\alpha > 0$). | Trayectorias giran en **espiral** hacia o desde el origen.  |
| $\lambda = \pm i\beta$ (Imaginarias Puras) | **Centro** | Marginalmente Estable | Trayectorias son **órbitas cerradas** (círculos/elipses).  |

## 4. Análisis de Sistemas No Lineales: Matriz Jacobiana

Para analizar la estabilidad de un sistema no lineal $\frac{d\mathbf{X}}{dt} = \mathbf{F}(\mathbf{X})$:

1.  **Puntos de Equilibrio ($\mathbf{X}_0$):** Se encuentran resolviendo $\mathbf{F}(\mathbf{X}) = \mathbf{0}$.
2.  **Linealización:** Se evalúa el sistema mediante la **Matriz Jacobiana** $J(\mathbf{X})$.

La matriz $J$ contiene las derivadas parciales de las funciones del sistema $\mathbf{F}(\mathbf{X}) = \begin{pmatrix} f_1(x_1, x_2) \\ f_2(x_1, x_2) \end{pmatrix}$:

$$J(\mathbf{X}) = \begin{pmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \end{pmatrix}$$

Se evalúa $J(\mathbf{X}_0)$ en cada punto de equilibrio. Los autovalores de $J(\mathbf{X}_0)$ determinan la estabilidad y el tipo del punto crítico.