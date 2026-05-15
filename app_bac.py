import streamlit as st
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
