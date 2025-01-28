import streamlit as st
import random

# Utilisation de CSS pour styliser la page
def inject_custom_css():
    st.markdown(
        """
        <style>
        .main-header {
            font-size: 40px;
            text-align: center;
            font-weight: bold;
            color: #0000FF; /* Couleur bleue */
            margin-bottom: 30px;
        }
        .centered-header {
            text-align: center;
            font-size: 28px;
            font-weight: 600;
            margin-top: 30px;
            color: #0000FF; /* Couleur bleue */
        }
        .spacing {
            margin-bottom: 25px;
        }
        .highlighted-text {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
            font-style: italic;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            margin: 20px;
        }
        .contact-btn {
    display: block;
    width: 220px;
    margin: 0 auto;
    text-align: center;
    background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%); /* Dégradé moderne */
    color: white;
    padding: 15px 32px;
    text-decoration: none;
    font-size: 16px;
    border-radius: 30px;
    transition: transform 0.3s, background-color 0.3s;
    box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
}
.contact-btn:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #92FE9D 0%, #00C9FF 100%); /* Inverse du dégradé pour l'effet hover */
    box-shadow: 0px 12px 20px rgba(0, 0, 0, 0.2);
}

        </style>
        """,
        unsafe_allow_html=True,
    )

# Fonction centrale pour le rendu de la page 'À propos'
def about_us_page():
    inject_custom_css()

    # Section Titre
    st.markdown("<div class='main-header'>À propos de moi</div>", unsafe_allow_html=True)

    # Affichage de l'image (Centrée)
    st.image("pp.png", use_column_width=True)

    st.write("\n\n")  # Lignes vides pour espacement

    # Section Aide et Support
    st.markdown("<div class='centered-header'>Aide et Support</div>", unsafe_allow_html=True)
    st.write(
        """
        Pour toute question ou support technique, n'hésitez pas à me contacter à l'adresse suivante :
        - **Email:** mhamedabdelhamidbou@gmail.com
        Vous pouvez également me joindre via LinkedIn ou à travers mon site personnel pour toute question concernant mes projets actuels ou futurs.
        """)

    # Section Encadrement du Projet
    st.markdown("<div class='centered-header'>Encadrement du projet</div>", unsafe_allow_html=True)
    st.write(
        """
        Ce projet est réalisé sous l'encadrement de **Mr. Ibrahim El Asri** dans le cadre du module **Processus Aléatoires**.
        Grâce à son expertise, j'ai pu approfondir mes connaissances sur les processus stochastiques et leur application
        dans des contextes réels, notamment en finance. L'encadrement de Mr. El Asri a été fondamental pour la réussite
        de ce projet, et sa perspective m'a beaucoup inspiré dans l'approche analytique des problèmes.
        """)

    # Section Réalisé par
    st.markdown("<div class='centered-header'>Réalisé par</div>", unsafe_allow_html=True)
    st.write(
        """
        **Bou Mhamed Abdelhamid**, élève ingénieur en Finance et Ingénierie Décisionnelle à l'ENSA Agadir.
        Au cours de mes études, j'ai développé un fort intérêt pour les mathématiques financières et la modélisation des risques.
        J'ai travaillé sur de nombreux projets axés sur la finance quantitative, ce qui m'a permis de renforcer mes compétences
        en programmation, en analyse de données et en utilisation d'outils comme Python et R pour la prise de décision basée
        sur des modèles quantitatifs.
        """)

    # Section Notre École
    st.markdown("<div class='centered-header'>Notre École</div>", unsafe_allow_html=True)
    st.write(
        """
        En 1999, l'Université IBN ZOHR innove en ouvrant la première école d'ingénieurs de la région : l'ENSA-AGADIR.
        C'est un établissement de formation d'ingénieurs qui offre, en cinq ans, aux jeunes bacheliers scrupuleusement
        sélectionnés, une formation professionnelle, diversifiée, complète et relativement polyvalente.
        L'ENSA Agadir est reconnue pour son excellence académique et son ouverture vers les nouvelles technologies, formant
        des ingénieurs capables de répondre aux besoins croissants du marché, tant au niveau national qu'international.
        """)

    # Section Notre Programme
    st.markdown("<div class='centered-header'>Notre Programme</div>", unsafe_allow_html=True)
    st.write(
        """
        La filière « Finance et Ingénierie décisionnelle » a pour finalité de former des ingénieurs qualifiés en finance
        de marché, gestion des risques, gestion de portefeuille en maîtrisant les outils mathématiques de modélisation
        et économétriques d'aide à la décision.
        Ce programme vise à doter les étudiants d'une base solide en analyse financière, en mathématiques appliquées,
        et en programmation, permettant ainsi une approche quantitative des problématiques financières. Nous travaillons
        également sur des projets en collaboration avec des entreprises du secteur financier, ce qui nous permet de
        développer des compétences pratiques adaptées aux réalités du marché.
        """)

    # Section À Propos de Moi
    st.markdown("<div class='centered-header'>À Propos de Moi</div>", unsafe_allow_html=True)
    st.write(
        """
        Étudiant en Finance et Ingénierie Décisionnelle, je suis passionné par l'apprentissage continu et l'acquisition
        de compétences en programmation et en finance, avec une motivation forte. Mon intérêt particulier réside dans
        la finance quantitative et la gestion d'actifs.
        Je suis également un fervent adepte de l'intelligence artificielle et de l'automatisation, que j'aime appliquer
        pour résoudre des problèmes financiers complexes. J'ai participé à plusieurs concours de programmation et à des
        hackathons, où j'ai eu l'occasion de développer des solutions innovantes dans des délais limités, tout en travaillant
        en équipe avec des personnes partageant les mêmes intérêts.
        """)

    # Section Contact
    st.markdown("<div class='centered-header'>Contact</div>", unsafe_allow_html=True)
    st.write(
        """
        N'hésitez pas à me contacter pour des propositions, des projets ou des remarques. Vous pouvez me retrouver sur
        [LinkedIn](https://www.linkedin.com/in/mhamedabdelhamidbou/). J'aime collaborer sur des projets innovants,
        particulièrement ceux qui touchent aux finances, à l'analyse de données ou à la technologie.
        """)

    # Ajouter un bouton pour un engagement utilisateur
    contact_button = "<a href='https://mhamedabdelhamidbou.github.io/bou/#' class='contact-btn'>En savoir plus sur mes projets</a>"
    st.markdown(contact_button, unsafe_allow_html=True)

    # Ajouter une citation aléatoire pour rendre la page dynamique
    quotes = [
        "La persévérance est la clé du succès.",
        "L'éducation est l'arme la plus puissante pour changer le monde. - Nelson Mandela",
        "Ne cessez jamais d'apprendre, car la vie ne cesse jamais d'enseigner.",
        "Le succès n'est pas final, l'échec n'est pas fatal : c'est le courage de continuer qui compte. - Winston Churchill",
        "Il faut toujours viser la lune, car même en cas d'échec, on atterrit dans les étoiles. - Oscar Wilde"
    ]
    random_quote = random.choice(quotes)
    st.markdown(f"<div class='highlighted-text'>{random_quote}</div>", unsafe_allow_html=True)

# Appel de la fonction principale
if __name__ == "__main__":
    about_us_page()
