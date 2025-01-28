import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import norm

def portfolio():
    # Configuration de la page
    st.title("⚙️ Calculs de Risque et Gestion de Portefeuille")

    # Menu déroulant pour sélectionner une section
    section = st.selectbox(
        "Choisissez une section :",
        [
            "Mesures de Risque",
            "Gestion de Portefeuille",
            "Analyse de Sensibilité"
        ]
    )
    st.write("---")

    ### Gestion des sections
    if section == "Mesures de Risque":
        st.subheader("🔹 Mesures de Risque")

        choix = st.selectbox(
            "Choisissez une mesure de risque :",
            ["Value at Risk (VaR)", "Conditional VaR (CVaR)", "Expected Shortfall", "Stress Testing", "Backtesting"]
        )

        if choix == "Value at Risk (VaR)":
            st.write("**Value at Risk (VaR)** : Mesure du risque maximum de perte pour un portefeuille à un certain niveau de confiance.")
            portfolio_value = st.number_input("Valeur du portefeuille (€)", value=100000.0)
            mean_return = st.number_input("Rendement moyen quotidien (%)", value=0.1) / 100
            volatility = st.number_input("Volatilité quotidienne (%)", value=2.0) / 100
            confidence_level = st.slider("Niveau de confiance (%)", 90, 99, 95)

            z_score = norm.ppf(1 - confidence_level / 100)
            var = portfolio_value * (mean_return - z_score * volatility)
            st.write(f"VaR à {confidence_level}% : **{var:.2f} €**")

        elif choix == "Conditional VaR (CVaR)":
            st.write("**Conditional VaR (CVaR)** : Perte moyenne dans les cas où la perte dépasse le VaR.")
            portfolio_value = st.number_input("Valeur du portefeuille (€)", value=100000.0)
            mean_return = st.number_input("Rendement moyen quotidien (%)", value=0.1) / 100
            volatility = st.number_input("Volatilité quotidienne (%)", value=2.0) / 100
            confidence_level = st.slider("Niveau de confiance (%)", 90, 99, 95)

            z_score = norm.ppf(1 - confidence_level / 100)
            cvar = portfolio_value * (mean_return - z_score * volatility) + volatility * portfolio_value * norm.pdf(z_score) / (1 - confidence_level / 100)
            st.write(f"CVaR à {confidence_level}% : **{cvar:.2f} €**")

        elif choix == "Expected Shortfall":
            st.write("**Expected Shortfall (ES)** : Mesure qui représente la perte moyenne au-delà du VaR.")
            portfolio_value = st.number_input("Valeur du portefeuille (€)", value=100000.0)
            mean_return = st.number_input("Rendement moyen quotidien (%)", value=0.1) / 100
            volatility = st.number_input("Volatilité quotidienne (%)", value=2.0) / 100
            confidence_level = st.slider("Niveau de confiance (%)", 90, 99, 95)

            z_score = norm.ppf(1 - confidence_level / 100)
            es = portfolio_value * (mean_return - z_score * volatility) + volatility * portfolio_value * norm.pdf(z_score) / (1 - confidence_level / 100)
            st.write(f"Expected Shortfall (ES) à {confidence_level}% : **{es:.2f} €**")

        elif choix == "Stress Testing":
            st.write("**Stress Testing** : Évaluation du portefeuille sous des scénarios de marché extrêmes.")
            scenario_impact = st.slider("Impact hypothétique (%)", -50, 0, -10)
            portfolio_value = st.number_input("Valeur du portefeuille (€)", value=100000.0)

            stressed_value = portfolio_value * (1 + scenario_impact / 100)
            st.write(f"Valeur du portefeuille après stress test : **{stressed_value:.2f} €**")

        elif choix == "Backtesting":
            st.write("**Backtesting** : Vérification de la précision des modèles de risque.")
            st.write("📌 Fonctionnalité à implémenter en fonction des données historiques du portefeuille.")

    elif section == "Gestion de Portefeuille":
        st.subheader("🔹 Gestion de Portefeuille")

        choix = st.selectbox(
            "Choisissez une fonctionnalité :",
            [
                "Optimisation de Portefeuille (Markowitz)",
                "Allocation d'actifs dynamique",
                "Backtesting des stratégies",
                "Suivi des performances",
                "Optimisation basée sur les modèles factoriels"
            ]
        )

        if choix == "Optimisation de Portefeuille (Markowitz)":
            st.write("**Optimisation de Portefeuille (Markowitz)**")
            assets = st.number_input("Nombre d'actifs dans le portefeuille", min_value=2, value=3)
            returns = st.text_area(
                "Entrez les rendements moyens des actifs séparés par des virgules (en %)", value="5, 7, 10"
            )
            volatility = st.text_area(
                "Entrez les volatilités des actifs séparées par des virgules (en %)", value="10, 15, 20"
            )
            correlation = st.text_area(
                "Entrez la matrice de corrélation (exemple : [[1, 0.2, 0.3], [0.2, 1, 0.4], [0.3, 0.4, 1]])",
                value="[[1, 0.2, 0.3], [0.2, 1, 0.4], [0.3, 0.4, 1]]"
            )

            try:
                returns = np.array([float(x) / 100 for x in returns.split(",")])
                volatilities = np.array([float(x) / 100 for x in volatility.split(",")])
                correlation_matrix = np.array(eval(correlation))
                cov_matrix = np.outer(volatilities, volatilities) * correlation_matrix
                weights = np.linalg.inv(cov_matrix).dot(returns)
                weights /= np.sum(weights)
                st.write(f"Poids optimaux des actifs : {weights}")
            except Exception as e:
                st.error(f"Erreur dans les données d'entrée : {e}")

        else:
            st.write("📌 Fonctionnalité à venir.")

    elif section == "Analyse de Sensibilité":
        st.subheader("🔹 Analyse de Sensibilité")

        choix = st.selectbox(
            "Choisissez une analyse :",
            ["Calcul des Greeks", "Analyse Paramétrique", "Simulation de Scénarios Multi-Actifs"]
        )

        if choix == "Calcul des Greeks":
            st.write("**Calcul des Greeks (Delta, Gamma, Vega, Theta, Rho)**")
            S = st.number_input("Prix initial de l'actif sous-jacent (S₀)", value=100.0)
            K = st.number_input("Prix d'exercice (K)", value=100.0)
            T = st.number_input("Temps à maturité (T, en années)", value=1.0)
            r = st.number_input("Taux d'intérêt sans risque (r)", value=0.05)
            sigma = st.number_input("Volatilité (σ)", value=0.2)

            d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
            d2 = d1 - sigma * np.sqrt(T)

            delta = norm.cdf(d1)
            gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
            vega = S * norm.pdf(d1) * np.sqrt(T)
            theta = - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2)
            rho = K * T * np.exp(-r * T) * norm.cdf(d2)

            st.write(f"**Delta** : {delta:.4f}")
            st.write(f"**Gamma** : {gamma:.4f}")
            st.write(f"**Vega** : {vega:.4f}")
            st.write(f"**Theta** : {theta:.4f}")
            st.write(f"**Rho** : {rho:.4f}")

        else:
            st.write("📌 Fonctionnalité à venir.")

if __name__ == "__main__":
    main()
