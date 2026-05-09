# 🚢 Titanic Survival Prediction using SVM

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-F7931E.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> An interactive machine learning web application that predicts passenger survival on the Titanic using Support Vector Classification (SVC).

## 🖥️ Live Demo
https://jpuccn64vd2nk6upg8jt3q.streamlit.app

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Performance](#-model-performance)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

This project implements a **Support Vector Machine (SVM)** classifier to predict whether a Titanic passenger would survive based on their demographic and ticket information. The model achieves **82% accuracy** and is deployed as an interactive **Streamlit web application**.

The famous Titanic dataset contains information about passengers who were aboard the ship during its tragic maiden voyage. This ML model analyzes features like passenger class, age, gender, and fare to make survival predictions.

---

## ✨ Features

- 🎨 **Interactive UI** - Beautiful, user-friendly Streamlit interface
- 🧠 **SVM Classifier** - Powered by Support Vector Machine algorithm
- 📊 **Real-time Predictions** - Instant survival predictions with visual feedback
- 🎯 **82% Accuracy** - Well-trained model with robust performance
- 🔢 **Standard Scaling** - Proper feature preprocessing for optimal results
- 🎉 **Bilingual Support** - Friendly messages in English and Urdu
- 📱 **Responsive Design** - Works on desktop and mobile devices

---

## 🎬 Demo

### Input Features:
- **Ticket Class** (1st, 2nd, 3rd)
- **Gender** (Male/Female)
- **Age** (10-100 years)
- **Siblings/Spouse Count** (0-8)
- **Parents/Children Count** (0-6)
- **Fare Amount** ($0-$500)
- **Embarkation Port** (Southampton, Cherbourg, Queenstown)

### Sample Output:
```
✅ Mubarak Ho! Aap Survive Kar Lete!
Survival Status: SURVIVED 🎉
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Programming Language |
| **Streamlit** | Web Application Framework |
| **Scikit-learn** | Machine Learning Library |
| **Pandas** | Data Manipulation |
| **NumPy** | Numerical Computing |
| **Matplotlib** | Data Visualization |
| **Pickle** | Model Serialization |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/FawadAhmad-bilal/titanic-survival-svm.git
cd titanic-survival-svm
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Ensure Model Files are Present
Make sure you have these files in the project directory:
- `model.pkl` (Trained SVM model)
- `scaler.pkl` (StandardScaler object)

---

## 🚀 Usage

### Run the Streamlit App
```bash
streamlit run SVM_PROJECT.py
```

The application will open automatically in your default browser at `http://localhost:8501`

### Making Predictions

1. **Select Ticket Class** - Choose between 1st, 2nd, or 3rd class
2. **Choose Gender** - Select Male or Female
3. **Adjust Age** - Use the slider to set passenger age
4. **Enter Family Details** - Add number of siblings/spouse and parents/children
5. **Input Fare Amount** - Enter the ticket fare
6. **Select Embarkation Port** - Choose where the passenger boarded
7. **Click "Predict My Survival"** - Get instant results!

---

## 📊 Model Performance

### Training Details
```
Algorithm:       Support Vector Classification (SVC)
Accuracy:        82%
Test Split:      80% Training / 20% Testing
Random State:    42
Preprocessing:   StandardScaler
```

### Model Metrics
- **Accuracy Score**: 82%
- **Feature Scaling**: StandardScaler applied to all features
- **Cross-validation**: Performed during training phase

### Feature Importance
The model considers these features in order of impact:
1. Gender (Sex)
2. Passenger Class
3. Fare Amount
4. Age
5. Family Size (SibSp + Parch)
6. Embarkation Port

---

## 📁 Project Structure

```
titanic-survival-svm/
│
├── SVM_PROJECT.py          # Main Streamlit application
├── model.pkl               # Trained SVM model
├── scaler.pkl              # StandardScaler object
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── notebooks/              # Jupyter notebooks (optional)
│   └── model_training.ipynb
│
└── data/                   # Dataset folder (optional)
    └── titanic.csv
```

---

## 🔍 How It Works

### 1. Data Preprocessing
```python
# Features are scaled using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 2. Model Training
```python
# SVM Classifier with RBF kernel
from sklearn.svm import SVC
model = SVC(kernel='rbf', random_state=42)
model.fit(X_train_scaled, y_train)
```

### 3. Prediction Pipeline
```
User Input → Encoding → Scaling → SVM Model → Prediction → Display Result
```

### 4. Feature Encoding
- **Sex**: Male=1, Female=0
- **Embarked**: Southampton=0, Cherbourg=1, Queenstown=2

---

## 🔮 Future Improvements

- [ ] Add data visualization dashboard
- [ ] Implement additional ML algorithms (Random Forest, XGBoost)
- [ ] Add model comparison feature
- [ ] Include SHAP values for explainability
- [ ] Deploy on cloud platforms (Streamlit Cloud, Heroku)
- [ ] Add feature importance visualization
- [ ] Implement A/B testing for model versions
- [ ] Create API endpoint for predictions

## 👨‍💻 Contact

**Fawad**  
BSAI Student | University of Haripur  
Department of Information Technology

-
- LinkedIn:https://www.linkedin.com/in/fawad-ahmad-bilal-78890236b/
- Email: fawadahmad19991@gmail.com

---

## 🙏 Acknowledgments

- Dataset: [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic)
- Scikit-learn documentation and community
- Streamlit for the amazing framework
- All contributors and supporters

---

<div align="center">

### ⭐ If you found this project helpful, please give it a star!

Made with ❤️ by Fawad

</div>
