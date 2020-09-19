from tutorial.functions import *
from tutorial.utils import *

def generate_data_step(dataset_name):
    data = generate_dataset(dataset_name)
    data_dict = {}
    data_dict['data'] = data
    save_json(data_dict, 'data.json')

def preprocess_data_step(data):
    raw_data = read_json(data)['data']
    features, labels = preprocess_data(np.array(raw_data))

    features_dict = {}
    features_dict['features'] = features
    save_json(features_dict, 'features.json')
    
    labels_dict = {}
    labels_dict['labels'] = labels
    save_json(labels_dict, 'labels.json')

def train_predict_step(features, labels, model_name):
    feat = read_json(features)['features']
    lab = read_json(labels)['labels']

    model = train_model(feat, lab, model_name)
    predictions = make_predictions(model, feat)

    predictions_dict = {}
    predictions_dict['predictions'] = predictions
    save_json(predictions_dict, 'predictions.json')

def calculate_accuracy_step(labels, predictions):
    lab = read_json(labels)['labels']
    pred = read_json(predictions)['predictions']

    accuracy = [calculate_accuracy(pred, lab)]

    accuracy_dict = {}
    accuracy_dict['accuracy'] = accuracy
    save_json(accuracy_dict, 'accuracy.json')