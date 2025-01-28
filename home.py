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
    st.write(
        """<h1 style='text-align: center; color: #0066CC; animation: fadeIn 3s;'>Bienvenue sur notre application</h1>""",
        unsafe_allow_html=True)

    # Supprimer l'image de fond ou le visuel accrocheur
    st.markdown(
        """
        <style>
        @keyframes slideIn {
            0% {transform: translateX(-100%); opacity: 0;}
            100% {transform: translateX(0); opacity: 1;}
        }
        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }
        .content {
            color: #003366;
            font-size: 18px;
            line-height: 1.6;
        }
        ul {
            color: #003366;
            font-size: 18px;
            line-height: 1.6;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("""<h3 style='text-align: center; color: #0066CC; animation: fadeIn 3s;'>Contexte du projet</h3>""",
             unsafe_allow_html=True)
    st.write("""  
    <div class='content' style='animation: fadeIn 3s;'>
    Cette application est conçue pour simuler divers modèles financiers et aider les utilisateurs à 
    mieux comprendre les concepts de finance quantitative. 
    Elle permet d'explorer différents processus stochastiques et d'analyser les comportements 
    des actifs financiers dans diverses conditions de marché.
    </div>
    """, unsafe_allow_html=True)

    st.write("""<h3 style='text-align: center; color: #0066CC; animation: fadeIn 3s;'>Vision générale</h3>""",
             unsafe_allow_html=True)
    st.write("""  
    <div class='content' style='animation: fadeIn 3s;'>
    L'objectif principal de cette application est de fournir un outil interactif et éducatif 
    pour les étudiants, les chercheurs et les professionnels de la finance. 
    Grâce à des simulations de la loi normale, du mouvement brownien, et d'autres modèles financiers, 
    les utilisateurs peuvent visualiser et analyser les résultats en temps réel. 
    Ce projet vise également à renforcer les compétences pratiques des étudiants en 
    finance quantitative et à les préparer à des défis réels dans le domaine de la finance.
    </div>
    """, unsafe_allow_html=True)

    st.write(
        """<h3 style='text-align: center; color: #0066CC; animation: fadeIn 3s;'>Fonctionnalités de l'application</h3>""",
        unsafe_allow_html=True)
    st.write("""
    <ul style='animation: fadeIn 3s;'>
        <li>Simulation de la loi normale</li>
        <li>Simulation du mouvement brownien</li>
        <li>Pricing des options avec Monte Carlo</li>
        <li>Gestion de portefeuille</li>
        <li>Pricing des actifs dérivés</li>
        <li>Pricing des actifs classiques</li>
        <li>Chaînes de Markov</li>
        <li>Informations</li>
    </ul>
    """, unsafe_allow_html=True)

    # Ajouter une simulation de graphique interactif pour une meilleure expérience
    st.write("""<h3 style='text-align: center; color: #0066CC; animation: fadeIn 3s;'>Simulation de Mouvement Brownien</h3>""",
             unsafe_allow_html=True)
    
    # Paramètres de simulation
    initial_price = st.slider('Prix initial de l\'actif', min_value=50, max_value=200, value=100)
    volatility = st.slider('Volatilité', min_value=0.01, max_value=0.5, value=0.2)
    drift = st.slider('Taux de rentabilité (drift)', min_value=0.01, max_value=0.2, value=0.05)
    time_horizon = st.slider('Horizon temporel (années)', min_value=1, max_value=10, value=1)
    num_simulations = st.slider('Nombre de simulations', min_value=1, max_value=10, value=3)
    
    # Simulation de trajectoires de prix
    time_steps = 252  # Nombre de jours de bourse dans une année
    dt = time_horizon / time_steps
    time_index = np.linspace(0, time_horizon, time_steps)
    
    fig, ax = plt.subplots(figsize=(10, 6))

    for _ in range(num_simulations):
        price_path = [initial_price]
        for t in range(1, time_steps):
            price_path.append(price_path[-1] * np.exp((drift - 0.5 * volatility ** 2) * dt + volatility * np.sqrt(dt) * np.random.normal()))
        ax.plot(time_index, price_path, label=f'Simulation {_+1}')
    
    ax.set_title('Simulations de Mouvement Brownien', fontsize=16)
    ax.set_xlabel('Temps (Années)')
    ax.set_ylabel('Prix')
    ax.legend()
    
    st.pyplot(fig)

if __name__ == "__main__":
    main()
