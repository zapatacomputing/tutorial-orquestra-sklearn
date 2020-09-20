import json
import pandas as pd

import json

with open('./examples/outputs/tutorial-1-workflow-output.json') as f:
    data = json.load(f)

steps = list(data.keys())

for step in steps:
    result = data[step]['result']
    print("Predictions")
    for prediction in result['predictions']:
        print(prediction['predictions'])
    print()
    print("Accuracy")
    print(result["accuracy"])
