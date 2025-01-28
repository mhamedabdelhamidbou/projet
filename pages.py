import streamlit as st

# Simuler le Mouvement Brownien (Drift et Géométrique)
def show_brownian():
    st.title("Simuler le Mouvement Brownien")
    simulation_type = st.selectbox("Choisissez le type de Mouvement Brownien", ["Drift", "Géométrique"])

    drift = st.number_input("Entrez le drift", value=0.0)
    stddev = st.number_input("Entrez l'écart type", value=1.0)
    num_simulations = st.number_input("Entrez le nombre de simulations", value=1000)
    period = st.number_input("Entrez la période", value=1.0)
    steps = st.number_input("Entrez le nombre de pas", value=100)

    if simulation_type == "Géométrique":
        initial_value = st.number_input("Entrez la valeur initiale", value=100.0)

    if st.button("Simuler"):
        if simulation_type == "Drift":
            # Logique pour simuler le Mouvement Brownien avec Drift
            st.write(f"Simulation du mouvement brownien avec drift={drift}, écart type={stddev}, etc.")
        elif simulation_type == "Géométrique":
            # Logique pour simuler le Mouvement Brownien Géométrique
            st.write(
                f"Simulation du mouvement brownien géométrique avec drift={drift}, écart type={stddev}, valeur initiale={initial_value}, etc.")


# Pricing des options avec Monte Carlo
def show_monte_carlo():
    st.title("Pricing des Options avec Monte Carlo")
    asset_price = st.number_input("Entrez le prix de l'action", value=100.0)
    strike_price = st.number_input("Entrez le prix d'exercice", value=100.0)
    interest_rate = st.number_input("Entrez le taux d'intérêt (décimal)", value=0.05)
    time_to_maturity = st.number_input("Temps jusqu'à l'échéance (en années)", value=1.0)
    volatility = st.number_input("Entrez la volatilité", value=0.2)
    option_type = st.selectbox("Type d'option", ["Call", "Put"])
    num_simulations = st.number_input("Entrez le nombre de simulations", value=10000)
    if st.button("Calculer le prix"):
        # Logique pour calculer le pricing des options avec Monte Carlo
        st.write(f"Pricing {option_type} option avec Monte Carlo")


# Gestion de portefeuille
def show_portfolio_management():
    st.title("Gestion de Portefeuille")
    # Logique pour la gestion de portefeuille
    st.write("Module de gestion de portefeuille")


# Pricing des actifs dérivés
def show_derivative_pricing():
    st.title("Pricing des Actifs Dérivés")
    # Logique pour le pricing des actifs dérivés
    st.write("Module de pricing des actifs dérivés")


# Pricing des actifs classiques
def show_classic_asset_pricing():
    st.title("Pricing des Actifs Classiques")
    # Logique pour le pricing des actifs classiques
    st.write("Module de pricing des actifs classiques")


# Chaînes de Markov



# Page À Propos
def show_about():
    st.title("À Propos")
    st.write("Étudiant en Finance et Ingénierie Décisionnelle...")
    st.write("LinkedIn: [Mhamed Abdelhamid Bou](https://www.linkedin.com/in/mhamedabdelhamidbou/)")
