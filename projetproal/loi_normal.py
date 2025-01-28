import numpy as np
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Fonction pour simuler une loi normale
def simulate_normal_distribution(mean, std_dev, num_simulations):
    return np.random.normal(mean, std_dev, num_simulations)

# Fonction pour simuler une loi uniforme
def simulate_uniform_distribution(a, b, num_simulations):
    return np.random.uniform(a, b, num_simulations)

# Fonction pour simuler une loi exponentielle
def simulate_exponential_distribution(scale, num_simulations):
    return np.random.exponential(scale, num_simulations)

# Fonction pour simuler une loi de Poisson
def simulate_poisson_distribution(lam, num_simulations):
    return np.random.poisson(lam, num_simulations)

# Fonction pour simuler une loi binomiale
def simulate_binomial_distribution(n, p, num_simulations):
    return np.random.binomial(n, p, num_simulations)

# Fonction principale pour afficher l'interface et les résultats de la simulation
def show_distribution_simulation():
    st.header("🌟 Simulation de Différentes Lois de Probabilité")

    # Custom CSS for more advanced styling
    st.markdown(
        """
        <style>
        .main {
            background: linear-gradient(to right, #ece9e6, #ffffff);
            padding: 0 20px;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #ff1e1e;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ff6347;
        }
        .stat-container {
            background: #f0f0f0;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Choix de la loi de probabilité
    distribution_type = st.selectbox("✨ Choisissez la loi de probabilité à simuler :", ["Normale", "Uniforme", "Exponentielle", "Poisson", "Binomiale"])

    # Entrée des paramètres en fonction de la loi choisie
    if distribution_type == "Normale":
        mean = st.number_input('📉 Entrez la moyenne', value=0.0)
        std_dev = st.number_input('📊 Entrez l\'écart type', value=1.0)
        num_simulations = st.number_input('🔄 Entrez le nombre de simulations', value=1000, step=1)
        results = simulate_normal_distribution(mean, std_dev, num_simulations)
    elif distribution_type == "Uniforme":
        a = st.number_input('📍 Entrez la borne inférieure (a)', value=0.0)
        b = st.number_input('📍 Entrez la borne supérieure (b)', value=1.0)
        num_simulations = st.number_input('🔄 Entrez le nombre de simulations', value=1000, step=1)
        results = simulate_uniform_distribution(a, b, num_simulations)
    elif distribution_type == "Exponentielle":
        scale = st.number_input("📈 Entrez le paramètre d'échelle (scale)", value=1.0)
        num_simulations = st.number_input('🔄 Entrez le nombre de simulations', value=1000, step=1)
        results = simulate_exponential_distribution(scale, num_simulations)
    elif distribution_type == "Poisson":
        lam = st.number_input("🔢 Entrez le taux moyen d'occurrence (lambda)", value=1.0)
        num_simulations = st.number_input('🔄 Entrez le nombre de simulations', value=1000, step=1)
        results = simulate_poisson_distribution(lam, num_simulations)
    elif distribution_type == "Binomiale":
        n = st.number_input("🧮 Entrez le nombre d'essais (n)", value=10, step=1)
        p = st.number_input("📊 Entrez la probabilité de succès (p)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        num_simulations = st.number_input('🔄 Entrez le nombre de simulations', value=1000, step=1)
        results = simulate_binomial_distribution(n, p, num_simulations)

    # Simulation et affichage du graphique si l'utilisateur clique sur 'Simuler'
    if st.button('🚀 Simuler'):
        # Statistiques de base
        st.markdown("<div class='stat-container'>", unsafe_allow_html=True)
        st.write(f"**Moyenne des résultats**: {np.mean(results):.4f}")
        st.write(f"**Écart type des résultats**: {np.std(results):.4f}")
        st.write(f"**Médiane des résultats**: {np.median(results):.4f}")
        st.write(f"**Maximum des résultats**: {np.max(results):.4f}")
        st.write(f"**Minimum des résultats**: {np.min(results):.4f}")
        st.write(f"**Asymétrie (Skewness) des résultats**: {np.mean((results - np.mean(results))**3) / np.std(results)**3:.4f}")
        st.write(f"**Kurtosis des résultats**: {np.mean((results - np.mean(results))**4) / np.std(results)**4 - 3:.4f}")
        st.markdown("</div>", unsafe_allow_html=True)

        # Affichage du graphique avec Plotly
        fig = px.histogram(results, nbins=50, title=f'📊 Histogramme de la distribution {distribution_type} simulée',
                           labels={'value': 'Valeurs simulées'}, opacity=0.75, color_discrete_sequence=['#FFA07A'])
        fig.update_layout(bargap=0.1, xaxis_title='Valeurs', yaxis_title='Fréquence', template="plotly_white")
        fig.update_traces(marker_line_width=2, marker_line_color='#ff4500')
        st.plotly_chart(fig)

        # Affichage du graphique avec Seaborn pour une vue alternative
        plt.figure(figsize=(10, 6))
        sns.histplot(results, kde=True, bins=50, color='green', alpha=0.6)
        plt.title(f'📊 Histogramme et densité de la distribution {distribution_type} simulée', fontsize=16, color='#ff4500')
        plt.xlabel('Valeurs simulées', fontsize=14)
        plt.ylabel('Fréquence', fontsize=14)
        plt.grid(True, linestyle='--', linewidth=0.5)
        st.pyplot(plt)

        # Boîte à moustaches pour visualiser la distribution
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=results, color='purple')
        plt.title(f'📦 Boîte à moustaches de la distribution {distribution_type} simulée', fontsize=16, color='#ff6347')
        plt.xlabel('Valeurs simulées', fontsize=14)
        st.pyplot(plt)

        # Affichage d'un graphique QQ-plot pour vérifier la normalité (pour la loi normale uniquement)
        if distribution_type == "Normale":
            from scipy import stats
            plt.figure(figsize=(10, 6))
            stats.probplot(results, dist="norm", plot=plt)
            plt.title('🔍 QQ-plot pour vérifier la normalité des données simulées', fontsize=16, color='#4682B4')
            st.pyplot(plt)

    # Explications supplémentaires avec icônes pour attirer l'attention
    if distribution_type == "Normale":
        st.write("""
        ### 📘 Loi Normale
        La loi normale, aussi appelée distribution de Gauss, est une distribution de probabilité continue qui est souvent utilisée pour modéliser des variables naturelles comme les tailles humaines, les notes d'examen, ou les fluctuations des prix des actifs financiers.
        La moyenne (mean) représente la valeur centrale attendue, et l'écart-type (standard deviation) représente la dispersion autour de cette moyenne.
        """)
    elif distribution_type == "Uniforme":
        st.write("""
        ### 📗 Loi Uniforme
        La loi uniforme est une distribution de probabilité où chaque valeur dans un intervalle spécifié a une probabilité égale d'être observée. Elle est souvent utilisée pour modéliser des phénomènes où il n'y a pas de biais ou de tendance, par exemple pour générer des nombres aléatoires.
        """)
    elif distribution_type == "Exponentielle":
        st.write("""
        ### 📙 Loi Exponentielle
        La loi exponentielle est utilisée pour modéliser le temps entre des événements qui se produisent de manière continue et indépendamment à un taux constant. Elle est souvent utilisée en fiabilité et en file d'attente pour modéliser des temps d'attente.
        """)
    elif distribution_type == "Poisson":
        st.write("""
        ### 📘 Loi de Poisson
        La loi de Poisson est utilisée pour modéliser le nombre d'événements qui se produisent dans un intervalle de temps fixe. Elle est souvent utilisée pour des événements rares, comme le nombre d'accidents de voiture par jour.
        """)
    elif distribution_type == "Binomiale":
        st.write("""
        ### 📗 Loi Binomiale
        La loi binomiale est utilisée pour modéliser le nombre de succès dans une séquence d'essais indépendants, chacun ayant une probabilité fixe de succès. Elle est souvent utilisée dans des situations où il y a un nombre défini d'essais, comme le nombre de fois où une pièce tombe sur face après l'avoir lancée plusieurs fois.
        """)

# Lancer l'application Streamlit
if __name__ == '__main__':
    show_distribution_simulation()
