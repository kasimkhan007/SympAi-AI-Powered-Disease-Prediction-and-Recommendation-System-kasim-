SympAi - AI-Powered Disease Prediction and Recommendation System
developed by muhammad kasim s

Overview
SympAi is an innovative AI-driven tool designed to predict diseases and provide personalized health recommendations based on symptoms. Leveraging advanced machine learning (ML) and natural language processing (NLP) techniques, SympAi aims to revolutionize healthcare by offering fast, reliable, and tailored insights.

Key Features
🌟 Accurate Disease Prediction: Utilizes the robust Random Forest model optimized with GridSearch to achieve high accuracy.
🧬 Advanced NLP for Symptom Analysis: FastText for effective symptom vectorization and DistilBERT for context-aware recommendations.
📊 Comprehensive Data Processing: Efficient handling of 5000+ records, including demographics and symptoms, with meticulous preprocessing.
🔍 Real-Time Insights: Provides real-time, actionable health insights to support healthcare professionals and patients.
Tech Stack
Machine Learning: Random Forest, GridSearch, XGBoost
Natural Language Processing: FastText, DistilBERT
Programming Language: Python (with libraries like scikit-learn, pandas, numpy, etc.)
Deployment: Flask (or Streamlit for UI), Docker (optional)
bash
Copy code
git clone https://github.com/kasim/SympAi.git
cd SympAi
Install the Required Packages:

bash
Copy code
pip install -r requirements.txt
Run the Application:

bash
Copy code
python app.py
Usage
Input Symptoms: Enter the symptoms in the user interface.
Get Predictions: The app predicts potential diseases based on input symptoms.
Receive Recommendations: Get personalized health advice and suggested actions.
Screenshots
![kasim app logo sympai](https://github.com/user-attachments/assets/d3b43f14-9a04-41b8-b13a-8cc931f6064c)
![interface4](https://github.com/user-attachments/assets/51aa6c14-2a7b-49be-9722-3100297d5990)
![interface3](https://github.com/user-attachments/assets/e73a3043-644f-469a-b0d0-9e4c0f58a81f)
![interface2](https://github.com/user-attachments/assets/697e1bab-6d37-42d1-abb6-6486c01d1e3b)
![interface1](https://github.com/user-attachments/assets/ff785f90-84af-4b5f-b450-d6688745666f)

How It Works
Data Preprocessing: Utilizes FastText for converting textual symptoms into word vectors and handles missing values using advanced imputation techniques.
Model Training: Random Forest classifier is optimized with GridSearchCV to tune hyperparameters (n_estimators, max_depth, etc.).
Recommendation System: DistilBERT is fine-tuned on medical text to provide personalized, context-aware health advice.
Results
Prediction Accuracy: Achieved 92% accuracy with the Random Forest model.
Recommendation Quality: 85% alignment with expert medical advice.
Performance Metrics: Precision, recall, and F1-score evaluation to validate model performance.
Future Enhancements
Expand the dataset to include more diverse symptoms and conditions.
Integrate more advanced NLP models like GPT-3 for better contextual understanding.
Improve real-time deployment capabilities and user interface.
Contributing
Contributions are welcome! Please feel free to fork this repository, make improvements, and submit a pull request.

License
This project is licensed under the MIT License.

Contact
Created by Muhammad Kasim S
Email: kasimmks2002@gmail.com


