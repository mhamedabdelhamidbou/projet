import numpy as np
import streamlit as st
import plotly.graph_objs as go

# Function to simulate multiple paths of Brownian motion (vectorized)
def simulate_multiple_brownian_paths(mu, sigma, T, n, X0, num_paths):
    dt = T / n
    t = np.linspace(0, T, n)
    dW = np.random.normal(0, np.sqrt(dt), (num_paths, n))
    X = np.zeros((num_paths, n))
    X[:, 0] = X0
    for i in range(1, n):
        X[:, i] = X[:, i - 1] + mu * dt + sigma * dW[:, i]
    return t, X

# Main function to display the page
def show_brownian():
    st.title("\U0001F30A Simulation de Mouvement Brownien")

    # Input fields for simulation parameters
    st.header("\u2728 Paramètres de la Simulation")
    movement_type = st.selectbox("\U0001F31F Choisir le type de mouvement :",
                                 ["Avec Dérive", "Sans Dérive", "Mouvement Géométrique Brownien",
                                  "Mouvement Ornstein-Uhlenbeck"])

    mu = 0.0
    if movement_type == "Avec Dérive":
        mu = st.number_input("\U0001F4C8 Dérive (mu)", value=0.05, step=0.01)
    sigma = st.number_input("\U0001F500 Volatilité (sigma)", value=0.3, step=0.01)
    T = st.number_input("\u23F3 Temps total (T)", value=2.0, step=0.1)
    n = st.number_input("\U0001F4CA Nombre de points (n)", value=500, step=10)
    X0 = st.number_input("\U0001F4CD Position initiale (X0)", value=1.0, step=0.1)
    num_paths = st.number_input("\U0001F6F4 Nombre de trajectoires à simuler", value=10, step=1)

    # Button to run the simulation
    if st.button("\U0001F680 Simuler"):
        # Handle different types of Brownian motion
        if movement_type == "Sans Dérive":
            mu = 0.0
            t, paths = simulate_multiple_brownian_paths(mu, sigma, T, n, X0, num_paths)
        elif movement_type == "Avec Dérive":
            t, paths = simulate_multiple_brownian_paths(mu, sigma, T, n, X0, num_paths)
        elif movement_type == "Mouvement Géométrique Brownien":
            t = np.linspace(0, T, n)
            dt = T / n
            paths = []
            for _ in range(num_paths):
                W = np.cumsum(np.random.normal(0, np.sqrt(dt), n))
                X = X0 * np.exp((mu - 0.5 * sigma ** 2) * t + sigma * W)
                paths.append(X)
        elif movement_type == "Mouvement Ornstein-Uhlenbeck":
            theta = st.number_input("\u2696\uFE0F Taux de réversion (theta)", value=0.5, step=0.01)
            mu_long = st.number_input("\U0001F3AF Moyenne à long terme (mu_long)", value=0.0, step=0.1)
            t = np.linspace(0, T, n)
            dt = T / n
            paths = []
            for _ in range(num_paths):
                X = np.zeros(n)
                X[0] = X0
                for i in range(1, n):
                    dW = np.random.normal(0, np.sqrt(dt))
                    X[i] = X[i - 1] + theta * (mu_long - X[i - 1]) * dt + sigma * dW
                paths.append(X)

        # Create interactive graph with Plotly
        fig = go.Figure()

        for i, X in enumerate(paths):
            fig.add_trace(go.Scatter(
                x=t,
                y=X,
                mode='lines',
                name=f"Trajectoire {i + 1}",
                line=dict(width=1.5, dash='solid')  # Reduced line width for better visualization on smaller screens
            ))

        # Layout configuration for the graph
        fig.update_layout(
            title="\u2728 Simulation de Mouvement Brownien",
            xaxis_title="Temps",
            yaxis_title="Position",
            showlegend=True,
            template="plotly_white",  # Use a clean white template
            height=500,  # Reduced height for better visualization on smaller screens
            xaxis=dict(showline=True, linewidth=1, linecolor='black', mirror=True),
            yaxis=dict(showline=True, linewidth=1, linecolor='black', mirror=True),
        )

        # Display the plot with Streamlit
        st.plotly_chart(fig, use_container_width=True)

        # Show statistics on the paths
        final_positions = [X[-1] for X in paths]
        mean_final_position = np.mean(final_positions)
        std_final_position = np.std(final_positions)

        # Using columns to improve layout
        col1, col2 = st.columns(2)
        with col1:
            st.metric("\U0001F4CA Position finale moyenne", f"{mean_final_position:.2f}")
        with col2:
            st.metric("\U0001F4C8 \u00c9cart-type de la position finale", f"{std_final_position:.2f}")

        # Corrected Histogram of final positions using Plotly
        hist_fig = go.Figure()
        hist_fig.add_trace(go.Histogram(
            x=final_positions,
            nbinsx=15,  # Reduced number of bins for better visibility on smaller scales
            marker=dict(color='blue'),
            opacity=0.6
        ))

        # Adding lines for mean and standard deviation
        hist_fig.add_shape(type="line", x0=mean_final_position, x1=mean_final_position, y0=0, y1=1,
                           line=dict(color="red", dash="dash"), xref='x', yref='paper', name="Moyenne")
        hist_fig.add_shape(type="line", x0=mean_final_position + std_final_position, x1=mean_final_position + std_final_position, y0=0, y1=1,
                           line=dict(color="green", dash="dash"), xref='x', yref='paper', name="Moyenne + Écart-type")
        hist_fig.add_shape(type="line", x0=mean_final_position - std_final_position, x1=mean_final_position - std_final_position, y0=0, y1=1,
                           line=dict(color="green", dash="dash"), xref='x', yref='paper', name="Moyenne - Écart-type")



    # Additional explanations
    with st.expander("En savoir plus sur le Mouvement Brownien"):
        st.write("""
        ### \U0001F9E0 Mouvement Brownien en Finance
        En finance, le mouvement brownien est utilisé pour modéliser les fluctuations des prix des actifs financiers, 
        tels que les actions, les devises, et autres instruments financiers. Les modèles financiers tels que le 
        modèle de Black-Scholes utilisent le mouvement brownien pour évaluer les options et autres produits dérivés.

        Le mouvement brownien avec dérive représente la tendance générale du marché (hausse ou baisse), 
        tandis que la volatilité représente l'incertitude ou les fluctuations autour de cette tendance.
        """)

        st.write("""
        ### ✨ Types de Mouvement Brownien
        - **Mouvement Brownien Simple** : Mouvement aléatoire sans dérive, représentant des fluctuations imprévisibles sans tendance spécifique.
        - **Mouvement Brownien avec Dérive** : Ajoute une composante de dérive (tendance) pour représenter un changement moyen dans une direction donnée.
        - **Mouvement Géométrique Brownien** : Utilisé en finance pour modéliser le prix des actifs, il inclut la dérive et la volatilité en exponentiel, garantissant que le prix reste positif.
        - **Mouvement Ornstein-Uhlenbeck** : Processus de réversion vers la moyenne, souvent utilisé pour modéliser les taux d'intérêt ou d'autres variables financières qui ont tendance à revenir à une valeur moyenne au fil du temps.
        """)

        st.write("""
        ### ⚙️ Paramètres de la Simulation
        - **Dérive (mu)** : Le taux moyen de changement de la position au fil du temps. En finance, cela représente le rendement moyen attendu d'un actif.
        - **Volatilité (sigma)** : La quantité d'aléa ou d'incertitude dans le mouvement. En finance, cela représente le risque ou la variabilité du prix de l'actif.
        - **Temps total (T)** : La période totale de la simulation.
        - **Position initiale (X0)** : La valeur de départ de la simulation.
        - **Nombre de trajectoires** : Le nombre de chemins simulés pour observer la distribution des résultats finaux.
        """)

# Call the function to display the page
if __name__ == "__main__":
    show_brownian()
