from sklearn.datasets import load_sample_images
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Charge 2 images d'exemple : une de fleurs, une de chat
images = load_sample_images()
X = [img.reshape(-1) for img in images.images]
y = [0, 1] # 0 = fleur, 1 = chat

# Entraine le modèle
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X, y)

print("=== Classificateur d'images ===")
print("Modèle entrainé sur des images d'exemple")
print("0 = Fleur, 1 = Chat")

# Teste avec une nouvelle image
prediction = model.predict([X[1]])
print(f"Prédiction : {'Chat' if prediction[0]==1 else 'Fleur'}")
