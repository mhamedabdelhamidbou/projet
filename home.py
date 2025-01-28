import streamlit as st
import base64
import time
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Application de Finance", layout="wide")
    show_home()

def show_home():
    # Titre de la page
    st.title("🚀 Projet de monte carlo : ENSA AGADIR-FID")

    # Séparation des sections avec des sous-titres
    st.subheader("📊 1. Simulations Stochastiques Avancées")

    # Simulations de processus
    st.markdown("""
    🔹 **Processus de Base**  
    • Simulation de la Loi Normale (standard et tronquée)  
    • Mouvement Brownien Standard (Wiener Process)  
    • Mouvement Brownien avec Drift  
    • Mouvement Brownien Géométrique (GBM)  

    🔹 **Processus Complexes**  
    • Processus de Poisson (Modélisation des sauts de prix)  
    • Modèle de Diffusion avec Sauts (Merton Jump-Diffusion)  
    • Processus de Lévy (modélisation des marchés à queue épaisse)  
    • Processus de Variance Stochastique (Modèle de Heston)  
    • Processus Fractionnaire (Mouvement Brownien Fractionnaire)  
    • Processus de Cox-Ingersoll-Ross (CIR) pour modéliser les taux d'intérêt  
    • Modèle SABR (Stochastic Alpha Beta Rho) pour la volatilité implicite
    """)

    # Section pour le pricing des produits dérivés
    st.subheader("💸 2. Pricing de Produits Dérivés et Exotiques")

    st.markdown("""
    🔹 **Options Vanilles**  
    • Pricing d'Options Européennes (Call et Put) (Monte Carlo, Black-Scholes)  
    • Pricing d'Options Américaines (méthode de Least Squares Monte Carlo)  

    🔹 **Options Exotiques**  
    • Options Asiatiques (moyenne arithmétique et géométrique)  
    • Options Barrières (Knock-in/Knock-out)  
    • Options Lookback (prix optimal historique)  
    • Options Digitales (paiement binaire)  
    • Options Rainbow (multi-actifs)  
    • Options Cliquet (ajustements périodiques)  

    🔹 **Produits Structurés**  
    • Convertible Bonds  
    • Autocallables et Reverse Convertibles  
    • Swaps de taux d’intérêt (IRS, OIS)  
    • Credit Default Swaps (CDS)
    """)

    # Section pour les calculs de risque et gestion de portefeuille
    st.subheader("⚙️ 3. Calculs de Risque et Gestion de Portefeuille")

    st.markdown("""
    🔹 **Mesures de Risque**  
    • Value at Risk (VaR) et Conditional VaR (CVaR)  
    • Expected Shortfall  
    • Stress Testing et Scénarios de Choc  
    • Backtesting des modèles de risque  

    🔹 **Gestion de Portefeuille**  
    • Optimisation de Portefeuille (Markowitz, Black-Litterman)  
    • Allocation d’actifs dynamique et rééquilibrage automatique  
    • Backtesting des stratégies d’investissement  
    • Suivi des performances (Sharpe, Sortino, Alpha, Beta)  
    • Optimisation basée sur les modèles factoriels (Fama-French, Carhart)  

    🔹 **Analyse de Sensibilité**  
    • Calcul des Greeks (Delta, Gamma, Vega, Theta, Rho)  
    • Analyse de Sensibilité Paramétrique  
    • Simulation de Scénarios Multi-Actifs
    """)

    # Section pour le trading algorithmique et intelligence artificielle
    st.subheader("📈 4. Trading Algorithmique et Intelligence Artificielle")

    st.markdown("""
    🔹 **Indicateurs Techniques**  
    • RSI, MACD, Bandes de Bollinger, Moyennes Mobiles (SMA, EMA)  
    • Ichimoku, Stochastic Oscillator, ATR, ADX  

    🔹 **Stratégies de Trading**  
    • Trading Momentum, Mean Reversion  
    • Pairs Trading (Cointegration)  
    • Arbitrage Statistique  
    • Market Making et Arbitrage Haute Fréquence  

    🔹 **Machine Learning et Deep Learning**  
    • Prévision des prix avec LSTM, GRU  
    • Détection de tendances avec Random Forest, XGBoost  
    • Réseaux de neurones convolutifs (CNN) pour l’analyse des séries temporelles  
    • Renforcement (Q-Learning, PPO) pour stratégie de trading autonome  

    🔹 **Automatisation et Exécution**  
    • Simulation d’ordres (Market, Limit, Stop-Loss, Take-Profit)  
    • Gestion des ordres en temps réel via des API de trading (Binance, Interactive Brokers)
    """)



    # Conclusion et objectif final
    st.subheader("🎯 Objectif Final")

    st.markdown("""
    Créer une plateforme complète et professionnelle qui couvre l’ensemble des besoins en simulation financière, gestion des risques, trading algorithmique, pricing des dérivés et analyse de portefeuille.
    Un tel projet deviendra un outil incontournable pour les quantitative analysts, traders, gestionnaires de portefeuille et investisseurs institutionnels.
    """)

if __name__ == "__main__":
    main()
