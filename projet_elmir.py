import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from arch import arch_model
from statsmodels.tsa.stattools import adfuller
import plotly.graph_objects as go
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import io

st.set_page_config(layout="wide")

# Configuration de l'apparence de Seaborn
sns.set(style="whitegrid")

# Fonction pour charger les données à partir de Yahoo Finance
@st.cache_data
def load_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    data = data.reset_index()
    if 'Close' not in data.columns:
        st.error("Données indisponibles pour le symbole spécifié. Veuillez vérifier le symbole boursier et réessayer.")
        return pd.DataFrame()
    return data

# Fonction pour ajouter des indicateurs techniques
def add_technical_indicators(data):
    data['SMA_20'] = data['Close'].rolling(window=20).mean()  # Moyenne Mobile Simple 20 jours
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()  # Moyenne Mobile Exponentielle 20 jours
    return data

# Fonction pour tester la stationnarité
def test_stationarity(data):
    result = adfuller(data.dropna())
    return result[1]  # p-value

# Fonction pour ajuster le modèle GARCH
def fit_garch_model(data, p=1, q=1):
    model = arch_model(data.dropna(), vol='Garch', p=p, q=q)
    model_fit = model.fit(disp='off')
    return model_fit

# Fonction pour effectuer des prévisions de volatilité
def forecast_volatility(model_fit, steps=5):
    forecast = model_fit.forecast(horizon=steps)
    future_volatility = np.sqrt(forecast.variance.values[-1, :])
    return future_volatility

# Fonction pour tracer les indicateurs techniques
def plot_technical_indicators(data, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['SMA_20'], mode='lines', name='SMA 20 jours'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['EMA_20'], mode='lines', name='EMA 20 jours'))
    fig.update_layout(title=f'Indicateurs Techniques pour {ticker}', xaxis_title='Date', yaxis_title='Prix')
    st.plotly_chart(fig)

# Fonction pour créer un rapport PDF bien présenté
def create_pdf_report(ticker, data, model_summary, future_volatility):
    pdf_filename = f"volatility_report_{ticker}.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    report_title = f"Rapport de Volatilité pour {ticker}"
    formatted_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    header = Paragraph(report_title, styles["Title"])
    sub_header = Paragraph(f"Date et heure de génération du rapport : {formatted_date}", styles["Normal"])

    # Aperçu des données
    tickers_table_data = [['Date', 'Close']]
    tickers_table_data.extend([[str(value['Date']), str(value['Close'])] for _, value in data.head().iterrows()])
    tickers_table = Table(tickers_table_data, colWidths=[200, 200])
    tickers_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
    ]))

    # Résultats du modèle GARCH
    model_summary_paragraph = Paragraph("Résultats du Modèle GARCH:", styles['Heading2'])
    model_summary_text = Paragraph(model_summary.replace('\n', '<br />'), styles['Normal'])

    # Prévisions de Volatilité
    future_volatility_paragraph = Paragraph("Prévisions de Volatilité Future:", styles['Heading2'])
    future_volatility_data = [["Step", "Volatilité Prévue"]]
    future_volatility_data.extend([[str(step), f"{vol:.4f}"] for step, vol in enumerate(future_volatility, 1)])
    future_volatility_table = Table(future_volatility_data, colWidths=[100, 200])
    future_volatility_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
    ]))

    # Graphiques
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Close'], label='Close Price', color='blue')
    plt.plot(data['Date'], data['SMA_20'], label='SMA 20 jours', color='orange')
    plt.plot(data['Date'], data['EMA_20'], label='EMA 20 jours', color='green')
    plt.title(f'Indicateurs Techniques pour {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Prix')
    plt.legend()
    plt.tight_layout()
    plt.savefig('technical_indicators.png')
    plt.close()
    technical_graph = Image('technical_indicators.png', width=400, height=300)

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(future_volatility) + 1), future_volatility, marker='o', color='red')
    plt.title(f'Prévisions de Volatilité Futur pour {ticker}')
    plt.xlabel('Pas à Prévoir')
    plt.ylabel('Écart-Type Prévu')
    plt.tight_layout()
    plt.savefig('volatility_forecast.png')
    plt.close()
    volatility_forecast_graph = Image('volatility_forecast.png', width=400, height=300)

    # Contenu du rapport
    report_content = [
        header, sub_header, Spacer(1, 12),
        tickers_table, Spacer(1, 12),
        model_summary_paragraph, model_summary_text, Spacer(1, 12),
        future_volatility_paragraph, future_volatility_table, Spacer(1, 12),
        Paragraph("Graphiques:", styles["Heading2"]), technical_graph, Spacer(1, 12),
        volatility_forecast_graph
    ]

    doc.build(report_content)

    with open(pdf_filename, 'rb') as f:
        pdf_data = f.read()
    return pdf_data

# Interface Streamlit
st.title('Prédiction de la Volatilité des Marchés')

# Saisie de l'utilisateur
tickers = st.text_input('Entrez le symbole boursier (ex: AAPL)', 'AAPL')
start_date = st.date_input('Date de début', value=pd.to_datetime('2020-01-01'))
end_date = st.date_input('Date de fin', value=pd.to_datetime('2024-01-01'))

# Paramètres du modèle GARCH
# Paramètres du modèle GARCH
p = st.number_input('Ordre p (GARCH)', min_value=0, step=1, value=1)
q = st.number_input('Ordre q (ARCH)', min_value=0, step=1, value=1)

steps = st.number_input('Nombre de pas à prévoir:', min_value=1, max_value=30, value=5)

# Bouton pour lancer la simulation
if st.button("Lancer la Simulation"):
    # Traitement pour chaque ticker
    ticker_list = [tickers]
    for ticker in ticker_list:
        st.subheader(f"Analyse pour {ticker}")

        # Chargement des données
        data = load_data(ticker, start_date, end_date)

        if not data.empty:
            st.write("Aperçu des données:", data['Close'].head())

            # Analyse exploratoire
            st.subheader('Analyse Exploratoire des Données')
            st.line_chart(data.set_index('Date')['Close'])
            st.write("Statistiques descriptives:", data['Close'].describe())

            # Ajout des indicateurs techniques
            st.subheader('Indicateurs Techniques')
            data = add_technical_indicators(data)
            plot_technical_indicators(data, ticker)

            # Test de stationnarité
            p_value = test_stationarity(data['Close'])
            st.write(f"P-value du test ADF pour la stationnarité: {p_value}")

            # Ajustement du modèle GARCH
            st.subheader('Modèle de Volatilité GARCH')
            model_fit = fit_garch_model(data['Close'], p=p, q=q)
            st.write(model_fit.summary())

            # Prévisions de volatilité
            future_volatility = forecast_volatility(model_fit, steps)
            st.write("Prévisions de volatilité (écart-type):", future_volatility)

            # Génération du rapport PDF
            st.subheader("Rapport PDF")
            pdf_data = create_pdf_report(ticker, data, model_fit.summary().as_text(), future_volatility)
            st.download_button("Télécharger le rapport PDF", data=pdf_data, file_name=f"{ticker}_volatility_report.pdf")

