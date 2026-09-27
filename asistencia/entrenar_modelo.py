from deepface import DeepFace
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
import os
import cv2
import joblib

def train_classifier_knn(dataset_path='dataset', model_name='VGG-Face'):
    if not os.path.exists(dataset_path) or len(os.listdir(dataset_path)) < 2:
        print("Error: Se requieren al menos 2 personas en carpetas distintas para entrenar.")
        return

    X, y = [], []
    for person_name in os.listdir(dataset_path):
        person_dir = os.path.join(dataset_path, person_name)
        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            img = cv2.imread(img_path)
            if img is None:
                continue
            try:
                embedding = DeepFace.represent(
                    img, model_name=model_name,
                    enforce_detection=True,
                    detector_backend='opencv'
                )[0]['embedding']
                X.append(embedding)
                y.append(person_name)
            except Exception as e:
                print(f"Error procesando {img_path}: {e}")
                continue

    if len(set(y)) < 2:
        print("Error: Se requieren imágenes válidas de al menos 2 personas distintas.")
        return

    if len(X) == 0:
        print("Error: No se pudieron generar embeddings.")
        return

    X = np.array(X)
    y = np.array(y)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_scaled, y)

    joblib.dump(clf, 'knn_vggface_classifier.joblib')
    joblib.dump(scaler, 'scaler.joblib')
    print("✅ Modelo entrenado y guardado exitosamente.")

if __name__ == "__main__":
    train_classifier_knn()
