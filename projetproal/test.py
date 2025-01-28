import streamlit as st
import os
from streamlit_navigation_bar import st_navbar  # Assurez-vous que cette bibliothèque est installée
import pages as pg  # Import des pages qui sont définies dans un autre fichier
from home import show_home
from loi_normal import show_normal_law
from markov import markov_chain_page

# Configuration initiale de la page
st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

# Définir les pages de navigation avec les modifications demandées
pages = [
    "Home",  # Ajoutez la page Home
    "Loi Normale",
    "Mvt Brownien",
    "Monte Carlo",
    "À Propos"
]

# Chemin du logo
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "cubes.svg")

# URLs pour les pages externes (facultatif)
urls = {"À Propos": "https://www.linkedin.com/in/mhamedabdelhamidbou/"}

# Styles pour la barre de navigation
styles = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "35px",
    },
    "span": {
        "color": "white",
        "padding": "38px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
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
    urls=urls,
    styles=styles,
    options=options,
)

# Gérer le clic sur le logo pour rediriger vers la page d'accueil
if page == "Home":
    st.session_state.current_page = "Home"
else:
    st.session_state.current_page = page

# Dictionnaire pour lier les pages aux fonctions
functions = {
    "Home": show_home,  # Remplacez par la référence de fonction, ne l'appelez pas
    "Loi Normale": show_normal_law,
    "Mvt Brownien": pg.show_brownian,
    "Monte Carlo": pg.show_monte_carlo,
    "À Propos": pg.show_about,
}

# Appeler la fonction correspondant à la page sélectionnée
go_to = functions.get(st.session_state.current_page)
if go_to:
    go_to()  # Appel de la fonction de la page sélectionnée
else:
    st.write("Page not found")
