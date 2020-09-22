import json
import pandas as pd

import json

# Insert file path in the next line
with open('./examples/outputs/ml-3-workflow-output.json') as f:
#with open('./examples/outputs/ml-1-workflow-output.json') as f:
    data = json.load(f)

steps = list(data.keys())

for step in steps:
    if 'result' in data[step].keys():
        print("****** STEP ******")
        result = data[step]['result']
        print("Predictions:")
        for prediction in result['predictions']:
            print(prediction['predictions'])
        print()
        print("Accuracy:")
        print(result["accuracy"])
