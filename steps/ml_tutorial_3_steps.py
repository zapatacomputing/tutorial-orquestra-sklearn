from tutorial.functions import *
from tutorial.utils import *

def generate_preprocess_step(dataset_name):
    # Reading the data
    data = generate_dataset(dataset_name)

    # Processing the data
    features, labels = preprocess_data(data)

    # Saving the prediction and score as results
    features_dict = {}
    features_dict['features'] = features
    save_json(features_dict, 'features.json')
    
    labels_dict = {}
    labels_dict['labels'] = labels
    save_json(labels_dict, 'labels.json')

def train_predict_accuracy_step(features, labels, model_name):
    
    feat = read_json(features)['features']
    lab = read_json(labels)['labels']

    # Training the model
    model = train_model(feat, lab, model_name)
    
    # Making predictions
    predictions = make_predictions(model, feat)
    
    # Scoring the model
    accuracy = calculate_accuracy(predictions, lab)
    
    # Saving the prediction and accuracy as results
    result = {}
    result['predictions'] = predictions.tolist()
    result['accuracy'] = accuracy
    save_json(result, 'result.json')
