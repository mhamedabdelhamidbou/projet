import streamlit as st
import numpy as np
from scipy.stats import norm


# Configuration de la page
st.set_page_config(page_title="💸 Pricing de Produits Dérivés et Structurés", layout="wide")
st.title("💸 Pricing de Produits Dérivés et Structurés")

# Menu déroulant pour sélectionner le produit
produit = st.selectbox(
    "Choisissez le produit dérivé ou structuré à pricer :",
    [
        "Options Européennes (Call et Put)",
        "Options Américaines",
        "Options Asiatiques",
        "Options Barrières",
        "Options Lookback",
        "Options Digitales",
        "Options Rainbow",
        "Options Cliquet",
        "Convertible Bonds",
        "Autocallables",
        "Swaps de Taux d'Intérêt",
        "Credit Default Swaps (CDS)"
    ]
)

st.write("---")

### Fonctions de pricing

# 1. Options Européennes (Black-Scholes et Monte Carlo)
def european_option_pricing():
    st.subheader("Pricing d'Options Européennes (Call et Put)")
    S = st.number_input("Prix initial de l'actif sous-jacent (S₀)", value=100.0)
    K = st.number_input("Prix d'exercice (K)", value=100.0)
    T = st.number_input("Temps à maturité (T, en années)", value=1.0)
    r = st.number_input("Taux d'intérêt sans risque (r)", value=0.05)
    sigma = st.number_input("Volatilité (σ)", value=0.2)
    method = st.radio("Méthode de calcul", ["Black-Scholes", "Monte Carlo"])

    if method == "Black-Scholes":
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        st.write(f"Prix de l'option Call : **{call_price:.2f}**")
        st.write(f"Prix de l'option Put : **{put_price:.2f}**")

    elif method == "Monte Carlo":
        simulations = st.slider("Nombre de simulations Monte Carlo", 1000, 50000, 10000)
        final_prices = S * np.exp(
            (r - 0.5 * sigma**2) * T + sigma * np.random.normal(0, np.sqrt(T), simulations)
        )
        call_payoff = np.maximum(final_prices - K, 0)
        put_payoff = np.maximum(K - final_prices, 0)
        call_price = np.mean(call_payoff) * np.exp(-r * T)
        put_price = np.mean(put_payoff) * np.exp(-r * T)
        st.write(f"Prix de l'option Call (Monte Carlo) : **{call_price:.2f}**")
        st.write(f"Prix de l'option Put (Monte Carlo) : **{put_price:.2f}**")

# 2. Options Américaines
def american_option_pricing():
    st.subheader("Pricing d'Options Américaines")
    st.write("📌 Implémentation avec la méthode Least Squares Monte Carlo à venir.")

# 3. Options Asiatiques
def asian_option_pricing():
    st.subheader("Pricing d'Options Asiatiques")
    st.write("📌 Implémentation en cours.")

# 4. Options Barrières
def barrier_option_pricing():
    st.subheader("Pricing d'Options Barrières")
    st.write("📌 Implémentation en cours.")

# 5. Options Lookback
def lookback_option_pricing():
    st.subheader("Pricing d'Options Lookback")
    st.write("📌 Implémentation en cours.")

# 6. Options Digitales
def digital_option_pricing():
    st.subheader("Pricing d'Options Digitales (Paiement binaire)")
    S = st.number_input("Prix initial de l'actif sous-jacent (S₀)", value=100.0)
    K = st.number_input("Prix d'exercice (K)", value=100.0)
    T = st.number_input("Temps à maturité (T, en années)", value=1.0)
    r = st.number_input("Taux d'intérêt sans risque (r)", value=0.05)
    sigma = st.number_input("Volatilité (σ)", value=0.2)
    payoff = st.selectbox("Type de payoff", ["Call Digital", "Put Digital"])

    d2 = (np.log(S / K) + (r - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

    if payoff == "Call Digital":
        price = np.exp(-r * T) * norm.cdf(d2)
        st.write(f"Prix de l'option Call Digital : **{price:.2f}**")
    else:
        price = np.exp(-r * T) * norm.cdf(-d2)
        st.write(f"Prix de l'option Put Digital : **{price:.2f}**")

# 7. Options Rainbow
def rainbow_option_pricing():
    st.subheader("Pricing d'Options Rainbow (Multi-actifs)")
    st.write("📌 Implémentation en cours.")

# 8. Options Cliquet
def cliquet_option_pricing():
    st.subheader("Pricing d'Options Cliquet")
    st.write("📌 Implémentation en cours.")

# 9. Convertible Bonds
def convertible_bond_pricing():
    st.subheader("Pricing de Convertible Bonds")
    st.write("📌 Implémentation en cours.")

# 10. Autocallables
def autocallable_pricing():
    st.subheader("Pricing d'Autocallables")
    st.write("📌 Implémentation en cours.")

# 11. Swaps de Taux d'Intérêt
def interest_rate_swap_pricing():
    st.subheader("Pricing de Swaps de Taux d'Intérêt")
    st.write("📌 Implémentation en cours.")

# 12. Credit Default Swaps (CDS)
def cds_pricing():
    st.subheader("Pricing de Credit Default Swaps (CDS)")
    st.write("📌 Implémentation en cours.")

### Gestion du choix de produit
if produit == "Options Européennes (Call et Put)":
    european_option_pricing()
elif produit == "Options Américaines":
    american_option_pricing()
elif produit == "Options Asiatiques":
    asian_option_pricing()
elif produit == "Options Barrières":
    barrier_option_pricing()
elif produit == "Options Lookback":
    lookback_option_pricing()
elif produit == "Options Digitales":
    digital_option_pricing()
elif produit == "Options Rainbow":
    rainbow_option_pricing()
elif produit == "Options Cliquet":
    cliquet_option_pricing()
elif produit == "Convertible Bonds":
    convertible_bond_pricing()
elif produit == "Autocallables":
    autocallable_pricing()
elif produit == "Swaps de Taux d'Intérêt":
    interest_rate_swap_pricing()
elif produit == "Credit Default Swaps (CDS)":
    cds_pricing()
else:
    st.warning("Cette option n'est pas encore implémentée.")
