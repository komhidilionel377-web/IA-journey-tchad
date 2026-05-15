sommeil_hours = sleep # on prend la valeur du sommeil actuelimport streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("🎓 Prédicteur de note au Bac - Tchad")
st.write("Entre tes heures de révision et de sommeil")

X = np.array([[2, 5], [4, 6], [6, 7], [8, 8], [10, 9]])
y = np.array([8, 11, 14, 16, 18])

model = LinearRegression()
model.fit(X, y)

revisions = st.slider("Heures de révision/jour", 0, 12, 5)
sommeil = st.slider("Heures de sommeil", 0, 12, 7)

if st.button("Prédire ma note"):
    prediction = model.predict([[revisions, sommeil]])[0]
    st.success(f"Note prédite : {prediction:.1f}/20")
    if prediction >= 10:
        st.balloons()
import matplotlib.pyplot as plt
import numpy as np

if st.button("Voir la courbe de progression"):
    sommeil_hours = sleep # on prend la valeur du slider sommeil actuel
    revision_range = np.arange(0, 11, 1)
    
    # On prédit la note pour chaque heure de révision
    predicted_notes = []
    for r in revision_range:
        note = model.predict([[r, sleep_hours]])[0]
        predicted_notes.append(note)
    
    # Graphique
    fig, ax = plt.subplots()
    ax.plot(revision_range, predicted_notes, marker='o', color='#1E90FF')
    ax.set_xlabel("Heures de révision/jour")
    ax.set_ylabel("Note prédite au Bac")
    ax.set_title(f"Évolution de la note pour {sleep_hours}h de sommeil")
    ax.grid(True)
    ax.set_ylim(0, 20)
    
    st.pyplot(fig)
    st.write("💡 Astuce : Vise le point où la courbe commence à stagner. C’est ton sweet spot.")
