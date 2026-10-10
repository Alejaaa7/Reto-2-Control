# Gráfica generada para el punto 4 del Reto 2 - Control (2026-2)

- Andrea Alejandra Suárez Cuervo
- Jonathan Alexander Ducuara Enciso

Efecto de la ubicación de los polos en la respuesta al escalón unitario.

Sistema de segundo orden con ganancia DC = 1:

La función de transferencia es:

$$
G(s) = \frac{\omega_n^2}{s^2 + 2\sigma s + \omega_n^2}
$$

Los polos son:

$$
s = -\sigma \pm j\omega_d
$$

Las relaciones entre los parámetros son:

$$
\omega_n^2 = \sigma^2 + \omega_d^2
$$

$$
\zeta = \frac{\sigma}{\omega_n},
\qquad
\theta = \arccos(\zeta)
$$

Se comparan tres casos contra un par de polos de referencia (-1 ± j4):
  A) misma sigma, distinta wd
  B) misma wd, distinta sigma
  C) mismo ángulo theta, polos más lejos del origen

Requisitos: numpy, scipy, matplotlib
Uso: python polos_plano_s.py   ->   genera polos_plano_s.png
