import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt

def run_app():
    # Configuration de la page Streamlit

    # Titre de l'application
    st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 3em;
            color: #2E86C1;
            font-weight: bold;
        }
    </style>
    <h1 class='main-title'>📈 Pricing - Modèle de Heston</h1>
    """, unsafe_allow_html=True)

    # Disposition de la page en deux colonnes
    col1, col2 = st.columns([1, 2])

    # Section Pricing (colonne de gauche)
    with col1:
        st.header("💡 Pricing")

        # Inputs pour les paramètres communs
        st.markdown("<div style='background-color: #F2F3F4; padding: 10px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.subheader("🔧 Paramètres du Modèle")
        S = st.number_input("Prix de l'actif sous-jacent (S)", value=100.0)
        K = st.number_input("Prix d'exercice (K)", value=100.0)
        T = st.number_input("Temps jusqu'à maturité (T, en années)", value=1.0)
        r = st.number_input("Taux d'intérêt sans risque (r)", value=0.05)
        st.markdown("</div>", unsafe_allow_html=True)

        # Checkbox pour afficher les paramètres spécifiques au modèle de Heston
        show_heston_params = st.checkbox("Afficher les paramètres spécifiques au modèle de Heston", value=False)

        if show_heston_params:
            # Inputs spécifiques au modèle de Heston
            st.markdown("<div style='background-color: #F9EBEA; padding: 10px; border-radius: 10px;'>", unsafe_allow_html=True)
            st.subheader("⚙️ Paramètres spécifiques au modèle de Heston")
            v0 = st.number_input("Variance initiale (v0)", value=0.04)
            kappa = st.number_input("Taux de réversion (κ)", value=1.0)
            theta = st.number_input("Variance à long terme (θ)", value=0.04)
            rho = st.number_input("Corrélation (ρ)", value=-0.7)
            sigma_v = st.number_input("Volatilité de la variance (σ_v)", value=0.3)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            # Valeurs par défaut pour le modèle de Heston
            v0 = 0.04
            kappa = 1.0
            theta = 0.04
            rho = -0.7
            sigma_v = 0.3

        # Récupérer les options avancées
        st.markdown("<div style='background-color: #E8F8F5; padding: 10px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.subheader("🔧 Options avancées")
        num_simulations = st.slider("Nombre de simulations Monte-Carlo", min_value=100, max_value=5000, value=1000, step=100)
        dt = st.slider("Pas de temps (dt)", min_value=0.001, max_value=0.1, value=0.01, step=0.001)
        st.markdown("</div>", unsafe_allow_html=True)

        # Bouton pour calculer le prix avec Heston
        if st.button("🔍 Calculer le Prix avec Heston"):
            # Implémentation du pricing Heston
            def heston_price(S, K, T, r, v0, kappa, theta, rho, sigma_v, num_simulations, dt):
                N = int(T / dt)
                prices = []
                paths = []  # Pour la visualisation
                for _ in range(num_simulations):
                    ST = S
                    v = v0
                    path = [S]  # Pour stocker la trajectoire
                    for _ in range(N):
                        z1 = np.random.normal()
                        z2 = rho * z1 + np.sqrt(1 - rho ** 2) * np.random.normal()
                        v = np.abs(v + kappa * (theta - v) * dt + sigma_v * np.sqrt(v * dt) * z2)
                        ST = ST * np.exp((r - 0.5 * v) * dt + np.sqrt(v * dt) * z1)
                        path.append(ST)
                    payoff = max(ST - K, 0)
                    prices.append(payoff)
                    paths.append(path)
                price = np.exp(-r * T) * np.mean(prices)
                return price, prices, paths

            # Calcul du prix avec la fonction Heston
            price, simulated_prices, paths = heston_price(S, K, T, r, v0, kappa, theta, rho, sigma_v, num_simulations, dt)

            # Section Outputs (colonne de droite)
            with col2:
                st.header("📊 Résultats")
                # Affichage du prix calculé
                st.success(f"Le prix de l'option calculé avec le modèle de Heston est : **`{price:.2f}`**")

                # Visualisation des trajectoires simulées
                st.subheader("📈 Trajectoires simulées")
                fig = go.Figure()
                for path in paths[:10]:  # Limiter à 10 trajectoires pour la visualisation
                    fig.add_trace(go.Scatter(x=np.linspace(0, T, len(path)), y=path, mode='lines'))
                fig.update_layout(title="Trajectoires simulées de l'actif", xaxis_title="Temps (années)", yaxis_title="Prix",
                                  plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(255,255,255,1)', font=dict(size=14))
                st.plotly_chart(fig)

                # Graphique de distribution des prix simulés
                st.subheader("📉 Distribution des prix simulés")
                plt.figure(figsize=(10, 6))
                plt.hist(simulated_prices, bins=50, alpha=0.7, color='blue', edgecolor='black')
                plt.title('Distribution des prix simulés', fontsize=16, color='#34495E')
                plt.xlabel('Prix simulés', fontsize=14)
                plt.ylabel('Fréquence', fontsize=14)
                plt.grid(alpha=0.3)
                st.pyplot(plt)

# Lancer l'application
if __name__ == "__main__":
    run_app()
