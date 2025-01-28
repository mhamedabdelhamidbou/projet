import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def markov_chain_page():
    st.title("Simulation de Chaînes de Markov")

    # Paramètres de la chaîne de Markov
    states = st.text_input("États (séparés par des virgules)", "A,B,C")
    transition_matrix_input = st.text_area("Matrice de Transition (lignes séparées par des retours à la ligne)",
                                            "0.7,0.2,0.1\n0.1,0.8,0.1\n0.2,0.3,0.5")
    initial_state = st.selectbox("État initial", options=["A", "B", "C"])

    if st.button("Lancer la Simulation de Chaîne de Markov"):
        # Traitement des états et de la matrice de transition
        states = [state.strip() for state in states.split(",")]
        transition_matrix = np.array([[float(num) for num in line.split(",")] for line in transition_matrix_input.splitlines()])

        # Vérification de la validité de la matrice de transition
        if np.all(np.isclose(transition_matrix.sum(axis=1), 1)):
            # Simulation des transitions
            num_steps = st.number_input("Nombre d'étapes", value=10, min_value=1)
            current_state = initial_state
            state_history = [current_state]

            state_index = {state: index for index, state in enumerate(states)}
            for _ in range(num_steps):
                current_index = state_index[current_state]
                current_state = np.random.choice(states, p=transition_matrix[current_index])
                state_history.append(current_state)

            st.write("Historique des États : ", state_history)

            # Visualisation de la distribution des états
            unique_states, counts = np.unique(state_history, return_counts=True)
            fig_distribution = go.Figure()
            fig_distribution.add_trace(go.Bar(x=unique_states, y=counts, name='Fréquence des États'))
            fig_distribution.update_layout(
                title="Distribution des États après Simulation",
                xaxis_title="États",
                yaxis_title="Fréquence",
                template="plotly_white"
            )
            st.plotly_chart(fig_distribution)

            # Visualisation des transitions
            transition_counts = np.zeros((len(states), len(states)))
            for i in range(1, len(state_history)):
                prev_state = state_history[i-1]
                curr_state = state_history[i]
                transition_counts[state_index[prev_state], state_index[curr_state]] += 1

            fig_transition = go.Figure(data=[
                go.Heatmap(
                    z=transition_counts,
                    x=states,
                    y=states,
                    colorscale='Viridis',
                    hoverongaps=False
                )
            ])
            fig_transition.update_layout(
                title='Matrice de Transition des États',
                xaxis_title='État Suivant',
                yaxis_title='État Précédent'
            )
            st.plotly_chart(fig_transition)

            # Affichage des statistiques
            st.write("Statistiques sur les États :")
            for state, count in zip(unique_states, counts):
                st.write(f"État {state}: {count} fois ({(count / len(state_history)) * 100:.2f}%)")
        else:
            st.error("La matrice de transition doit être valide (les lignes doivent se sommer à 1).")

# Fonction principale
if __name__ == "__main__":
    markov_chain_page()
