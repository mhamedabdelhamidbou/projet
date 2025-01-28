import streamlit as st
import os
from streamlit_navigation_bar import st_navbar  # Assurez-vous que ce module est installé
from home import show_home
from loi_normal import show_distribution_simulation
from markov import markov_chain_page
from monte_carlo import show_monte_carlo
from ABOUT import about_us_page
from show_brownian import show_brownian
from heston import run_app  # Fonction pour l'application de pricing Heston
from simulation_des_loi import show_simulation_des_lois  # Importer la nouvelle page
from portfolio import portfolio
from trading import trading

# Configuration initiale de la page Streamlit
st.set_page_config(
    page_title="Application de Finance Stochastique",
    page_icon="📈",
    initial_sidebar_state="collapsed",
    layout="wide"
)

# Définir les pages de navigation
pages = [
    "Home",  # Page d'accueil
    "Simulation de loi",  # Simulation des lois de probabilité
    "Simulation avancé",  # Nouvelle page ajoutée
    "Mvt Brownien",  # Mouvement Brownien
    "Monte Carlo",  # Simulations Monte Carlo
    "Getion de portfeuille",
    "trading",
    "Modèle Heston",  # Modèle Heston
    "À Propos"  # Page À Propos
]

# Chemin du logo
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "cubes.svg")

# Styles personnalisés pour la barre de navigation
styles = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "30px",
    },
    "span": {
        "color": "white",
        "padding": "30px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "13px",
    }
}

# Options de navigation
options = {
    "show_menu": False,
    "show_sidebar": False,
}

# Afficher la barre de navigation
page = st_navbar(
    pages,
    logo_path=logo_path,
    styles=styles,
    options=options,
)

# Gérer la redirection lorsque le logo est cliqué
if page == "Home":
    st.session_state.current_page = "Home"
else:
    st.session_state.current_page = page

# Dictionnaire pour mapper les pages aux fonctions correspondantes
functions = {
    "Home": show_home,  # Page d'accueil
    "Simulation de loi": show_distribution_simulation,  # Simulation des lois de probabilité
    "Simulation avancé": show_simulation_des_lois,  # Nouvelle page ajoutée
    "Mvt Brownien": show_brownian,  # Mouvement Brownien
    "Monte Carlo": show_monte_carlo,  # Simulation Monte Carlo
    "Getion de portfeuille":portfolio,
    "trading":trading,
    "Modèle Heston": run_app,  # Modèle Heston
    "À Propos": about_us_page,  # Page À Propos
}

# Exécuter la fonction associée à la page sélectionnée
go_to = functions.get(st.session_state.current_page)
if go_to:
    go_to()  # Appeler la fonction associée à la page
else:
    st.error("Page introuvable. Veuillez vérifier la configuration.")
