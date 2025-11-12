# 📚 Unidad 04: Análisis de Fourier

## 1. Series de Fourier Trigonométricas

Una **Serie de Fourier** permite representar una función periódica $f(t)$ con periodo $T=2L$ como una suma infinita de funciones trigonométricas (senos y cosenos). 

### 1.1. La Serie y sus Coeficientes

Para una función $f(t)$ definida en el intervalo $[-L, L]$, la **Serie de Fourier** es:

$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos\left(\frac{n\pi t}{L}\right) + b_n \sin\left(\frac{n\pi t}{L}\right) \right]$$

Los **Coeficientes de Fourier** se calculan mediante las siguientes integrales:

* **Término DC (Media):**
    $$a_0 = \frac{1}{L} \int_{-L}^{L} f(t) dt$$

* **Coeficientes del Coseno (Par):**
    $$a_n = \frac{1}{L} \int_{-L}^{L} f(t) \cos\left(\frac{n\pi t}{L}\right) dt$$

* **Coeficientes del Seno (Impar):**
    $$b_n = \frac{1}{L} \int_{-L}^{L} f(t) \sin\left(\frac{n\pi t}{L}\right) dt$$

### 1.2. Condición de Dirichlet y Fenómeno de Gibbs

La serie converge al valor de $f(t)$ si esta cumple las **condiciones de Dirichlet**:
1.  Es **acotada** en el intervalo.
2.  Tiene un número finito de **discontinuidades** de salto en el intervalo.
3.  Tiene un número finito de **extremos** (máximos y mínimos) en el intervalo.

> **Fenómeno de Gibbs:** En los puntos de discontinuidad (saltos), la serie converge al punto medio del salto, pero siempre muestra un **sobreimpulso (overshoot)** constante de aproximadamente **9%** cerca de la discontinuidad. 

---

## 2. Serie de Fourier Compleja

La representación compleja simplifica la manipulación matemática, unificando los coeficientes $a_n$ y $b_n$ en un solo coeficiente $c_n$.

### 2.1. La Serie y sus Coeficientes

La **Serie de Fourier Compleja** es:

$$f(t) = \sum_{n=-\infty}^{\infty} c_n e^{i \frac{n\pi t}{L}}$$

* **Coeficientes Complejos ($c_n$):**
    $$c_n = \frac{1}{2L} \int_{-L}^{L} f(t) e^{-i \frac{n\pi t}{L}} dt$$

---

## 3. La Transformada de Fourier (FT)

La **Transformada de Fourier** ($\mathcal{F}$) extiende el concepto de serie a **funciones no periódicas** (periodo infinito), convirtiendo una función del **dominio del tiempo** ($t$) al **dominio de la frecuencia** ($\omega$ o $k$). 

[Image of a time domain signal being transformed into a frequency domain spectrum, illustrating the concept of the Fourier Transform]


### 3.1. Definición de la Transformada ($\mathcal{F}$)

La Transformada de Fourier de una función $f(t)$ se denota como $F(\omega)$:

$$\mathcal{F}\{f(t)\} = F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i \omega t} dt$$

### 3.2. Transformada Inversa ($\mathcal{F}^{-1}$)

Permite reconstruir la función original a partir de su espectro de frecuencias $F(\omega)$:

$$\mathcal{F}^{-1}\{F(\omega)\} = f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i \omega t} d\omega$$

### 3.3. Propiedades Clave

Las propiedades de la Transformada de Fourier son fundamentales para simplificar el análisis de sistemas.

| Propiedad | Función en el Tiempo ($f(t)$) | Transformada en la Frecuencia ($F(\omega)$) |
| :--- | :--- | :--- |
| **Linealidad** | $a f(t) + b g(t)$ | $a F(\omega) + b G(\omega)$ |
| **Escalamiento** | $f(at)$ | $\frac{1}{|a|} F\left(\frac{\omega}{a}\right)$ |
| **Desplazamiento** | $f(t - t_0)$ | $e^{-i \omega t_0} F(\omega)$ |
| **Derivación** | $f'(t)$ | $i \omega F(\omega)$ |
| **Convolución** | $f(t) * g(t)$ | $F(\omega) \cdot G(\omega)$ |

---

## 4. Transformada Rápida de Fourier (FFT)

La **FFT** (Fast Fourier Transform) es un algoritmo computacionalmente eficiente para calcular la Transformada Discreta de Fourier (DFT). Es esencial en el **procesamiento digital de señales** para analizar las frecuencias dominantes en datos muestreados.
