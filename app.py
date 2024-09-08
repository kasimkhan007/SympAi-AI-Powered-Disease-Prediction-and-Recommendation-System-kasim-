from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import pickle
import fasttext
import json
import torch
from transformers import DistilBertTokenizer, DistilBertModel


fasttext_model = fasttext.load_model('fasttext_model.bin')


filename = 'trained_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))
with open('label_encoder_gender.pkl', 'rb') as f:
    loaded_label_encoder_gender = pickle.load(f)
with open('label_encoder_disease.pkl', 'rb') as f:
    loaded_label_encoder_disease = pickle.load(f)


tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')
model.eval()


with open('disease_details-kasim.json', 'r') as file:
    data = json.load(file)


diseases = [entry['predicted_disease'] for entry in data]
descriptions = [entry['description'] for entry in data]
recommendations = [entry['precautions'] + " " + entry['lifestyle_recommendations'] + " " +
                    entry['diet_recommendations'] + " " + entry['exercise_recommendations'] for entry in data]


def get_recommendation_and_description(disease_name):
    try:
        idx = diseases.index(disease_name)
        description = descriptions[idx]

      
        recommendation_dict = {
            'description': data[idx]['description'],
            'precautions': data[idx]['precautions'],
            'lifestyle_recommendations': data[idx]['lifestyle_recommendations'],
            'diet_recommendations': data[idx]['diet_recommendations'],
            'exercise_recommendations': data[idx]['exercise_recommendations']
        }
        return description, recommendation_dict
    except ValueError:
        description = 'No description available for this disease.'
        recommendation_dict = {
            'precautions': 'No precautions available for this disease.',
            'lifestyle_recommendations': 'No lifestyle recommendations available.',
            'diet_recommendations': 'No diet recommendations available.',
            'exercise_recommendations': 'No exercise recommendations available.'
        }
        return description, recommendation_dict


def get_symptom_embeddings(symptoms, fasttext_model):
    symptom_vectors = [fasttext_model.get_word_vector(symptom) for symptom in symptoms.split()]
    return np.mean(symptom_vectors, axis=0)


app = Flask(__name__)
app.secret_key = 'supersecretkey' 


@app.route('/')
def index():
    return render_template('1.html')


@app.route('/input')
def input_page():
    return render_template('2.html')


@app.route('/predict', methods=['POST'])
def predict():
   
    name = request.form['name']
    age = int(request.form['age'])
    gender = request.form['gender']  
    symptoms = request.form['symptoms']

    
    gender_encoded = loaded_label_encoder_gender.transform([gender])[0]

    
    symptoms_list = [symptom.strip() for symptom in symptoms.split(',')]
    symptoms_combined = ' '.join(symptoms_list)

    
    symptom_embeddings = get_symptom_embeddings(symptoms_combined, fasttext_model)

    
    input_features = np.concatenate(([age, gender_encoded], symptom_embeddings))
    input_features = input_features.reshape(1, -1) 

    
    predicted_disease_encoded = loaded_model.predict(input_features)[0]
    predicted_disease = loaded_label_encoder_disease.inverse_transform([predicted_disease_encoded])[0]

    
    session['name'] = name
    session['age'] = age
    session['gender'] = gender
    session['predicted_disease'] = predicted_disease

    
    return redirect(url_for('prediction_result_page'))


@app.route('/prediction_result')
def prediction_result_page():
    name = session.get('name')
    age = session.get('age')
    gender = session.get('gender')
    predicted_disease = session.get('predicted_disease')
    
    return render_template('3.html', name=name, age=age, gender=gender, predicted_disease=predicted_disease)


@app.route('/recommendations')
def recommendation_page():
    name = session.get('name')
    age = session.get('age')
    gender = session.get('gender')
    predicted_disease = session.get('predicted_disease')
    
    
    description, recs = get_recommendation_and_description(predicted_disease)

    return render_template('4.html', 
                           name=name, 
                           age=age, 
                           gender=gender, 
                           predicted_disease=predicted_disease, 
                           description=description,
                           recommendations=recs)

if __name__ == '__main__':
    app.run(debug=True)
