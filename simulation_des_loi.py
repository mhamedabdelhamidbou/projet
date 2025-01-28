import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable


def show_simulation_des_lois():
    # Configuration générale
    st.title("📊 Simulations Stochastiques Avancées")

    # Menu déroulant pour sélectionner le type de processus
    processus = st.selectbox(
        "Choisissez le processus à simuler :",
        [
            "Loi Normale (Standard et Tronquée)",
            "Mouvement Brownien Standard",
            "Processus de Variance Stochastique (Heston)",
            "Modèle SABR",
            "Processus de Lévy",
            "Mouvement Brownien Fractionnaire",
            "Processus de Cox-Ingersoll-Ross (CIR)"
        ]
    )
    st.write("---")  # Séparation visuelle

    def simulate_normal_law(truncated=False):
        mu = st.number_input("Moyenne (µ)", value=0.0)
        sigma = st.number_input("Écart-type (σ)", value=1.0)
        n = st.slider("Nombre de points", 100, 1000, 500)
        if truncated:
            lower = st.number_input("Borne inférieure", value=-2.0)
            upper = st.number_input("Borne supérieure", value=2.0)
            data = np.random.normal(mu, sigma, n)
            data = data[(data > lower) & (data < upper)]
        else:
            data = np.random.normal(mu, sigma, n)
        plt.hist(data, bins=30, density=True)
        plt.title("Loi Normale")
        st.pyplot(plt)

    def simulate_wiener_process():
        t = st.number_input("Temps total (T)", value=1.0)
        n = st.slider("Nombre de points", 100, 1000, 500)
        dt = t / n
        wiener = np.cumsum(np.random.normal(0, np.sqrt(dt), n))
        plt.plot(np.linspace(0, t, n), wiener)
        plt.title("Mouvement Brownien Standard")
        st.pyplot(plt)

    def simulate_heston():
        s0 = st.number_input("Prix initial (S₀)", value=100.0)
        v0 = st.number_input("Variance initiale (v₀)", value=0.04)
        kappa = st.number_input("Taux de réversion (κ)", value=2.0)
        theta = st.number_input("Variance long terme (θ)", value=0.04)
        xi = st.number_input("Volatilité de la variance (ξ)", value=0.1)
        rho = st.number_input("Corrélation (ρ)", value=-0.5)
        t = st.number_input("Temps total (T)", value=1.0)
        n = st.slider("Nombre de points", 100, 1000, 500)
        dt = t / n
        prices = [s0]
        variances = [v0]
        for _ in range(1, n):
            dW1 = np.random.normal(0, np.sqrt(dt))
            dW2 = rho * dW1 + np.sqrt(1 - rho ** 2) * np.random.normal(0, np.sqrt(dt))
            v_t = max(variances[-1] + kappa * (theta - variances[-1]) * dt + xi * np.sqrt(variances[-1]) * dW1, 0)
            variances.append(v_t)
            prices.append(prices[-1] * np.exp(-0.5 * v_t * dt + np.sqrt(v_t) * dW2))
        plt.plot(np.linspace(0, t, n), prices)
        plt.title("Processus de Heston")
        st.pyplot(plt)

    def simulate_sabr():
        f0 = st.number_input("Prix initial (f₀)", value=100.0)
        alpha = st.number_input("Volatilité (α)", value=0.3)
        beta = st.number_input("Exposant β (0 ≤ β ≤ 1)", value=0.5)
        rho = st.number_input("Corrélation (ρ)", value=-0.5)
        nu = st.number_input("Volatilité de volatilité (ν)", value=0.2)
        t = st.number_input("Temps total (T)", value=1.0)
        n = st.slider("Nombre de points", 100, 1000, 500)
        dt = t / n
        f_t = f0
        alpha_t = alpha
        prices = [f_t]
        for _ in range(1, n):
            dW1 = np.random.normal(0, np.sqrt(dt))
            dW2 = rho * dW1 + np.sqrt(1 - rho ** 2) * np.random.normal(0, np.sqrt(dt))
            alpha_t += nu * alpha_t * dW2
            f_t += alpha_t * (f_t ** beta) * dW1
            prices.append(f_t)
        plt.plot(np.linspace(0, t, n), prices)
        plt.title("Modèle SABR")
        st.pyplot(plt)

    def simulate_levy():
        alpha = st.slider("Stabilité (α)", 0.1, 2.0, 1.5)
        beta = st.slider("Asymétrie (β)", -1.0, 1.0, 0.0)
        scale = st.number_input("Échelle", value=1.0)
        n = st.slider("Nombre de points", 100, 1000, 500)
        data = levy_stable.rvs(alpha, beta, scale=scale, size=n)
        plt.hist(data, bins=30, density=True)
        plt.title("Processus de Lévy")
        st.pyplot(plt)

    def simulate_fractional_brownian():
        hurst = st.slider("Paramètre de Hurst (H)", 0.1, 0.9, 0.5)
        n = st.slider("Nombre de points", 100, 1000, 500)
        time = np.linspace(0, 1, n)
        fbm = np.cumsum(np.random.normal(0, np.sqrt((time[1:] - time[:-1]) ** (2 * hurst)), size=n - 1))
        fbm = np.insert(fbm, 0, 0)
        plt.plot(time, fbm)
        plt.title("Mouvement Brownien Fractionnaire")
        st.pyplot(plt)

    def simulate_cir():
        x0 = st.number_input("Valeur initiale (x₀)", value=0.05)
        kappa = st.number_input("Taux de réversion (κ)", value=0.1)
        theta = st.number_input("Moyenne long terme (θ)", value=0.05)
        sigma = st.number_input("Volatilité (σ)", value=0.02)
        t = st.number_input("Temps total (T)", value=1.0)
        n = st.slider("Nombre de points", 100, 1000, 500)
        dt = t / n
        x = [x0]
        for _ in range(1, n):
            dx = kappa * (theta - x[-1]) * dt + sigma * np.sqrt(max(x[-1], 0)) * np.random.normal(0, np.sqrt(dt))
            x.append(max(x[-1] + dx, 0))
        plt.plot(np.linspace(0, t, n), x)
        plt.title("Processus CIR")
        st.pyplot(plt)

    # Gestion des choix
    if processus == "Loi Normale (Standard et Tronquée)":
        simulate_normal_law(truncated=True)
    elif processus == "Mouvement Brownien Standard":
        simulate_wiener_process()
    elif processus == "Processus de Variance Stochastique (Heston)":
        simulate_heston()
    elif processus == "Modèle SABR":
        simulate_sabr()
    elif processus == "Processus de Lévy":
        simulate_levy()
    elif processus == "Mouvement Brownien Fractionnaire":
        simulate_fractional_brownian()
    elif processus == "Processus de Cox-Ingersoll-Ross (CIR)":
        simulate_cir()
    else:
        st.warning("Processus non implémenté.")


# Exécuter la simulation
