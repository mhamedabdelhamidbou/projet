import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.figure_factory as ff


def monte_carlo_simulation(initial_investment, mean_return, volatility, time_horizon, num_simulations,
                           yearly_contribution=0, withdrawal_rate=0):
    np.random.seed(42)
    results = []
    for _ in range(num_simulations):
        prices = [initial_investment]
        for year in range(time_horizon):
            next_price = prices[-1] * np.exp((mean_return - 0.5 * volatility ** 2) + volatility * np.random.normal())
            next_price += yearly_contribution
            next_price -= next_price * withdrawal_rate
            prices.append(next_price)
        results.append(prices)
    return results


# Streamlit app
def show_monte_carlo():
    st.title("💸 Simulation Monte Carlo pour l'investissement 💹")
    st.markdown(
        "<style>body {background-color: #f0f2f6;} .sidebar .sidebar-content {background-color: #f9fafb;}</style>",
        unsafe_allow_html=True)

    # Input parameters
    st.write("### 🛠️ Paramètres de la Simulation")
    initial_investment = st.number_input("💰 Investissement Initial (en euros)", min_value=1000, value=10000, step=1000)
    mean_return = st.slider("📈 Retour Moyen Annuel (%)", min_value=-10.0, max_value=20.0, value=5.0, step=0.1) / 100
    volatility = st.slider("📊 Volatilité Annuel (%)", min_value=0.0, max_value=50.0, value=15.0, step=0.1) / 100
    time_horizon = st.slider("⏳ Horizon Temporel (années)", min_value=1, max_value=50, value=10)
    num_simulations = st.slider("🔁 Nombre de Simulations", min_value=100, max_value=5000, value=1000, step=100)
    yearly_contribution = st.number_input("💵 Contribution Annuelle (en euros)", min_value=0, value=1000, step=100)
    withdrawal_rate = st.slider("🏦 Taux de Retrait Annuel (%)", min_value=0.0, max_value=20.0, value=0.0,
                                step=0.1) / 100
    target_value = st.number_input("🎯 Objectif d'Investissement (en euros)", min_value=0, value=50000, step=1000)

    # Button to run simulation
    if st.button("🚀 Lancer la Simulation"):
        # Running Monte Carlo simulation
        st.write("### 🎲 Résultats de la Simulation Monte Carlo")
        simulations = monte_carlo_simulation(initial_investment, mean_return, volatility, time_horizon, num_simulations,
                                             yearly_contribution, withdrawal_rate)

        # Convert results to DataFrame for easier plotting
        df = pd.DataFrame(simulations).T

        # Plotting the results with Plotly
        fig = go.Figure()
        colors = ['rgba(0, 123, 255, 0.1)', 'rgba(255, 99, 132, 0.1)', 'rgba(40, 167, 69, 0.1)',
                  'rgba(255, 193, 7, 0.1)', 'rgba(23, 162, 184, 0.1)']
        for i in range(df.shape[1]):
            color = colors[i % len(colors)]  # Cycle through different colors
            fig.add_trace(go.Scatter(x=list(range(time_horizon + 1)), y=df[i], mode='lines', line=dict(color=color),
                                     name=f'Simulation {i + 1}'))

        fig.update_layout(
            title="📊 Simulation Monte Carlo des Trajectoires de l'Investissement",
            xaxis_title="🗓️ Années",
            yaxis_title="💶 Valeur de l'Investissement (en euros)",
            template="plotly_white",
            showlegend=False
        )
        st.plotly_chart(fig)

        # Calcul de statistiques
        final_values = df.iloc[-1]
        mean_final_value = np.mean(final_values)
        median_final_value = np.median(final_values)
        worst_case = np.percentile(final_values, 5)
        best_case = np.percentile(final_values, 95)

        st.write(f"💡 La valeur moyenne finale de l'investissement est de **{mean_final_value:,.2f} €**.")
        st.write(f"💡 La valeur médiane finale de l'investissement est de **{median_final_value:,.2f} €**.")
        st.write(f"⚠️ Dans le pire des cas (5ème percentile), l'investissement vaut **{worst_case:,.2f} €**.")
        st.write(f"✨ Dans le meilleur des cas (95ème percentile), l'investissement vaut **{best_case:,.2f} €**.")

        # Afficher une distribution des valeurs finales avec Plotly
        st.write("### 📈 Distribution des Valeurs Finales de l'Investissement")
        hist_data = [final_values]
        group_labels = ['Valeurs Finales']
        fig2 = ff.create_distplot(hist_data, group_labels, bin_size=500, colors=['#20c997'])
        fig2.update_layout(
            title="🔍 Distribution des Valeurs Finales de l'Investissement",
            xaxis_title="💶 Valeur de l'Investissement (en euros)",
            yaxis_title="📊 Fréquence",
            template="plotly_white"
        )
        st.plotly_chart(fig2)

        # Probability of Meeting a Target
        prob_meeting_target = np.mean(final_values >= target_value) * 100
        st.write(
            f"🎯 La probabilité d'atteindre l'objectif d'investissement de **{target_value:,.2f} €** est de **{prob_meeting_target:.2f}%**.")


if __name__ == "__main__":
    show_monte_carlo()
