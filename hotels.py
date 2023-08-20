import streamlit as st
import pandas as pd

# Daten für die beiden Hotels und ihre Attribute
data = {
    'Hotel': ['TUI Blue', 'Melia Llana'],
    'Bewertung': [84, 82],
    'Wichtigkeit Susi': [0, 5],
    'Anzahl der Pools': [2, 2],
    'Anzahl Restaurants': [4, 4],
    'Anzahl Bars und Mehr': [4, 3],
    'Lobbybar': [1, 1],
    'Poolbar': [1, 1],
    'Strandbar': [1, 0],
    'Loungebar': [0, 1],
    'Anzahl Saunen': [1, 2],

    # Weitere Attribute hier hinzufügen
}

df = pd.DataFrame(data)

# App-Titel und Beschreibung
st.title('Hotelvergleichs-App :desert_island:')
st.write('Wähle die Attribute und gib die Wichtigkeit:')

# Attribut-Auswahl und Wichtigkeit
attributes = df.columns[1:]  # Ignoriere die Spalte 'Hotel'
weights = {}

for attribute in attributes:
    weights[attribute] = st.slider(f'{attribute}', 1, 10, 5)

# Berechnung der Gesamtbewertung für jedes Hotel
df['Gesamtbewertung'] = df[attributes].multiply(list(weights.values())).sum(axis=1)

# Anzeige des empfohlenen Hotels
recommended_hotel = df.loc[df['Gesamtbewertung'].idxmax(), 'Hotel']
st.write(f'Empfohlenes Hotel: {recommended_hotel}')

# Anzeige der Daten der beiden Hotels
st.write(df)
