import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    # 1. Load Data
    print("Memuat dataset Wine Recognition...")
    data = load_wine()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target

    # 2. Split Data (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Preprocessing (Standardization)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 4. Inisialisasi Model
    svm_model = SVC(kernel='linear', random_state=42)
    knn_model = KNeighborsClassifier(n_neighbors=5)

    # 5. Training
    print("Melatih model SVM dan KNN...")
    svm_model.fit(X_train_scaled, y_train)
    knn_model.fit(X_train_scaled, y_train)

    # 6. Prediksi
    svm_pred = svm_model.predict(X_test_scaled)
    knn_pred = knn_model.predict(X_test_scaled)

    # 7. Evaluasi
    svm_acc = accuracy_score(y_test, svm_pred)
    knn_acc = accuracy_score(y_test, knn_pred)

    print(f"\nAkurasi SVM: {svm_acc:.4f}")
    print(f"Akurasi KNN: {knn_acc:.4f}")

    # 8. Visualisasi (Confusion Matrix)
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    
    sns.heatmap(confusion_matrix(y_test, svm_pred), annot=True, fmt='d', cmap='Blues', ax=ax[0])
    ax[0].set_title('Confusion Matrix - SVM')
    ax[0].set_xlabel('Prediksi Kelas')
    ax[0].set_ylabel('Aktual Kelas')

    sns.heatmap(confusion_matrix(y_test, knn_pred), annot=True, fmt='d', cmap='Greens', ax=ax[1])
    ax[1].set_title('Confusion Matrix - KNN')
    ax[1].set_xlabel('Prediksi Kelas')
    ax[1].set_ylabel('Aktual Kelas')

    plt.tight_layout()
    plt.savefig('visualisasi_wine.png')
    plt.show()

if __name__ == "__main__":
    main()