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


if __name__ == "__main__":
    main()
