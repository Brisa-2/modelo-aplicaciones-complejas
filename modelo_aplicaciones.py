# Simulación interactiva con Streamlit: Conceptos de Variable Compleja
# Autor: ChatGPT

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

st.set_page_config(layout="wide")

st.title("Simulaciones: Funciones de Variable Compleja en Ingeniería Electromecánica")

# -------------------------
# 1. Representación de Fasores
# -------------------------
st.header("1. Representación de Fasores (AC)")
V0 = st.slider("Amplitud de tensión V0", 0.1, 10.0, 1.0)
I0 = st.slider("Amplitud de corriente I0", 0.1, 10.0, 1.0)
phi_v = st.slider("Fase de tensión (rad)", -np.pi, np.pi, 0.0)
phi_i = st.slider("Fase de corriente (rad)", -np.pi, np.pi, 0.0)

z_v = V0 * np.exp(1j * phi_v)
z_i = I0 * np.exp(1j * phi_i)

fig1, ax1 = plt.subplots()
ax1.quiver(0, 0, np.real(z_v), np.imag(z_v), angles='xy', scale_units='xy', scale=1, color='b', label='Tensión')
ax1.quiver(0, 0, np.real(z_i), np.imag(z_i), angles='xy', scale_units='xy', scale=1, color='r', label='Corriente')
ax1.set_xlim(-max(V0, I0)*1.5, max(V0, I0)*1.5)
ax1.set_ylim(-max(V0, I0)*1.5, max(V0, I0)*1.5)
ax1.set_aspect('equal')
ax1.grid(True)
ax1.legend()
ax1.set_title('Fasores en el Plano Complejo')
st.pyplot(fig1)

# -------------------------
# 2. Función Armónica (Laplace)
# -------------------------
st.header("2. Función Armónica (Solución de Laplace)")
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)
Z = np.log(np.sqrt(X**2 + Y**2) + 1e-6)  # evitar log(0)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(X, Y, Z, cmap=cm.viridis)
ax2.set_title('Solución Armónica: ln(r)')
st.pyplot(fig2)

# -------------------------
# 3. Mapeo Conforme: w = z^2
# -------------------------
st.header("3. Mapeo Conforme: w = z²")
res = st.slider("Resolución de puntos", 10, 100, 30)
x = np.linspace(-2, 2, res)
y = np.linspace(-2, 2, res)
X, Y = np.meshgrid(x, y)
Z = X + 1j*Y
W = Z**2

fig3, ax3 = plt.subplots()
ax3.plot(np.real(W), np.imag(W), 'ro', markersize=2, alpha=0.6)
ax3.set_title('Mapeo conforme: $w = z^2$')
ax3.set_xlabel('Parte real')
ax3.set_ylabel('Parte imaginaria')
ax3.axis('equal')
ax3.grid(True)
st.pyplot(fig3)

# -------------------------
# 4. Transformación Clarke-Park (simplificada)
# -------------------------
st.header("4. Transformación Clarke-Park")
i_a = st.number_input("Corriente i_a", value=10.0)
i_b = st.number_input("Corriente i_b", value=-5.0)
i_c = st.number_input("Corriente i_c", value=-5.0)

# Clarke
i_alpha = (2/3)*(i_a - 0.5*i_b - 0.5*i_c)
i_beta = (2/3)*(np.sqrt(3)/2)*(i_b - i_c)

# Park
theta = st.slider("Ángulo theta (rad)", 0.0, 2*np.pi, np.pi/4)
i_d = i_alpha * np.cos(theta) + i_beta * np.sin(theta)
i_q = -i_alpha * np.sin(theta) + i_beta * np.cos(theta)

st.latex(r"i_d = {:.2f},\quad i_q = {:.2f}".format(i_d, i_q))

# -------------------------
# 5. Visualización de integral con residuos
# -------------------------
st.header("5. Integral con residuos")
x = np.linspace(-5, 5, 1000)
y = 1 / (x**2 + 1)
fig5, ax5 = plt.subplots()
ax5.plot(x, y)
ax5.set_title('f(x) = 1 / (x² + 1) — Representación de una integral clásica')
ax5.grid(True)
st.pyplot(fig5)
